from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

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
