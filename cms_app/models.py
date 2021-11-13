from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=120)
    profile_pic = models.FileField(blank=True, null=True, upload_to='uploads', verbose_name='Profile Picture')
    biography = models.TextField()

    def __str__(self):
        return self.team_name

    class Meta():
        verbose_name_plural='Our Team'

    def get_profile(self):
        if self.profile_pic:
            return self.profile_pic.url

class Category(models.Model):
    cat_name = models.CharField(max_length=30, verbose_name='Category Name')
    cat_desc = models.TextField(blank=True, null=True, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural = 'Category'


class Post(models.Model):
    pst_title = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pst_image = models.FileField(null=True, blank=True, upload_to='uploads/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural = 'Post'


class Comment(models.Model):
    name = models.CharField(max_length=150)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post.pst_title

    class Meta():
        verbose_name_plural = 'Comment'

