from .models import Song
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class SongList(APIView):
    def get(self, request, format=None):
        return Response('SongList says hi')
        pass

    def post(self, request, format=None):
        pass

class SongDetail(APIView):
    #helper function
    def get_object(self,pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        return Response('SongDetail says hi')
        pass

    def put(self, request, pk, format=None):
        pass

    def delete(self, request, pk, format=None):
        pass

    

