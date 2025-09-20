from django.db import models
from post.models import Post

class Employee(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='employees')
    hiring_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
