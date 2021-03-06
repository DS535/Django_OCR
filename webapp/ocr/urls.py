from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

urlpatterns=[
path('status',views.status,name='status'),
path('catchData',views.catchData, name='catchData'),
path('', include(router.urls)),
path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]