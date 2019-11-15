"""inverdana URL Configuration

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
from api import admin
from django.urls import path, include
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from api import views
from landing import views as lviews
#from api import urls
urlpatterns = [
    path('', include('landing.urls')),
    path('inverdana', lviews.inverdana_site, name="Inverdana"),
    path('admin/', admin.admin.urls),
    path('api/', include('api.urls')),
    path("login/", views.login, name="login"),
    path('test/', views.logintest, name="test"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
