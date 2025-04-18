from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=255)
    answers = models.JSONField()
    correct_answer = models.CharField(max_length=10)
    points = models.IntegerField(default=1)

    def __str__(self):
        return self.text