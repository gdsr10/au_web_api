"""au_entry URL Configuration

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
from api.views import Login, CenterMaster, UserMaster, EntryDetails, EntryFilter, EntryFilterMC, EntryFilterUS, EntryFilterDate

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API to get/CategoryMaster Scheme
    path('api/login/', Login.LoginView.as_view()),
    
    # API to get/CategoryMaster Scheme
    path('api/centermaster/', CenterMaster.CenterMasterView.as_view()),
    
    # API to get/CategoryMaster Scheme
    path('api/usermaster/', UserMaster.UserMasterView.as_view()),
    
    # API to get/CategoryMaster Scheme
    path('api/entryfilter/', EntryFilter.EntryFilterView.as_view()),
    
    # API to get/CategoryMaster Scheme
    path('api/entryfiltermc/', EntryFilterMC.EntryFilterMCView.as_view()),
    
    # API to get/CategoryMaster Scheme
    path('api/entryfilterus/', EntryFilterUS.EntryFilterUSView.as_view()),
    
    # API to get/CategoryMaster Scheme
    path('api/entryfilterdate/', EntryFilterDate.EntryFilterDateView.as_view()),
    
    # API to get/CategoryMaster Scheme
    path('api/entrydetails/', EntryDetails.EntryDetailsView.as_view()),
    
    # API to get/CategoryMaster Scheme
    path('api/logout/', Login.LoginView.as_view()),
]
