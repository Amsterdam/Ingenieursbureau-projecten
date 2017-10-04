from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from app.models import Project

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def projectenGeojson(request):
    projectenList = serialize('geojson',Project.objects.all())
    return HttpResponse(projectenList, content_type='json')