import sys
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.shortcuts import redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import datetime
from datetime import date, timedelta
from .models import Reservation, ReservationLog
from .forms import ReservationForm
# Create your views here.

date = datetime.date.today()
date = date.strftime('%Y-%m-%d')
def loginView(request):
    l = AuthenticationForm()
    today = datetime.date.today()
    today = today.strftime('%Y-%m-%d')
    if request.method == "POST":
        user = request.POST['username']
        passw = request.POST['password']
        user = authenticate(request, username=user, password=passw)
        if user is not None:
            login(request, user)
            print('logged in as ', user)
            return HttpResponseRedirect('/api/'+today+'/')
        else:
            msg = 'Access denied. Please enter valid access data'
            return render(request, 'account/login.html', {'form': l, 'msg': msg})
    return render(request, 'account/login.html', {'form': l})

def logout_view(request):
    user = request.user
    logout(request)
    print(user, ' logged out')
    return HttpResponseRedirect('/api/login')


@login_required
def list(request, date=date):
    seats = {0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30}
    f = ReservationForm()
    r = reserve(request, date)
    coming_days = []
    for x in range(15):
        day = datetime.date.today() + timedelta(days=x)
        coming_days.append(day)
    current_date = datetime.datetime.strptime(date, '%Y-%m-%d')
    reservs = Reservation.objects.filter(date__exact=date)
    logs = ReservationLog.objects.all()
    #request.reply_channel.send({'form': f, 'reservs': reservs, 'seats': seats, 'current_date': current_date, 'coming_days': coming_days, 'logs': logs, 'MAX_HOUR': settings.MAX_HOUR, 'MIN_STEPS': settings.MIN_STEPS, 'MAX_RES_TIME': settings.MAX_RES_TIME, 'DEF_RES_TIME': settings.DEF_RES_TIME})
    return render(request, 'reservation/list.html', {'form': f, 'reservs': reservs, 'seats': seats, 'current_date': current_date, 'coming_days': coming_days, 'logs': logs, 'MAX_HOUR': settings.MAX_HOUR, 'MIN_STEPS': settings.MIN_STEPS, 'MAX_RES_TIME': settings.MAX_RES_TIME, 'DEF_RES_TIME': settings.DEF_RES_TIME})

def remove(request, id=1):
    res = Reservation.objects.get(pk=id)
    res_log = ReservationLog.objects.filter(res_id=id)
    res.delete()
    res_log.delete()
    today = datetime.date.today()
    today = today.strftime('%Y-%m-%d')
    return redirect('/api/'+today, {'res': res})

def reserve(request, date):
    if request.method == "POST":
        f = ReservationForm(request.POST)
        print(request.POST.get('note'))
        print(request.POST.get('secret'))
        print(request.POST.get('x'))
        print(request.POST.get('y'))
        if request.POST.get('id'):
            res = Reservation.objects.get(pk=request.POST.get('id'))
            f = ReservationForm(request.POST, instance=res)
            creator = res.creator
        else:
            f = ReservationForm(request.POST)
            print('will try and add new reservation and create id')
            creator = User.objects.get(pk=request.POST.get('creator'))
        if f.is_valid():
            print('form is valid')
            res = f.save(commit=False)
            #res.created_at = timezone.now()
            res.date = date
            res.creator = creator
            a = 1
            range_steps = settings.MAX_HOUR/settings.MIN_STEPS+1
            for x in [x * settings.MIN_STEPS for x in range(0, int(range_steps))]:
                if x < res.x:
                    a = x
            b = a + settings.MIN_STEPS
            if b-res.x > res.x-a:
                res.x = a
            else:
                res.x = b
            for y in [y * settings.MIN_STEPS for y in range(0, int(range_steps))]:
                if y < res.y:
                    a = y
            b = a + settings.MIN_STEPS
            if b-res.y > res.y-a:
                res.y = a
            else:
                res.y = b


            if res.y > settings.MAX_HOUR:
                res.y = settings.HOUR
            print(res.note)
            print(res.secret)
            print(res.x)
            print(res.y)
            res.save()
            if request.POST.get('id'):
                res_created = Reservation.objects.get(pk=request.POST.get('id'))
            else:
                res_created = Reservation.objects.latest('id')
            writeResLog(request, res_created)
    return True

def writeResLog(request, res_created):
    res_log = ReservationLog()
    res_log.res_id = res_created.id
    res_log.created_at = timezone.now()
    res_log.creation_date = res_created.created_at
    res_log.res_creator = res_created.creator
    res_log.updated_by = request.user
    res_log.seat = res_created.seat
    res_log.secret = res_created.secret
    res_log.x = res_created.x
    res_log.y = res_created.y
    res_log.note = res_created.note
    res_log.date = res_created.date
    res_log.save()
    return True

#
# def seat(request):
#     x=1
#     for x in range(31):
#         seat = Seat(number=x, guest_id="", note="")
#         seat.save()
#     return True
