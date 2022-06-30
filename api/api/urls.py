from django.contrib import admin
from django.urls import path, include
from core.views import PessoaViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register('Pessoas', PessoaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
