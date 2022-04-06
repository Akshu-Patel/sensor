from sqlite3 import Date
from time import time
from urllib import request
from django.shortcuts import render,redirect
from rest_framework.response import Response 
from sensorapp.models import Device
from sensorapp.serializers import DeviceSerializer
from datetime import datetime
from .forms import DeviceForm
from rest_framework.decorators import api_view
from django.urls import reverse



# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    sensorapp_urls = {
        
        'Register':'/device-register/',
    }

@api_view(['POST'])
def deviceRegister(request):
    print('welcome',request.data)
    request.data['timestamp'] = datetime.now()
    serializer = DeviceSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()

    return Response(reverse(serializer.data))

@api_view(['GET'])
def SearchDevice(request):
    qs = Device.objects.all()
    sensor_type_query = request.GET.get("sensor_type")
    location_query = request.GET.get("location")
    # timestamp = datetime.strptime(timestamp, '%Y-%m-%d')
    starttimestamp_query = request.GET.get("starttimestamp")
    stoptimestamp_query = request.GET.get("stoptimestamp")
    # stopdate_query = request.GET.get("stopdate")
    # print('timestamp_query',startdate_query)
    # # date_unix = ''
    # if timestamp_query !='' and timestamp_query is not None:
    #     date = datetime.strptime(timestamp_query,"%Y-%m-%dT%H:%M")
    #     date_unix = int(date.timestamp())

    # datestop_unix = ''
    # if timestampstop_query !='' and timestampstop_query is not None:
    #     date = datetime.strptime(timestampstop_query,"%Y-%m-%dT%H:%M")
    #     datestop_unix = int(date.timestamp())
    
    # end_query = request.GET.get("timestamp")
    # start = request.GET.get('start', None)
    # end = request.GET.get('end', None)

    if sensor_type_query !='' and sensor_type_query is not None:
        qs = qs.filter(sensor_type=sensor_type_query)

    if location_query !='' and location_query is not None:
        qs = qs.filter(location=location_query)

    if starttimestamp_query !='' and stoptimestamp_query is not None:
        qs = qs.filter(timestamp__gte=starttimestamp_query, timestamp__lte=stoptimestamp_query)

    # elif stopdate_query !='' and stopdate_query is not None:
    #     qs = qs.filter(stopdate=stopdate_query)

    # elif end_query !='' and end_query is not None:
    #     qs = qs.filter(timestamp=end_query)

    # elif end !='' and end is not None:
    #      qs = qs.filter(todate=todate_query)

    context = {
        'object_list': qs
    }
    
    return render(request, "home.html", context)

def index(request):
    data = Device.objects.all()
    sensor_type_query = request.GET.get("sensor_type")
    value_query = request.GET.get("value")
    # timestamp_query = request.GET.get("timestamp")
    starttimestamp_query = request.GET.get("start_timestamp")
    stoptimestamp_query = request.GET.get("stop_timestamp")
    location_query = request.GET.get("location")
    if sensor_type_query !='' and sensor_type_query is not None:
        data = data.filter(sensor_type=sensor_type_query)

    if value_query !='' and value_query is not None:
        data = data.filter(value=value_query)

    # if timestamp_query !='' and timestamp_query is not None:
    #     data = data.filter(timestamp=timestamp_query)

    if starttimestamp_query !='' and stoptimestamp_query is not None:
        data = data.filter(timestamp__gte=starttimestamp_query, timestamp__lte=stoptimestamp_query)


    if location_query !='' and location_query is not None:
        data = data.filter(location=location_query)

    form = DeviceForm(request.GET)
    # if request.method == 'GET':
        # if form.is_valid():
        #     form.save()
        #     # return redirect('/')
        # else:
        #     form = DeviceForm()
    context={
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)

