from django.contrib.auth.models import User
from django.db import models
from django.db.models import SlugField
from django.http import HttpResponseRedirect
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from asstruz import settings


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),)

    title = models.CharField(verbose_name=_('title'),max_length=200, unique=True)
    slug: SlugField = models.SlugField(verbose_name=_('slug'),max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    image = models.ImageField(verbose_name='Photo', upload_to='posts/')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name=_('content'))
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title+" \t  Status:"+self.status

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)