from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

class Post(models.Model):

    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    post= models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user_posts',on_delete=models.CASCADE)
    message = models.TextField()
    message_html = models.TextField(editable=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.message, self.user)

    def save(self,*args,**kwargs):
        self.message_html=misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single')

    class Meta:
        ordering =['-created_at']
