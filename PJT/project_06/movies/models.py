from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.CharField(max_length=20)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    
    class Meta:
        ordering = ('-pk',)

    def get_absolute_url(self):
        return reverse("movies:detail", kwargs={'movies_pk': self.pk})

class Review(models.Model):
    content = models.CharField(max_length=100)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pk',)