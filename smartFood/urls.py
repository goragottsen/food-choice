"""smartFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#import motion.views

# Listed here are the standard URL paths that users/admins can navigate to.
urlpatterns = [
    path('', include('taste.urls')),
    path('admin/', admin.site.urls),
    path('taste/', include('taste.urls')),
#    path('motion/', include('motion.urls')),
#    path('motion/', motion.views.index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
