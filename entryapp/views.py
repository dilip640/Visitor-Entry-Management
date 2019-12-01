from django.shortcuts import render

from entryapp.forms import CheckInForm, HostForm
from entryapp.models import Host

# Create your views here.

def home(request):
    form = CheckInForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            host = Host.objects.all()
            if host.count():
                form.save()
                return render(request, 'entryapp/showinfo.html',
                                    {'info': "Successfuly CheckIn!"})
            else:
                return render(request, 'entryapp/showinfo.html',
                                    {'error': "Please register Host first!"})
    return render(request, 'entryapp/index.html', {'form': form})

def host(request):
    try:
        host = Host.objects.all().first()
        form = HostForm(request.POST or None, instance=host)
    except:
        form = HostForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            form.save()
            return render(request, 'entryapp/showinfo.html',
                                    {'info': "Host Successfuly Updated!"})
    return render(request, 'entryapp/host.html', {'form': form})
