from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from .models import Table, Vote, Taste
from datetime import datetime
from django.utils import timezone
import os
import time
# import paho.mqtt.client as paho


def index(request):
    # t1 = Vote.objects.all()
    # print("The value for 't1' is... ")
    # res = t1.latest('id')
    # res = res.vote_value
    # print(res)

    # page = render(request, 'taste/index.html')
    # page['cola'] = str(res)
    return render(request, 'taste/index.html')


def votes(request, table_id):
    table = get_object_or_404(Table, pk=table_id)
    if request.method == 'POST':
        value = request.POST['value']
        cmd = request.POST['taste']
        print("success " + cmd)
        vote = Vote(
            vote_value=value,
            current_value=5,
            table=table,
            voted_at=timezone.now(),
            taste=get_object_or_404(Taste, taste_name=cmd)
        )
        vote.save()
        
    return render(request, 'taste/votes.html', {'table' : table})