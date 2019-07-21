from django import forms
from .models import Blog, Comment

class NewBlog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']
        # fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content'] #author 
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 80})
        }

        def save(self, commit=True):
            comment = Comment(**self.cleaned_data)
            if commit:
                comment.save()
            return comment 