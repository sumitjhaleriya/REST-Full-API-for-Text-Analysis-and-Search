from django.db import models   # type: ignore

class Paragraph(models.Model):
    content = models.TextField()

class Word(models.Model):
    text = models.CharField(max_length=100)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
