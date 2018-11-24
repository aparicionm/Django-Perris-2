from django.conf.urls import include, url
from . import views
from rest_framework import routers
from api.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'rescatado', views.RescatadoViewSet)

app_name= 'rescatado'

urlpatterns = [
    url(r'^api', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  
]
