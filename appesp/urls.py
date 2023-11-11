"""gestion_scholarite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from teamd import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.login),
    path('menu/', views.menu,name='menu'),
    
    #urls des enseignants
    
    path('insertEnseignant/', views.insert, name='insert'),
    path('viewEnseignant/', views.view,name='enseignants'),
    path('deleteEnseignant/<id>', views.delete),
    path('editEnseignant/<id>', views.update, name='update'),
    
    #urls des etudiants
    
    path('insertEtudiant/', views.insertE ,name='insertEtudiant'),
    path('viewEtudiant/', views.viewE,name='viewEtudiant'),
    path('deleteEtudiant/<id>', views.deleteE),
    path('editEtudiant/<id>', views.updateE ,name='updateEtudiant'),
    
    #urls des notes
    
    path('insertNote/', views.insertN ,name='insertNote'),
    path('viewNote/', views.viewN,name='viewNote'),
    path('deleteNote/<id>', views.deleteN),
    path('editNote/<id>', views.updateN ,name='updateNote'),
    #urls des modules

    path('menu/list/', views.module_list, name='module_list'),
    path('create/', views.create_module, name='create_module'),
    path('update/<int:pk>/', views.update_module, name='update_module'),
    path('delete/<int:pk>/', views.delete_module, name='delete_module'),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
