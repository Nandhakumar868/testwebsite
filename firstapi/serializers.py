from rest_framework import serializers
from .models import Person, Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']

class FirstSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    class Meta:
        model = Person
        fields = '__all__'

    def validate(self, data):
        
        special_characters = "!@#$%^&*()<>?{}[];'./|\`~"
        if any(c in special_characters for c in data['name']):
            raise serializers.ValidationError('Name should not have special characters')

        if data['age']<18:
            raise serializers.ValidationError('Age is not sufficient')
        