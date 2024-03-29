from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from core.views import ClientViewSet

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]


# ROTA > VIEWS > MODELS > SERIALIZER