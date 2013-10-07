from django.views.generic import ListView

from .models import Speaker


class SpeakerList(ListView):
    model = Speaker
    context_object_name = 'speakers'
