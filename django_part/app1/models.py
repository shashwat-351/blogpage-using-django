from django.db import models

# Create your models here.


class blognews(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news/')
    content = models.TextField()
    post_by = models.EmailField()
    posted_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
