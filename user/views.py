# coding=utf-8
import json

import uuid
import requests
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from myshop.settings import WX_APP_SECRET
from .models import WxUser


class UserView(APIView):

    def post(self, request):
        js_code = request.data.get('code')
        if not js_code:
            return Response({'messgae': '缺少code'}, status=status.HTTP_400_BAD_REQUEST)
        appid = request.data.get('appId')
        secret = WX_APP_SECRET
        url = 'https://api.weixin.qq.com/sns/jscode2session' + '?appid=' + appid + '&secret=' + secret + '&js_code=' + js_code + '&grant_type=authorization_code'
        response = json.loads(requests.get(url).content)
        print(request.data)
        user_uuid = str(uuid.uuid4())
        openid = response['openid'] if 'openid' in response else None
        session_key = response['session_key'] if 'session_key' in response else None
        if not openid:
            return Response({'message': '微信调用失败'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        user = WxUser
        try:
            user = WxUser.objects.get(openid=openid)
            user.session_key = response['session_key']
            user.uuid = user_uuid
            user.save()
        except Exception:
            nickname = request.data.get('nickname')
            user_sex = request.data.get('gender')
            user_avatar = request.data.get('avatarUrl')
            user = WxUser.objects.create(nickname=nickname, user_sex=user_sex, user_avatar=user_avatar, openid=openid,
                                         session_key=session_key, uuid=user_uuid)
        # return Response(response)
        res = {
            'uuid': user_uuid,
            'msg': 'success'
        }
        return JsonResponse(res)







