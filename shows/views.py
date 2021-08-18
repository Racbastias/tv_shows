from django.shortcuts import render, HttpResponse, redirect
from shows.models import Tv, Shows
from django.contrib import messages

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
    showtitle = request.POST['title']
    idnetwork = int(request.POST['network'])
    date = request.POST['date']
    desc = request.POST['desc']
    
    #network = Tv.objects.get(id=int(idnetwork))
    thisshow = Shows.objects.create(title=showtitle, release_date=date, network_id=idnetwork, desc=desc)
    
    messages.success(request, f'Your show {showtitle} has been created')
    return redirect("/shows")

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
    context = {
        "selectedshow": selectedshow,
        "channel": channel
    }
    return render(request, 'edit.html', context)

def update(request, id):
    selectedshow = Shows.objects.get(id=id)
    channel = Tv.objects.all()
    showtitle = request.POST['title']
    idnetwork = int(request.POST['network'])
    date = request.POST['date']
    desc = request.POST['desc']
    
    selectedshow.title = showtitle
    selectedshow.network_id = idnetwork
    selectedshow.release_date = date
    selectedshow.desc = desc
    selectedshow.save()
    
    messages.warning(request, f'Your show {showtitle} has been updated')
    return redirect("/shows")

def destroy(request, id):
    selectedshow = Shows.objects.get(id=id)
    temp = selectedshow.title
    context = {
        "temp": temp
    }
    messages.error(request, f'Your show {temp} has been deleted')
    
    selectedshow.delete()
    return redirect("/shows", context)
    