from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .serializers import EventSerializer
from .models import Event


class CreateEventView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ListEventsView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class UpdateEventView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class DeleteEventView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer