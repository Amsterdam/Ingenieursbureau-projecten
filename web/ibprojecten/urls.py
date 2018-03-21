"""ibprojecten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# Added to open Files on dev server
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from ibprojecten.api.views import (HomePageView,
                                   projectenList,
                                   projectDetail,
                                   ProjectViewSet,
                                   EmployeeViewSet,
                                   RoleViewSet,
                                   ProjectTypeViewSet,
                                   OrganisationViewSet,
                                   WerkorderTypeViewSet,
                                   HoofdTypeViewSet)


router = DefaultRouter()
router.register(prefix='projects', viewset=ProjectViewSet)
router.register(prefix='employees', viewset=EmployeeViewSet)
router.register(prefix='roles', viewset=RoleViewSet)
router.register(prefix='projecttype', viewset=ProjectTypeViewSet)
router.register(prefix='hoofdtype', viewset=HoofdTypeViewSet)
router.register(prefix='werkordertype', viewset=WerkorderTypeViewSet)
router.register(prefix='organisation', viewset=OrganisationViewSet)

urlpatterns = router.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/projecten/$', projectenList, name='projecten'),
    url(r'^api/projecten/(?P<pk>[0-9]+)/$', projectDetail),
    url(r'^$', HomePageView.as_view(), name='home'),
]


# To open Files on development server add this:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)