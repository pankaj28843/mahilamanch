from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from report.models import Event, Block, District, HealthCenter
from report.forms import DistrictForm, BlockForm, HealthCenterForm, EventForm
from django.conf import settings

uttar_pradesh_lat = "26.79644"
uttar_pradesh_lng = "82.198639"
map_zoom_level = 7
def index(request):
    events = Event.objects.all()
    return render_to_response('report/index.html', {'events' : events, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY})

def add_district(request):
    if request.POST:
        f = DistrictForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/add_district_done.html',)
    else:
         f = DistrictForm()   
    return render_to_response('report/add_district.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY})

def add_block(request):
    if request.POST:
        f = BlockForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/add_block_done.html',)
    else:
         f = BlockForm()   
    return render_to_response('report/add_block.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY})


def add_health_center(request):
    if request.POST:
        f = HealthCenterForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/add_health_center_done.html',)
    else:
         f = HealthCenterForm()   
    return render_to_response('report/add_health_center.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY})

def add_event(request):
    if request.POST:
        f = EventForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/add_event_done.html',)
    else:
         f = EventForm()   
    return render_to_response('report/add_event.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY})

def feeds_block_list(request, district_name):
    block_list = Block.objects.all().filter(district=get_object_or_404(District, name=district_name)).order_by("id")
    return render_to_response('feeds/blocks.txt', {'block_list':block_list, }, mimetype="text/plain")

def feeds_district_center(request, district_name):
    district = get_object_or_404(District, name=district_name)
    return HttpResponse(district.center)

def feeds_block_center(request, block_name):
    block = get_object_or_404(Block, name=block_name)
    return HttpResponse(block.center)

def feeds_health_center_position(request, health_center_name):
    hc = get_object_or_404(HealthCenter, name=health_center_name)
    return HttpResponse(hc.center)
    
