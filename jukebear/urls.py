from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    # Examples:
    # url(r'^$', 'jukebear.views.home', name='home'),
    url(r'^$', RedirectView.as_view(url='jukebox/', permanent=False), name='index'),
    url(r'^jukebox/', include('jukebox.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
