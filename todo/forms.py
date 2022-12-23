from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = "__all__"
        fields = ['id', 'name', 'detail', 'importance']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'todo_name'}),
            'detail': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'details'}),
            'importance': forms.Select(
                attrs={'class': 'form-control', 'id': 'impoortance'}),

        }
