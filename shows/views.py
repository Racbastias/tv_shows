from django.shortcuts import render, HttpResponse, redirect
from shows.models import Tv, Shows
from django.contrib import messages
from django.db import IntegrityError

def index(request):
    return redirect('/shows')

def network(request):
    channel = Tv.objects.all()
    show = Shows.objects.all()
    context = {
        "channel": channel,
        "show": show
    }
    return render(request, 'channels.html', context)

def tvinfo(request, id):
    selectedchannel = Tv.objects.get(id=id)
    show = Shows.objects.all()
    context = {
        "show": show,
        "selectedchannel": selectedchannel
    }
    return render(request, 'channel.html', context)

def shows(request): # Ok
    channel = Tv.objects.all()
    show = Shows.objects.all()
    context = {
        "channel": channel,
        "show": show
    }
    return render(request, 'shows.html', context)

def new(request): # Ok
    channel = Tv.objects.all()
    show = Shows.objects.all()
    context = {
        "channel": channel,
        "show": show
    }
    return render(request, 'create.html', context)

def create(request): # Ok
    errors = Shows.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'../shows/new')
        
    else:
        
        showtitle = request.POST['title']
        idnetwork = int(request.POST['network'])
        release_date = request.POST['release_date']
        desc = request.POST['desc']
        
        try:
            thisshow = Shows.objects.create(title=showtitle, release_date=release_date, network_id=idnetwork, desc=desc)
        
        except IntegrityError:
            messages.error(request,"This shows already exist")
            return redirect (f'../shows/new')
        
        messages.success(request, f'Your show {showtitle} has been created')
        return redirect(f'/shows/{thisshow.id}')
    

def id(request, id):
    selectedshow = Shows.objects.get(id=id)
    channel = Tv.objects.all()
    show = Shows.objects.all()
    context = {
        "channel": channel,
        "show": show,
        "selectedshow": selectedshow
    }
    return render(request, 'tv_show.html', context)

def edit(request, id):
    selectedshow = Shows.objects.get(id=id)
    channel = Tv.objects.all()
    release_date = selectedshow.release_date.strftime('%Y-%m-%d')
    context = {
        "selectedshow": selectedshow,
        "channel": channel,
        "release_date": release_date
    }
    return render(request, 'edit.html', context)

def update(request, id):
    selectedshow = Shows.objects.get(id=id)
    errors = Shows.objects.basic_validator(request.POST)
    channel = Tv.objects.all()
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'../{selectedshow.id}/edit')
    else:
        showtitle = request.POST['title']
        idnetwork = int(request.POST['network'])
        date = request.POST['date'].strftime('%Y-%m-%d')
        desc = request.POST['desc']
        
        selectedshow.title = showtitle
        selectedshow.network_id = idnetwork
        selectedshow.release_date = date
        selectedshow.desc = desc
        selectedshow.save()
        messages.info(request, f'Your show {showtitle} has been updated')
        return redirect(f'../{selectedshow.id}')

def destroy(request, id):
    selectedshow = Shows.objects.get(id=id)
    temp = selectedshow.title
    context = {
        "temp": temp
    }
    messages.error(request, f'Your show {temp} has been deleted')
    
    selectedshow.delete()
    return redirect("/shows", context)
    