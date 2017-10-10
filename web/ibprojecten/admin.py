from django.contrib import admin
from ibprojecten.api.models import Project, Employee, Rol, Werkorder, ProjectType, ProjectPlan, Organisatie
from leaflet.admin import LeafletGeoAdmin

# Change header name
admin.site.site_header = 'Startdocument Project Ingenieursbureau'

# Register your models here.

# //////////////////////////////////////////////
# Option lists
# /////////////////////////////////////////////


class OrganisatiesAdmin(admin.ModelAdmin):
    list_organisaties = ('Cluster', 'Organisatie')


admin.site.register(Organisatie, OrganisatiesAdmin)


class ProjectleidersAdmin(admin.ModelAdmin):
    list_employees = ('Voornaam', 'Achternaam')


admin.site.register(Employee, ProjectleidersAdmin)


class RolesAdmin(admin.ModelAdmin):
    list_roles = ('Rol')
   # filter_horizontal = ('user',)


admin.site.register(Rol, RolesAdmin)

class ProjectTypeAdmin(admin.ModelAdmin):
    list_roles = ('ProjectType')

admin.site.register(ProjectType, ProjectTypeAdmin)


class WerkorderAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_werkorders = ('Werkordernaam')


admin.site.register(Werkorder, WerkorderAdmin)


# Subproject list view in project
class WerkorderInline(admin.StackedInline):
    model = Werkorder
    show_change_link = True
    extra = 0


class ProjectPlanAdmin(admin.ModelAdmin):
    list_projectplan = ('Projectplan')


admin.site.register(ProjectPlan, ProjectPlanAdmin)


# Subproject list view in project
class ProjectPlanInline(admin.StackedInline):
    model = ProjectPlan
    show_change_link = True
    extra = 0


# //////////////////////////////////////////////
# Main Project
# /////////////////////////////////////////////


class ProjectenAdmin(LeafletGeoAdmin, admin.ModelAdmin):
    list_projects = ('name')
    inlines = [WerkorderInline, ProjectPlanInline]


admin.site.register(Project, ProjectenAdmin)


