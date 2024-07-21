from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Book, Author
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm, BookForm, AuthorForm
def home(request):
    books = Book.objects.all()
    return render(request, 'includes/index.html', {'books': books})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
#-----------------------------Books------------------------
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

# Delete a book
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

def book_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    selected_author = request.GET.get('author')
    if selected_author:
        books = books.filter(author__name=selected_author)
    return render(request, 'books/book_list.html', {'books': books, 'authors': authors})
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@login_required
def like_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.liked_by.filter(id=request.user.id).exists():
        book.liked_by.remove(request.user)
        liked = False
    else:
        book.liked_by.add(request.user)
        liked = True
    return JsonResponse({'liked': liked})

@login_required
def like_books(request):
    books = Book.objects.filter(liked_by=request.user)
    print(books)
    return render(request, 'books/like_books.html', {'books': books})



def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = AuthorForm()
    return render(request, 'author/add_author.html', {'form': form})

from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.conf import settings

def send_liked_books_email(request):
    users = User.objects.all()
    for user in users:
        liked_books = user.liked_books.all()
        if liked_books:
            subject = 'Your Liked Books'
            message = render_to_string('books/email_liked_books.html', {'user': user, 'liked_books': liked_books})
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
            