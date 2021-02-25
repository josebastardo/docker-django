
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [

	path('', views.list_photos, name='home'),
	path('upimage', views.upimage, name='upimage'),
	path('books/<slug:url>/', views.book_list_user, name='book_list_user'),
	path('detail/<slug:url>/', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
