
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scholars.models import Scholar
from scholars.serializers import ScholarSerializer

class ScholarView(APIView):
    def get(self,request):

        scholars = Scholar.objects.all()
        print(scholars)
        serializer = ScholarSerializer(scholars, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self,request):

        serializer = ScholarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ScholarSingleView(APIView):
    def put(self, request, id):
        scholar = Scholar.objects.get(id=id)
        serializer = ScholarSerializer(place, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        scholar = Scholar.objects.get(id=id)
        scholar.delete()
        return Response({"Message":"Becario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)