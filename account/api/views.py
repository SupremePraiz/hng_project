# from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from account.models import Data
from . serializer import ProfileSerializer




# class ProfileListView(generics.ListAPIView):
#     queryset = Data.objects.all()
#     serializer_class = ProfileSerializer

@api_view(['GET'])
def profile_list(request):
    if request.method == 'GET':
        profiles = Data.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

