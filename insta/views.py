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

@login_required(login_url='/accounts/login/')
def posts(request):
    follows=Follow.objects.filter(following=request.user.id)
    images = Image.objects.filter(profile = request.user.followings.follower)
    return render(request, 'all-views/post.html',{"images":images})

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    profile = Profile.objects.get(user = request.user.id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.user_profile = profile
            image.save()
        return redirect('profile',current_user.id)

    else:
        form = ImageForm()
    return render(request, 'new_post.html', {"form": form})
