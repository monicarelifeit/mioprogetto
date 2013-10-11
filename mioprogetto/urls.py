from django.conf.urls import patterns, include, url
# from django.contrib.auth.models import User, Group
# from cartelle import cartella
from rest_framework import routers

from cartelle.views import UserViewSet
from cartelle.views import GroupViewSet
from cartelle.views import CartellaViewSet

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'cartelle', CartellaViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
