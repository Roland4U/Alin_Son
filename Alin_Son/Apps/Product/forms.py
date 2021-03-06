from django import forms
from .models import *
from django.core.exceptions import ValidationError


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == "new" or "create":
            raise ValidationError('Slug may not be "{}"'.format(new_slug))
        elif Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))

        return new_slug


    def save(self):
        new_category = Category.objects.create(
            title=self.cleaned_data['title'],
            slug=self.cleaned_data['slug']
        )
        return new_category



class ProductForm(forms.ModelForm):

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == "new" or "create":
            raise ValidationError('Slug may not be "{}"'.format(new_slug))
        elif Post.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))

        return new_slug



    class Meta:
        model = Product
        fields = ['title', 'slug', 'body', 'tags', 'autor']

        atrs = {'class': 'form-control'}

        widgets = {
            'title': forms.TextInput(attrs=atrs),
            'slug': forms.TextInput(attrs=atrs),
            'body': forms.Textarea(attrs=atrs),
            'tags': forms.SelectMultiple(attrs=atrs),
            'autor': forms.TextInput(attrs=atrs),

        }
    
# class CommentForm(forms.ModelForm):
#     class Meta:
        
#         atrs = {'class': 'form-control'}
        
#         model = Comment
#         fields = ['autor', 'comment']

#         widgets = {
#             'autor': forms.TextInput(attrs=atrs),
#             'comment': forms.Textarea(attrs=atrs)
#         }