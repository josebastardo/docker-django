from django import forms

from .models import *


class UpimagesuForm(forms.ModelForm):   
    class Meta: 
        model = Upimagesu
        exclude = [ 'visit', 'url'] 
        #fields = ['title', 'image','description', 'url'] 



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('user', 'category', 'title', 'author', 'pdf', 'cover')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text', 'worker')
