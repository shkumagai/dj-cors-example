from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK


class SampleView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, *args, **kwargs):
        content = {
            "message": "You've got an expected response for your GET request.",
        }
        return Response(content, HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        content = {
            "message": "You've got an expected response for your POST request.",
        }
        return Response(content, HTTP_200_OK)
