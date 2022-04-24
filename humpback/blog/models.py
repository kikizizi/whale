from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    head_image=models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True)
    def get_absulute_url(self):
        return f'/blog/{self.pk}/'
