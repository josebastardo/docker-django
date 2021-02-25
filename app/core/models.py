from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import uuid
#import django.utils.timezone 


class Upimagesu(models.Model):
    title = models.CharField( max_length=20) # models.OneToOneField( User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description=models.TextField( max_length=600)
    url= models.SlugField(max_length=100, unique=True)
    visit= models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return ('detail', (), {'url' :self.url} )


    class Meta:
        ordering=('visit',)

    def __str__(self):
        return   self.title   #'{} by @{}'.format(self.title, self.create)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Upimagesu, self).save(*args, **kwargs)


class Book(models.Model):
    user = models.ForeignKey('Upimagesu', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


class Comment(models.Model):
    name = models.CharField(max_length=75)
    text =models.TextField( max_length=400)
    worker= models.ForeignKey('Upimagesu', on_delete=models.CASCADE) #revisar!!
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.name)
