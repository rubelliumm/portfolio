from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from jobapp.models import Circular, circularImage, savedCircular
from django.contrib.auth.decorators import login_required


def getUserData(request):
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
    return user_data


def renderJobappHomePage(request):
    top_3_circular = Circular.objects.filter(is_featured=True)
    recently_published_circular = Circular.objects.order_by("-application_published_on")

    user_data = getUserData(request)
    return render(
        request,
        "jobapp/jobapp_home.html",
        {
            "user_data": user_data,
            "top_3_circular": top_3_circular,
            "recently_published_circular": recently_published_circular,
        },
    )


def renderAllCircularPage(request):
    user = request.user
    user_data = getUserData(request)
    try:
        all_circular = Circular.objects.all()
        saved_list = savedCircular.objects.get(user=user)
        for c in all_circular:
            if saved_list.circular.contains(c):
                c.is_saved = True
                c.save()
            else:
                c.is_saved = False
    except Circular.DoesNotExist:
        # message: circular doesnt exists.
        return
    except savedCircular.DoesNotExist:
        saved_list = savedCircular(user=user)
        saved_list.save()
        for c in all_circular:
            if saved_list.circular.contains(c):
                c.is_saved = True
                c.save()
            else:
                c.is_saved = False
    except TypeError:
        print("typer error")
    if user.is_anonymous:
        for c in all_circular:
            c.is_saved = False
            c.save()
    return render(
        request,
        "jobapp/allcircular.html",
        {"circulars": all_circular, "user_data": user_data},
    )


def renderCircularDetailsPage(request, cid):
    user = request.user

    user_data = getUserData(request)
    circular = get_object_or_404(Circular, pk=cid)
    images = circularImage.objects.filter(circular=circular)
    return render(
        request,
        "jobapp/circular_details.html",
        {"circular": circular, "user_data": user_data, "images": images},
    )


def saveCircular(request, cid):
    # first check if there is a savedcart or not
    user = request.user
    if user.is_authenticated:
        try:
            circular = Circular.objects.get(pk=cid)

            if (
                len(savedCircular.objects.filter(user=user)) == 0
            ):  # no savedcircular instance for user
                saved_list = savedCircular(user=user)
                saved_list.save()
                saved_list.circular.add(circular)
                saved_list.save()
                circular.is_saved = True
                circular.save()
                return JsonResponse({"statusCode": 1, "statusText": "Saved!"})
            elif len(savedCircular.objects.filter(user=user)) == 1:
                saved_list = savedCircular.objects.get(user=user)
                saved_list.save()
                if not saved_list.circular.contains(circular):
                    saved_list.circular.add(circular)
                    saved_list.save()
                    circular.is_saved = True
                    circular.save()
                    return JsonResponse({"statusCode": 1, "statusText": "Updated!"})
                else:
                    return JsonResponse(
                        {"statusCode": 0, "statusText": "Circular already saved!"}
                    )
            else:
                # more than one savedcircular cart with same user.
                return JsonResponse({"statusCode": 0, "statusText": "Fatal!"})
        except Circular.DoesNotExist:
            return JsonResponse(
                {"statusCode": 0, "statusText": "Circular doesn't exists!"}
            )
    else:
        # user needs to be authenticated to save circular
        return JsonResponse(
            {
                "statusCode": 0,
                "statusText": "user must be authenticated to save circular",
            }
        )


def unSaveCircular(request, cid):
    user = request.user
    if user.is_authenticated:
        try:
            circular = Circular.objects.get(pk=cid)
            if circular.is_saved:
                saved_list = savedCircular.objects.get(user=user)
                if saved_list.circular.contains(circular):
                    saved_list.circular.remove(circular)
                    saved_list.save()
                    circular.is_saved = False
                    circular.save()
                    return JsonResponse(
                        {
                            "statusCode": 10,
                            "statusText": "Circular unsaved successfully",
                        }
                    )
            else:
                return JsonResponse(
                    {
                        "statusCode": 0,
                        "statusText": "Circular isn't saved!",
                    }
                )
        except Circular.DoesNotExist:
            return JsonResponse(
                {
                    "statusCode": 0,
                    "statusText": "Circular doesn't exists",
                }
            )
    else:
        return JsonResponse(
            {
                "statusCode": 0,
                "statusText": "User must be authenticated",
            }
        )


def isCircularSaved(request, cid):
    user = request.user
    if user.is_authenticated:
        try:
            saved_list = savedCircular.objects.get(user=user)
            circular = Circular.objects.get(pk=cid)
            if saved_list.circular.contains(circular):
                return JsonResponse({"statusCode": 1, "statusText": "Saved"})
            else:
                return JsonResponse({"statusCode": 0, "statusText": "Failed!"})
        except savedCircular.DoesNotExist:
            return JsonResponse(
                {"statusCode": 0, "statusText": "User doesn't have a saveCircualr cart"}
            )
        except Circular.DoesNotExist:
            return JsonResponse(
                {"statusCode": 0, "statusText": "Circular not found in the Database"}
            )
    else:
        return JsonResponse(
            {
                "statusCode": 0,
                "statusText": "user must be authenticated to save circular",
            }
        )


@login_required
def viewSavedCircular(request):
    user = request.user
    if user.is_authenticated:
        try:
            saved_list = savedCircular.objects.get(user=user).circular.get_queryset()
            user_data = getUserData(request)
            return render(
                request,
                "jobapp/saved_circular.html",
                {"user_data": user_data, "saved_list": saved_list},
            )
        except savedCircular.DoesNotExist:
            # send message: no saved list.returning to all circular.
            return redirect("jobapp:all_circular_page_url")
        except savedCircular.MultipleObjectsReturned:
            # message: multiple save list available, delete them, or notify your admin.
            return redirect("jobapp:all_circular_page_url")
    else:
        # send message: user must be authenticated to see saved circular. returnign to signin pagee.
        return redirect("main:login_page_url")


def renderTopicsPage(request):
    return render(request, "jobapp/topics.html")


def renderExamQuestions(request):
    user = request.user
