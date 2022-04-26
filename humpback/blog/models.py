from django.db import models
import os

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    head_image=models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True)
    file_upload=models.FileField(upload_to='blog/file/%Y/%m/%d/',blank=True)
    def get_absulute_url(self):
        return f'/blog/{self.pk}/'

    # 파일명얻기
    # def get_file_name(self):
    #     return os.path.basename(self.file_upload.name)
    # 파일 확장자 얻기
    # def get_file_ext(self):
    #     return self.get_file_name().split('.')[-1]