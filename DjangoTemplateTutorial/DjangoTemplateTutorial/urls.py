from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'DjangoTemplateTutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #defining a new URL pattern
    #when we will go here our template will render
    url(r'^firsttemplate/', views.index),
]
