from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from .models import Image,User,Profile,Follow,Comment
# from .forms import ImageForm,UpdateProfile,CommentForm
# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user= request.user
    all_images=Image.objects.all()
    profile=Profile.objects.all()
    return render(request, 'all-views/index.html',{"images":all_images})
