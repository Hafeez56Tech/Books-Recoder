from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.create_book, name='create_book'),
    path('book/<int:pk>/edit/', views.update_book, name='update_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),

    path('author/', views.add_author, name='add_author'),
    path('like/', views.like_books, name='like_books'),
    path('like/<int:book_id>/', views.like_book, name='like_book'),

    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    
]
