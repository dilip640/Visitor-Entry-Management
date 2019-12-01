from django.shortcuts import render

from entryapp.forms import CheckInForm
from entryapp.models import Host

# Create your views here.

def home(request):
    form = CheckInForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            host = Host.objects.all()
            if host.count():
                form.save()
            else:
                return render(request, 'entryapp/showinfo.html',
                                    {'error': "Please register Host first!"})
    return render(request, 'entryapp/index.html', {'form': form})
