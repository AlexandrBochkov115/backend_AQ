# serializers.py
from rest_framework import serializers
from .models import Project, ProjectDetail

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetail
        fields = ['text']

class ProjectSerializer(serializers.ModelSerializer):
    details = ProjectDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'address', 'description', 'image', 'is_flipped', 'details']
