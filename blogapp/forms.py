from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name', 'name')

# double notation of name requirement for select structure it is ridiclius but i guess one of them value one of them return

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "header_image", "body"]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write text'}),
        }

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "category", "header_image", "body"]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write text'}),
        }
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
