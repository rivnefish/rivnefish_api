# -*- coding: utf-8 -*-
import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Markers


def conv(lst):
        for k, v in lst:
            if len(v) == 1:
                yield k, v[0]
            else:
                yield k, v


@csrf_exempt
def fish_map_markers(request):
    if not request.method == 'GET':
        return HttpResponse('{"error": "Not allowed!"}')
    result = []
    print request.method
    for model in Markers.objects.all():
        model = model_to_dict(model, fields=['address', 'lat', 'lng',
                                             'marker_id', 'name'])
        for key in model.iterkeys():
            model[key] = '%s' % model[key]
        result.append(model)
    return HttpResponse(json.dumps(result), content_type="application/json")


@csrf_exempt
def fish_marker(request, marker_id):
    if not request.method == 'GET':
        return HttpResponse('{"error": "denied"}')
    marker = model_to_dict(Markers.objects.get(marker_id=marker_id))
    for key in marker.iterkeys():
        marker[key] = '%s' % marker[key]
    return HttpResponse(json.dumps(marker), content_type="application/json")


@csrf_exempt
def add_lake(request):
    # Here new lake
    if request.method == 'POST':
        data = {item[0]: item[1] for item in conv(request.POST.lists())}
        return HttpResponse(json.dumps(data))
    elif request.method == 'GET':
        data = {item[0]: item[1] for item in conv(request.GET.lists())}
        return HttpResponse(json.dumps(data))
    else:
        return HttpResponse('{"error": "Not allowed!"}')


@csrf_exempt
def search_by_filters(request):
    result = None
    if request.method == 'POST':
        data = {item[0]: item[1] for item in conv(request.POST.lists())}
    elif request.method == 'GET':
        data = {item[0]: item[1] for item in conv(request.GET.lists())}
    else:
        return HttpResponse('{"error": "Not allowed!"}')

    result = Markers.objects.all()
    if 'name' in data and data['name']:
        result = result.filter(name__icontains=data['name'])
    if 'permit' in data and data['permit']:
        if data['permit'] in ['free', 'paid']:
            result = result.filter(permit__icontains=data['permit'])
            #==================================================================
            # if data['permit'] == 'paid':
            #     if 'price' in data:
            #         result = result.filter(permit__lt=data['price'])
            #==================================================================
    if 'boat' in data and data['boat']:
        result = result.filter(boat_usage=data['boat'])
    if 'at_night' in data:
        pass
    if 'distance' in data and data['distance']:
        result = result.filter(distance_to_rivne__lt=data['distance'])
    if 'fishes' in data:
        result = result.filter(distance_to_rivne__lt=data['distance'])
    if 'fish_weight' in data:
        pass
    return HttpResponse(result)
