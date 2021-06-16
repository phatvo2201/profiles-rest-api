from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status,viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from . import serializers
from rest_framework.authentication import TokenAuthentication
from profiles_api import models
from profiles_api import permissions

class UserLoginApiView(ObtainAuthToken):
    renderer_classes =api_settings.DEFAULT_RENDERER_CLASSES



class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class= serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()

    authentication_classes= (TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)












class HelloApiView(APIView):
    serializer_class= serializers.HelloSerializer
    def get(self,request,format=None):
        an_apiview=['Uses http method as a function'
        ,'is similar to a traditional django view'
        'give most control000',
        'is maooed manually to urls']

        return Response({'massage0':'an_apiview','an_apiview':an_apiview})
# Create your views here.
    def post(self,request):
        serializer= self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello{name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST

            )

class HelloViewSet(viewsets.ViewSet):
        """test api view set"""
        serializer_class=serializers.HelloSerializer

        def list(self,request):
            """return a hello """
            an_aviewset=['Uses http method as a function(list,create retieve update)'
            ,'is similar to a traditional django view'
            'give most control000',
            'is maooed manually to urls']
            return Response({'message':"hello","a-viewset":an_aviewset})
        def create(self,request):
            serializer=self.serializer_class(data=request.data)
            if serializer.is_valid():
                name=serializer.validated_data.get('name')
                message=f'hello the {name}'
                return Response({'message':message})
            else:
                return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        def update(self,request,pk=None):
            return Response({'message':'PUT'})

        def retrieve(self,request,pk=None):
            return Response({'message':'GET'})
        def destroy(self,request,pk=None):
            return Response({'message':'Delete'})
