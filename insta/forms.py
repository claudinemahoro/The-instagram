from .models import Image,Profile,Comment
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'user_profile' , 'likes']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profilepic'] 
        exclude=['user']     
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']


# class registration_form(forms.Form):
#     your_name = forms.CharField(label='First Name',max_length=30)
#     email = forms.EmailField(label='Email')
