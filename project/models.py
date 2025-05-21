from django.db import models


class Project(models.Model):
    title = models.CharField("Название проекта", max_length=200)
    address = models.CharField("Адрес", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to='project/projects/')
    is_flipped = models.BooleanField("Перевёрнут", default=False)

    def __str__(self):
        return self.title


class ProjectDetail(models.Model):
    project = models.ForeignKey(Project, related_name='details', on_delete=models.CASCADE)
    text = models.CharField("Деталь", max_length=255)

    def __str__(self):
        return f"{self.project.title} - {self.text}"
