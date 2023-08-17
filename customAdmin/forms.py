from django import forms
from django.forms import ModelForm
from jobapp.models import Circular, circularImage


class createCircularForm(ModelForm):
    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = ''
        # verbose_name_plural = 's'
        model = Circular
        fields = "__all__"
