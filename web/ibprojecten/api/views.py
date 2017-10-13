from django.views.generic import TemplateView
#from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from ibprojecten.api.models import (Project,
                                    Employee,
                                    Rol,
                                    ProjectType,
                                    HoofdType,
                                    Organisatie,
                                    Werkorder,
                                    WerkorderType)
from ibprojecten.api.serializers import (ProjectSerializer,
                                         EmployeeSerializer,
                                         ProjectGeoJsonSerializer,
                                         RoleSerializer,
                                         ProjectTypeSerializer,
                                         HoofdTypeSerializer,
                                         OrganisationSerializer,
                                         WerkorderSerializer,
                                         WerkorderTypeSerializer)

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


#def projectenGeojson(request):
#    projectenList = serialize('geojson',Project.objects.all())
#    return HttpResponse(projectenList, content_type='json')


class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RoleViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Rol.objects.all()
    serializer_class = RoleSerializer


class HoofdTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = HoofdType.objects.all()
    serializer_class = HoofdTypeSerializer


class ProjectTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer


class WerkorderTypeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = WerkorderType.objects.all()
    serializer_class = WerkorderTypeSerializer


class OrganisationViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Organisatie.objects.all()
    serializer_class = OrganisationSerializer


class WerkorderViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Werkorder.objects.all()
    serializer_class = WerkorderSerializer


def projectenList(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        projecten = Project.objects.all()
        serializer = ProjectGeoJsonSerializer(projecten, many=True)
        return JsonResponse(serializer.data, safe=False)


def projectDetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProjectGeoJsonSerializer(project)
        return JsonResponse(serializer.data)
