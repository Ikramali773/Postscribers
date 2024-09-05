from django import forms
from .models import PostModel, Comments

class PostModelForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'row':4}))
    class Meta:
        model=PostModel
        fields=['title', 'content']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model=PostModel
        fields=['title', 'content']

class CommentModelForm(forms.ModelForm):
    content=forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Add Comment here'}))
    class Meta():
        model=Comments
        fields=('content',)