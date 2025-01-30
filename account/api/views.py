from rest_framework import generics
from account.models import Data
from . serializer import ProfileSerializer



class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = ProfileSerializer




