from rest_framework import serializers
from scholars.models import Scholar  #De becario se trae Becario

class ScholarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholar
        fields = '__all__'
