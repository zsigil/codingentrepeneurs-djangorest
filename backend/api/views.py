# from django.shortcuts import render
import json
from django.http import JsonResponse
# Create your views here.


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body - byte string of json data
    print(request.GET)
    body = request.body
    # print(body)
    # print(request.headers)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    return JsonResponse(data)
