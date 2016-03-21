from django.http import HttpResponseForbidden, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect#, render_to_response
from django.utils.translation import ugettext_lazy as _, get_language

import urllib2
import json

#from rest_framework import serializers, viewsets
#from rest_framework import status
#from rest_framework.decorators import detail_route, list_route
#from rest_framework.response import Response

from social.backends.oauth import BaseOAuth2

class CustomOAuth2(BaseOAuth2):
    """Whiteblackcat OAuth authentication backend"""
    name = 'custom'
    AUTHORIZATION_URL = 'https://accounts.whiteblack-cat.info/o/authorize/'
    ACCESS_TOKEN_URL = 'https://accounts.whiteblack-cat.info/o/token/'
    ACCESS_TOKEN_METHOD = "POST"
    SCOPE_SEPARATOR = ','
    #EXTRA_DATA = [
    #    ('id', 'id'),
    #    ('expires', 'expires')
    #]

    def get_user_details(self, response):
        """Return user details from account"""
        return {'email': response.get('email') or '',
                'first_name': response.get('nickname') or response.get('first_name')}

    def user_data(self, access_token, *args, **kwargs):
        url='https://accounts.whiteblack-cat.info/api/profiles/basicinfo/'
        headers = { "AUTHORIZATION":'Bearer %s' % access_token}#'HTTP_ACCEPT' :'application/json',

        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        jsondata = response.read()
        data=json.loads(jsondata)
        result={"email":data["email"],"first_name":data["nickname"]}
        return result
