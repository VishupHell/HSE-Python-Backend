from django.shortcuts import render

from rest_framework import viewsets
from backend import models
from backend import serializers

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

class UsersAPIViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class PostsAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class CommentsAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('swagger-ui')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('swagger-ui')
    return render(request, 'registration/login.html', {'form': form})
