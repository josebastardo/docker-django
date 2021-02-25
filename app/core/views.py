
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy


from .forms import *
from .models import *


#@login_required
def upimage(request):
    if request.method == 'POST':
        form = UpimagesuForm(request.POST, request.FILES)
        if form.is_valid():
            #form.clean()
            #form= form.save(commit=False)
            #form.title=request.Worker
            #form.title=request.user.username
            form.save()
        return redirect('/')
            #return HttpResponseRedirect(/home')
    else:
        form = UpimagesuForm()
    return render(request, 'upimage.html', {'form':form})



#@login_required
class UploadedImageView(CreateView):
    model = Upimagesu
    form_class = UpimagesuForm
    success_url = reverse_lazy('/')
    template_name = 'upimage.html'

# cambiar abajo uploadedImage -->upimagesu


def list_photos(request):
    images=Upimagesu.objects.all()
    return render(request, 'list_photos.html', {'images':images})


#@login_required
def detail(request, url):   
    image = get_object_or_404(Upimagesu, url=url)    
    #return render(request, 'detail.html',{'image': image} )
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.image = image
        comment.name=request.user.username
        comment.save()
        request.session["name"] = comment.name

        return redirect(request.path)

    form.initial['name'] = request.session.get('name')

    return render(request, 'detail.html',{'image': image, 'form':form, })


def book_list_user(request, url):
    image= get_object_or_404(Upimagesu, url=url)
    return render(request, 'book_list_user.html', {'image': image, })

###############################



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def book_list(request):   
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', { 'form': form})


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

