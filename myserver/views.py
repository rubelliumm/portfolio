import threading
from django.http import HttpResponse
from django.shortcuts import redirect
# # from myserver.server import server as s


def server_home(request):
    return HttpResponse('server off')
#     # thread = threading.Thread(target=s(), daemon=True)
#     # thread.start()
#     # return HttpResponse('server started??')
