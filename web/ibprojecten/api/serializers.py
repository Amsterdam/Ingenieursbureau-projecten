from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from ibprojecten.api.models import (Project,
                                    Employee,
                                    Rol,
                                    Organisatie,
                                    ProjectPlan,
                                    ProjectType,
                                    Werkorder,
                                    )


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = Employee
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = Project
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = Rol
        fields = '__all__'


class ProjectTypeSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = ProjectType
        fields = '__all__'


class OrganisationSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Employee model """
    class Meta:
        model = Organisatie
        fields = '__all__'


class EmployeeField(serializers.StringRelatedField):
    def to_representation(self, value):
        return ('{} {}'.format(value.Voornaam, value.Achternaam),value.Email)
    #def get_huurder(self, obj):
    #    vo = obj.Ambtelijkopdrachtgever
    #   request = self.context.get('request')
    #   return EmployeeDetailSerializer(vo, many=False, context={'request':request}).data


class ProjectGeoJsonSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    #Ambtelijkopdrachtgever = EmployeeDetailSerializer(many=False, read_only=True, source = 'Ambtelijk_opdrachtgever')
    #Opdrachtverantwoordelijke = EmployeeDetailSerializer(many=False, read_only=True, source = 'Opdracht_verantwoordelijke')
    #Bestuurlijkopdrachtgever = EmployeeDetailSerializer(many=False, read_only=True, source = 'Bestuurlijk_opdrachtgever')
    #Deelprojectleider = EmployeeDetailSerializer(many=False, read_only=True, source = 'Deel_projectleider')
    #Accounthouder = EmployeeDetailSerializer(many=False, read_only=True, source = 'Account_houder')

    Ambtelijkopdrachtgever = EmployeeField(many=False, read_only=True, source = 'Opdracht_verantwoordelijke')
    Bestuurlijkopdrachtgever = EmployeeField(many=False, read_only=True, source = 'Bestuurlijk_opdrachtgever')
    Opdrachtverantwoordelijke = EmployeeField(many=False, read_only=True, source = 'Opdracht_verantwoordelijke')
    Deelprojectleider = EmployeeField(many=False, read_only=True, source = 'Deel_projectleider')
    Accounthouder = EmployeeField(many=False, read_only=True, source = 'Account_houder')
    

    class Meta:
        model = Project
        geo_field = 'Plangebied'
        fields = [
            'Projectnaam',
            'Type',
            'Opdrachtverantwoordelijke',
            'Ambtelijkopdrachtgever',
            'Bestuurlijkopdrachtgever',
            'Deelprojectleider',
            'Accounthouder',
            'startdatum',
            'einddatum',
            #'Plangebied',
            ]