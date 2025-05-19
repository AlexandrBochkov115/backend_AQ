from rest_framework import serializers
from .models import Pool, PoolImage, PoolDescription


class PoolImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = PoolImage
        fields = ['id', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None


class PoolListSerializer(serializers.ModelSerializer):
    main_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Pool
        fields = ['id', 'name', 'description_short', 'main_image_url', 'slug']

    def get_main_image_url(self, obj):
        if obj.main_image:
            return obj.main_image.url
        return None


class PoolDetailSerializer(serializers.ModelSerializer):
    images = PoolImageSerializer(many=True, read_only=True)
    description = serializers.SerializerMethodField()
    main_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Pool
        fields = [
            'id', 'name', 'description_short', 'description',
            'slug', 'main_image_url', 'images'
        ]

    def get_description(self, obj):
        if hasattr(obj, 'description_obj'):
            return obj.description_obj.description
        return None

    def get_main_image_url(self, obj):
        if obj.main_image:
            return obj.main_image.url
        return None