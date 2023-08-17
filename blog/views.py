from django.shortcuts import render

# Create your views here.


def render_blog_homepage(request):
    user = request.user
    if user.is_anonymous:
        user_data = {"user_name": "anon", "full_name": "Anonymouse User"}
    elif user.is_authenticated:
        user_data = {
            "user_name": user.username,
            "full_name": user.first_name + " " + user.last_name,
        }
    else:
        pass
    return render(request, "blog/homepage.html", {"user_data": user_data})
