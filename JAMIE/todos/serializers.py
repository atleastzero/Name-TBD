from rest_framework import serializers
from .models import Todo, Routine

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('')