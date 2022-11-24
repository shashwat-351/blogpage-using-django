from django.db import models

# Create your models here.
class blognews(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    post_by = models.EmailField()
    posted_at = models.DateTimeField(auto_now_add=True)
    #pics = models.ImageField()
    def __str__(self):
        return self.title