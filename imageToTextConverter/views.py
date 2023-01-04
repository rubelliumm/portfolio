from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.http import HttpResponse
from PIL import Image
import pytesseract


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            lang = request.POST['lang']
            file = request.FILES['file']
            text = pytesseract.image_to_string(Image.open(file), lang=lang)
            return render(request, 'converter/home.html', {'form': form, 'text': text})
        else:
            text = 'form is invalid'
            return render(request, 'converter/home.html', {'form': form, 'text': text})
    else:
        form = UploadFileForm()
        return render(request, 'converter/home.html', {'form': form})
