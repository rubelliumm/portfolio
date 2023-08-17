from django.http import JsonResponse
from django.shortcuts import render
from customAdmin.forms import createCircularForm


def admin_home(request):
    return render(request, "custom-admin/admin_home.html")


def create_circular(request):
    if request.method == "POST":
        form = createCircularForm(request.POST)
        if form.is_valid():
            print(form.data.get("images"))
            form.save()
            return JsonResponse(
                {
                    "statuscode": 2,
                }
            )
        else:
            return render(request, "custom-admin/create-circular.html", {"form": form})
    else:
        form = createCircularForm()
        return render(request, "custom-admin/create-circular.html", {"form": form})
