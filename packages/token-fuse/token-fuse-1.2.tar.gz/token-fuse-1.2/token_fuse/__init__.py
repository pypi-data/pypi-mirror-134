from .json_web_token import JsonWebToken as Jwt


class JwtFuse:
    """懒加载JwtFuse"""

    def __new__(cls, *args, **kwargs):
        from .json_web_token_fuse import JsonWebTokenFuse

        return JsonWebTokenFuse()


__all__ = ['Jwt', 'JwtFuse']
