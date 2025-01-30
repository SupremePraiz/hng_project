from rest_framework import generics
from account.models import Data
from . serializer import ProfileSerializer



class ProfileListView(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = ProfileSerializer




