from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.viewsets import ReadOnlyModelViewSet

router = DefaultRouter()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router.register('data', UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^schema/$', get_schema_view(title='api')),
    url(r'^docs/', include_docs_urls(title='api', public=False, description='api')),
    url(r'^', include(router.urls)),
]
