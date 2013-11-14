from django.views.generic import ListView

from .models import Speaker


class SpeakerList(ListView):
    queryset = Speaker.objects.order_by('order')
    context_object_name = 'speakers'
