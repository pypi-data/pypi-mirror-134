import json
import pickle
import heapq
import redis
from .json_web_token import JsonWebToken
from .judge_pc_or_mobile import judge_pc_or_mobile
from .auth_failed import AuthFailed
from django.conf import settings

jwt_conf = getattr(settings, 'JWT_CONF', {})
redis_params = jwt_conf.get('redis', dict(host='127.0.0.1', port=6379, db=0))
pool = redis.ConnectionPool(**redis_params)
rds = redis.Redis(connection_pool=pool)
MAX_LOGIN = jwt_conf.get('max_login', 1)


class JsonWebTokenFuse(JsonWebToken):

    def token(self, payload: dict, request=None):
        """根据payload生成token，
        :param payload:
            必选参数有: 1.exp 过期时间 ，now > exp 则失效
                      2.iat：签发时间戳 。
                      3.uid：用户辨识用户的唯一id，建议[uid, user]任选一种作为参数名都可以
            可选参数有：
                      1.iss:签发人，在同一台服务器中如果存在多个项目（多项目共用了Redis数据池），
                      如果这些项目不是共享token，那么在JwtRange().auth()时为了防止token串号，可以设置iss用于区分。
        :param request:
            如果传入了request参数，则默认生成带有设备信息的token；
            根据request中的User-Agent将访问的请求区分为移动和PC两种设备类型。
            再将设备类型{'ua':'m'}或{'ua':'p'}更新到payload中，最后使用带有设备类型标记的payload生成token。
            不同设备类型不共享max_login,也就是说max_login=1时，ua:p和ua:m的设备能同时登录访问
        :return: 生成的token"""

        if 'iat' not in payload or ('uid' not in payload and 'user' not in payload):
            raise ValueError('payload中不存在iat或uid(或user)！')
        if request:
            ua = request.headers.get('User-Agent')
            ua = 'm' if judge_pc_or_mobile(ua) else 'p'
            payload.update({'ua': ua})
        return super().token(payload=payload)

    def _generate_key_name(self, payload: dict):
        """生成token在Redis中的键名"""
        uid = payload.get('uid') or payload.get('user')  # 用户表示在payload中为user或uid
        if not uid:
            raise TypeError('payload中没有配置uid或user')
        ua = payload.get('ua')  # 返回mobile或者pc，不区分设备的token返回None
        iss = payload.get('iss') or 'no_iss'  # 如果没有指定签发人 则把iss默认为'token'
        token_key_name = str(uid) + '<' + ua + '>' if ua else str(uid)
        token_key_name = '<' + iss + '>' + token_key_name  # token在Redis中的键名
        return token_key_name

    def _push_queue(self, queue: list, token):
        """将token存入queue，队列长度不会超过max_len，queue中的token永远保持最新的max_len条（根据签发时间），
        也就是说如果queue已经存满（长度为max_len），且token的签发时间比队列中最小的签发时间还小,token将不会被存入（存入后会被pop掉）
        :param token:需要存入的token
        :return:返回一个保存token的列表，格式：[(iat,token), ...]"""
        _, payload, *_ = token.split('.')
        payload = json.loads(self.enc.debase64(payload, alt_chars='-_'))
        item = (payload['iat'], token)  # iat签发时间
        if item not in queue:
            heapq.heappush(queue, item)
        if len(queue) > MAX_LOGIN:
            heapq.heappop(queue)
        return queue

    def auth(self, token: str):
        """验证token 只允许max_len条token有效"""
        try:
            payload = super().auth(token)
            if isinstance(payload, AuthFailed):  # 如果token没有验证通过，返回payload（此时payload为AuthFailed()对象）
                return payload

            token_key_name = self._generate_key_name(payload)  # 生成token在Redis中的键名
            token_queue_byte = rds.get(token_key_name)  # Redis中取出来的类型为byte类型
            if not token_queue_byte:  # Redis中没有该用户的token列表（token_queue），说明是首次登录
                # 将token存入队列，如果队列已经存满（长度为max_len），
                # 且token的签发时间比队列中最小的签发时间还小,token将不会被存入（存入会被pop掉）
                token_queue = self._push_queue(list(), token)
            else:
                token_queue = self._push_queue(pickle.loads(token_queue_byte), token)
            # 存入redis的过期时间为3600秒 意味着3600秒后该token可以正常访问
            rds.set(token_key_name, pickle.dumps(token_queue), 3600)
            if token in [i[-1] for i in token_queue]:
                return payload
            else:
                return AuthFailed('token超出允许的数量范围')  # 103: token超出允许的数量范围

        except Exception as err:
            return AuthFailed(str(err))  # 103: token超出允许的数量范围
