from django.conf.urls import patterns, url

from .views import SpeakerList


urlpatterns =  patterns(
    '',
    url(r'^$', SpeakerList.as_view()),
)
