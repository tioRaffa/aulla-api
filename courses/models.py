from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CourseModels(Base):
    title = models.CharField(max_length=150)
    url = models.URLField(unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
    

class ReviewModels(Base):
    course = models.ForeignKey(CourseModels, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    comment = models.TextField(blank=True, default='')
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        unique_together = ['email', 'course']
        ordering = ['id']

    def __str__(self):
        return f'{self.name} rated the {self.course} course with a score of {self.rating}'