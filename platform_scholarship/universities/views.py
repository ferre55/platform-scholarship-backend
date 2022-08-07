
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from universities.models import University
from universities.serializers import UniversitySerializer

class UniversityView(APIView):
    def get(self,request):

        universities = University.objects.all()
        print(universities)
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    def post(self,request):

        serializer = UniversitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UniversitySingleView(APIView):
    def put(self, request, id):
        university = University.objects.get(id=id)
        serializer = UniversitySerializer(place, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        university = University.objects.get(id=id)
        university.delete()
        return Response({"Message":"Universidad eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)
