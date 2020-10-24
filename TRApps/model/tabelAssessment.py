from django.db import models

class Assessment(models.Model):
    file = models.ImageField(upload_to='images/')
    score = models.IntegerField(null=True)

    def __str__(self):
        return self.file+"-"+self.score