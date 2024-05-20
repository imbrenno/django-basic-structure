from rest_framework import serializers
from main.database.models.person_model import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
