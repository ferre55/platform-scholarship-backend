from rest_framework import serializers
from universities.models import University  #De Univer se trae Becario

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'