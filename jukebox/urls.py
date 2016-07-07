from django.conf.urls import url


from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^([0-9]*)$', views.index, name='index'),
    url(r'^update_playlist$', views.update_playlist, name='update_playlist'),

]