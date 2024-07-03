from django import forms

from shop.models import Comment, Order


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'email',)