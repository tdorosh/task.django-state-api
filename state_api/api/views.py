from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

from states.models import State
from .serializers import StateSerializer


class RandomStateAPIView(APIView):

    @extend_schema(responses={200: StateSerializer})
    def get(self, request):
        random_state = State.objects.order_by('?').first()
        serializer = StateSerializer(random_state)
        return Response(serializer.data)
