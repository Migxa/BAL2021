from django.db import models
from django.template.defaultfilters import slugify

class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    points = models.IntegerField(default=0)
    slug = models.CharField(max_length=32, unique=True)
    late = models.IntegerField(default=0)
    first = models.IntegerField(default=0)
    second = models.IntegerField(default=0)
    third = models.IntegerField(default=0)
    color = models.CharField(max_length=32, default="white")



    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name

# Create your models here.
