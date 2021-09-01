from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST,require_GET
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero

import json

# Create your views here.
@require_GET
def status(request):
    return JsonResponse({"server":"Ready"}, status=202)
    
@csrf_exempt    
@require_POST
def catchData(request):
    received_data=json.loads(request.body)
    requestor_name=received_data.get("requestedby")
    return JsonResponse({"requestedby":requestor_name,"status":"success"},status=202)


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer