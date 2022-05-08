from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class ArticlePost(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/')
    intro = models.TextField(max_length=2555, null=True)
    count = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug


