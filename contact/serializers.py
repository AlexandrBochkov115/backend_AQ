from rest_framework import serializers
from .models import Contact
import phonenumbers

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'phone_number', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_full_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("ФИО не может быть пустым.")
        if len(value) > 150:
            raise serializers.ValidationError("ФИО слишком длинное (максимум 150 символов).")
        return value

    def validate_phone_number(self, value):
        try:
            # Парсим номер с указанием региона России
            phone_obj = phonenumbers.parse(value, "RU")
            if not phonenumbers.is_valid_number(phone_obj):
                raise serializers.ValidationError("Номер телефона недействителен.")
            # Нормализуем в формат +7XXXXXXXXXX
            return phonenumbers.format_number(phone_obj, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise serializers.ValidationError("Неверный формат номера телефона.")
