from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Show

def new_show(request):
    return render (request, "shows_app/newshow.html")

def shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, 'shows_app/shows.html', context)

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title = request.POST.get('title')
        network = request.POST.get('network')
        release_date = request.POST.get('release_date')
        desc = request.POST.get('desc')
        newShow = Show.objects.create(title=title, network=network, release_date=release_date, desc=desc)
        messages.success(request, "Show successfully added!")
        return redirect('/shows/' + str(newShow.id))

def show_info(request, id):
    show = Show.objects.get(id=int(id))
    context = {
        'show' : show,
    }
    return render(request, "shows_app/showinfo.html", context)

def edit_info (request, id):
    show = Show.objects.get(id=int(id))
    context = {
        'show' : show,
    }
    return render(request, "shows_app/edit.html", context)

def update_info(request, id):
    show = Show.objects.get(id=int(id))
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+ str(show.id) +'/edit')
    else:
        show.title = request.POST.get('title')
        show.network = request.POST.get('network')
        show.release_date = request.POST.get('release_date')
        show.desc = request.POST.get('desc')
        show.save()
        messages.success(request, "Show successfully updated")
        return redirect('/shows/' + str(show.id))

def destroy(request, id):
    Show.objects.get(id=int(id)).delete()
    return redirect('/shows')


