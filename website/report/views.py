from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from report.models import Event, Block, District, HealthCenter
from report.forms import DistrictForm, BlockForm, HealthCenterForm, EventForm
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from report.create_excel import ExcelResponse

try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps


uttar_pradesh_lat = "26.79644"
uttar_pradesh_lng = "82.198639"
map_zoom_level = 7

@login_required
def index(request):
    events = Event.objects.all()
    return render_to_response('report/index.html', {'events' : events, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY},context_instance=RequestContext(request))

@login_required
def add_district(request):
    if request.POST:
        f = DistrictForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/add_district_done.html',)
    else:
         f = DistrictForm()   
    return render_to_response('report/add_district.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY},context_instance=RequestContext(request))

@login_required
def add_block(request):
    if request.POST:
        f = BlockForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/add_block_done.html',)
    else:
         f = BlockForm()   
    return render_to_response('report/add_block.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY},context_instance=RequestContext(request))

@login_required
def add_health_center(request):
    if request.POST:
        f = HealthCenterForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/add_health_center_done.html',)
    else:
         f = HealthCenterForm()   
    return render_to_response('report/add_health_center.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY},context_instance=RequestContext(request))

@login_required
def add_event(request):
    if request.POST:
        f = EventForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/add_event_done.html',)
    else:
         f = EventForm()   
    return render_to_response('report/add_event.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY},context_instance=RequestContext(request))

@login_required
def feeds_block_list(request, district_name):
    block_list = Block.objects.all().filter(district=get_object_or_404(District, name=district_name)).order_by("id")
    return render_to_response('feeds/blocks.txt', {'block_list':block_list, }, mimetype="text/plain")

@login_required
def feeds_district_center(request, district_name):
    district = get_object_or_404(District, name=district_name)
    return HttpResponse(district.center)

@login_required
def feeds_block_center(request, block_name):
    block = get_object_or_404(Block, name=block_name)
    return HttpResponse(block.center)

@login_required
def feeds_health_center_position(request, health_center_name):
    hc = get_object_or_404(HealthCenter, name=health_center_name)
    return HttpResponse(hc.center)


def confirm_required(template_name, context_creator, key='__confirm__'):
    def decorator(func):
        def inner(request, *args, **kwargs):
            if request.POST.has_key(key):
                return func(request, *args, **kwargs)
            else:
                context = context_creator and context_creator(request, *args, **kwargs) \
                    or RequestContext(request)
                return render_to_response(template_name, context)
        return wraps(func)(inner)
    return decorator

@login_required
def district_list_edit(request):
    d_list = District.objects.all().order_by('name')
    return render_to_response("report/district_list_edit.html", {"districts":d_list})

@login_required
def edit_district(request, district_name):
    if request.POST:
        f = DistrictForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/edit_district_done.html',)
    else:
         f = DistrictForm(instance = get_object_or_404(District, name=district_name))   
    return render_to_response('report/edit_district.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY},context_instance=RequestContext(request))


@login_required
def delete_district_context(request, district_name):
    d = get_object_or_404(District, name=district_name)
    return RequestContext(request, {'district': d})

@confirm_required('report/delete_district_confirm.html', delete_district_context)
@login_required
def delete_district(request, district_name):
    d = get_object_or_404(District, name=district_name)
    d.delete()
    next_url = request.GET.get('next', '/edit/district/')
    return HttpResponseRedirect(next_url)


@login_required
def block_list_edit(request):
    b_list = Block.objects.all().order_by('name')
    return render_to_response("report/block_list_edit.html", {"blocks":b_list})

@login_required
def edit_block(request, block_name):
    if request.POST:
        f = BlockForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/edit_block_done.html',)
    else:
         f = BlockForm(instance = get_object_or_404(Block, name=block_name))   
    return render_to_response('report/edit_block.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY},context_instance=RequestContext(request))

@login_required
def delete_block_context(request, block_name):
    b = get_object_or_404(Block, name=block_name)
    return RequestContext(request, {'block': b})

@confirm_required('report/delete_block_confirm.html', delete_block_context)
@login_required
def delete_block(request, block_name):
    d = get_object_or_404(Block, name=block_name)
    d.delete()
    next_url = request.GET.get('next', '/edit/block/')
    return HttpResponseRedirect(next_url)

@login_required
def health_center_list_edit(request):
    hc_list = HealthCenter.objects.all().order_by('name')
    return render_to_response("report/health_center_list_edit.html", {"health_centers":hc_list})

@login_required
def edit_health_center(request, health_center_name):
    if request.POST:
        f = HealthCenterForm(request.POST)
        if f.is_valid():
            f.save()
            return render_to_response('report/edit_health_center_done.html',)
    else:
         f = HealthCenterForm(instance = get_object_or_404(HealthCenter, name=health_center_name))   
    return render_to_response('report/edit_health_center.html', {"form":f, "center_lat":uttar_pradesh_lat, "center_lng":uttar_pradesh_lng, "zoom_level":map_zoom_level, "map_api_key":settings.MAPS_API_KEY},context_instance=RequestContext(request))

@login_required
def delete_health_center_context(request, health_center_name):
    hc = get_object_or_404(HealthCenter, name=health_center_name)
    return RequestContext(request, {'health_center': hc})

@confirm_required('report/delete_health_center_confirm.html', delete_health_center_context)
@login_required
def delete_health_center(request, health_center_name):
    d = get_object_or_404(HealthCenter, name=health_center_name)
    d.delete()
    next_url = request.GET.get('next', '/edit/health-center/')
    return HttpResponseRedirect(next_url)

def excelview(request):
    objs = Event.objects.all()
    data_list = [
        ["Date","Time", "Health Center", "Block", "District", "Category", "Amount"],
        ]

    for o in objs:
        data_list.append(
            [o.reporting_date,o.reporting_time, o.target_health_center.name, o.block.name, o.district.name, o.category, o.money]
            )

    return ExcelResponse(data_list)

