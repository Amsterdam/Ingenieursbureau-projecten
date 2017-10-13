#from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import datetime

# /////////////////////////////////////////////////
# Option menu's
# /////////////////////////////////////////////////

class Organisatie(models.Model):
    org_id = models.AutoField(primary_key=True)
    Cluster = models.CharField(max_length=255, null=True)
    Organisatie = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{} - {}'.format(self.Cluster, self.Organisatie)

    class Meta:
        db_table = 'organisatie'


class Rol(models.Model):
    role_id = models.AutoField(primary_key=True)
    Rol = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.Rol)

    class Meta:
        db_table = 'rol'

class HoofdType(models.Model):
    class_id = models.AutoField(primary_key=True)
    HoofdtypeAfkorting = models.CharField(max_length=255, null=True)
    Hoofdtype =  models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.Hoofdtype) 


    class Meta:
        db_table = 'hoofdtype'

class ProjectType(models.Model):
    type_id = models.AutoField(primary_key=True)
    Soort = models.CharField(max_length=255, null=True)
    Hoofdtype = models.ManyToManyField(HoofdType,
                            related_name='hoofdtype_aard'
                            )
    def __str__(self):
        return '{}'.format(self.Soort)

    class Meta:
        db_table = 'projecttype'

class WerkorderType(models.Model):
    type_id = models.AutoField(primary_key=True)
    Werkordertype = models.CharField(max_length=255, null=True)

    def __str__(self):
        return '{}'.format(self.Werkordertype)
 
    class Meta:
        db_table = 'werkordertype'


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    Voornaam = models.CharField(max_length=255, null=True)
    Achternaam = models.CharField(max_length=255, null=True)
    Email = models.CharField(max_length=128, null=True)
    Telefoon = models.CharField(max_length=128, null=True)
    Rol = models.ForeignKey(Rol,
                            related_name='collegue_role',
                            on_delete=models.CASCADE,
                            null=True)
    ZoekeenCollegaUrl = models.CharField(max_length=128, blank=True, null=True)

    def Functie(self):
        return '{}'.format(self.Rol.Rol)

    def __str__(self):
        return '{} - {} {}'.format(self.Rol, self.Voornaam, self.Achternaam)

    def fullName(self):
        return '{} {}'.format(self.Voornaam, self.Achternaam)


    class Meta:
        db_table = 'employee'


# /////////////////////////////////////////////////
# Main Project
# /////////////////////////////////////////////////

class Project(models.Model):
    pjid = models.AutoField(primary_key=True)
    Locatie = models.CharField(max_length=255, blank=False)
    Hoofdtype = models.ForeignKey(HoofdType, related_name='hoofd_type_project', on_delete=models.CASCADE, null=True)
    Aard = models.ManyToManyField(ProjectType, related_name='project_type_project')
    Intakedatum = models.DateField(blank=False, default=datetime.now)

    startdatum = models.DateField(blank=False, default=datetime.now)
    einddatum = models.DateField(blank=False, default=datetime.now)

    Plangebied = models.PolygonField(srid=4326, null=True)

    Organisatie_opdrachtgever = models.ForeignKey(Organisatie, blank=True, related_name='organisatie_project', on_delete=models.CASCADE, null=True)

    Bestuurlijk_opdrachtgever = models.ForeignKey(Employee, related_name='administrativeclient_project', on_delete=models.CASCADE, blank=True, null=True)
    Ambtelijk_opdrachtgever = models.ForeignKey(Employee, blank=True, related_name='officialclient_project', on_delete=models.CASCADE, null=True)
    Opdracht_verantwoordelijke = models.ForeignKey(Employee, blank=False, related_name='maincontractor_project', on_delete=models.CASCADE, null=True)
    Deel_projectleider = models.ForeignKey(Employee, blank=True, related_name='subcontractor_project', on_delete=models.CASCADE, null=True)
    Account_houder = models.ForeignKey(Employee, blank=True, related_name='accountant_project', on_delete=models.CASCADE, null=True)

    Timetellnummer = models.CharField(max_length=18, blank=True, null=True)

    # Convert manytomany list into a string 
    @property
    def Type(self):
        return self.Hoofdtype

    @property
    def AardList(self):
        return ', '.join([a.Soort for a in self.Aard.all()])
 
 

    @property
    def Jaar(self):
        return '{}'.format(self.startdatum.year)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.pjid, self.Type, self.AardList, self.Locatie, self.Jaar )

    objects = models.GeoManager()

    Indicatiebedrag = models.DecimalField(max_digits=9,
                                          decimal_places=2,
                                          blank=True,
                                          default=0.00)
    Maximumbedrag = models.DecimalField(max_digits=9,
                                        decimal_places=2,
                                        blank=True,
                                        default=0.00)
    Vervolgafspraken = models.TextField(max_length=None,
                                        blank=True,
                                        null=True)

    class Meta:
        db_table = 'project'

# Subprojects


class Werkorder(models.Model):
    werkorder_id = models.AutoField(primary_key=True)
    startdatum = models.DateField(blank=False, default=datetime.now)
    einddatum = models.DateField(blank=False, default=datetime.now)
    Werkordertype = models.ForeignKey(WerkorderType,
                                related_name='werkordertype_werkorder_set',
                                on_delete=models.CASCADE, blank=True, null=True)
    Timetellnummer = models.CharField(max_length=18, blank=True, null=True)
    TimetellNaam = models.CharField(max_length=255, blank=True, null=True)
    Boekingscombinatie = models.CharField(max_length=18, blank=True, null=True)
    WerkorderPlangebied = models.PolygonField(srid=4326, blank=True, null=True)
    Project = models.ForeignKey(Project,
                                related_name='werkorder_project_set',
                                on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{}-{}'.format(self.Project.Locatie, self.Werkordertype)

    objects = models.GeoManager()

    class Meta:
        db_table = 'werkorder'


def project_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'projectplannen/project_{0}/{1}'.format(instance.Project.pjid,
                                                   filename)


class ProjectPlan(models.Model):
    pp_id = models.AutoField(primary_key=True)
    Projectplan = models.FileField(upload_to=project_directory_path, blank=True)
    Aanleiding = models.CharField(max_length=2000, blank=True, null=True)
    Doel = models.CharField(max_length=2000, blank=True, null=True)
    Resultaat = models.CharField(max_length=2000, blank=True, null=True)
    Afbakening = models.CharField(max_length=2000, blank=True, null=True)
    Project = models.ForeignKey(Project, related_name='projectplan_project_set', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return '{}-{}'.format(self.pp_id, self.Projectplan)

    class Meta:
        db_table = 'projectplan'


