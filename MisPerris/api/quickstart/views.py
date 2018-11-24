from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.quickstart.serializers import UserSerializer, GroupSerializer, RescatadoSerializer
from blog.models import Rescatado

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class RescatadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Rescatado.objects.all()
    serializer_class = RescatadoSerializer
