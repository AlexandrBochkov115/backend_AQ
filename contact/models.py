from django.db import models

class Contact(models.Model):
    full_name = models.CharField("ФИО", max_length=150)
    phone_number = models.CharField("Номер телефона", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"
