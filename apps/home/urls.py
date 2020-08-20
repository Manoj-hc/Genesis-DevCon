from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('speakers/', views.speakers, name='speakers'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('attendees/', views.attendees, name='attendees'),
    path('our-story/', views.our_story, name='our-story'),
    path('agenda/', views.agenda, name='agenda'),
    path('contest/', views.contest, name='contest'),
    path('api/subscribe-user/', views.subscribe_user, name='subscribe-user'),
    path('api/speaker-application/', views.speaker_application, name='speaker-application'),
    path('api/prospect-application/', views.prospect_application, name='prospect-application'),
    path('genesisdevcon2020/', views.devcon, name='devcon'),
]
