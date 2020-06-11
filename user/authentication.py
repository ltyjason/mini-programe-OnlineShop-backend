# from django_redis import get_redis_connection
# from rest_framework import exceptions
# from rest_framework.authentication import BaseAuthentication
#
#
# class UserAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         if 'HTTP_SKEY' in request.META:
#             skey = request.META['HETTP_SKRY']
#             conn = get_redis_connection('default')
#             if conn.exists(skey):
#                 user = conn.get(skey)
#                 return (user, skey)
#             else:
#                 raise exceptions.AuthenticationFailed(detail={'code': 401, 'msg': 'skey已过期'})
#         else:
#             raise exceptions.AuthenticationFailed(detail={'code': 400, 'msg': '缺少skey'})
#
#     def authenticate_header(self, request):
#         return 'skey'
