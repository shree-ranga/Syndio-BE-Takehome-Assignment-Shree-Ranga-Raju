from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class GetPValue(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"args": args}, status=status.HTTP_200_OK)
