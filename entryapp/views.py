from django.shortcuts import render
from django.core.mail import send_mail

from entryapp.forms import CheckInForm, HostForm, CheckOutForm
from entryapp.models import Host, Visitor, PastVisitor
from entryapp.methods import send_message

import os

# Create your views here.

def home(request):
    form = CheckInForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            try:
                host = Host.objects.all().first()
                visitor = form.save()
                message = ('Name : ' + visitor.name +
                        '\nEmail : ' + visitor.email +
                        '\nPhone : ' + visitor.phone_number.as_e164 +
                        '\nCheck In : ' + visitor.check_in.strftime("%H:%M %p"))
                send_mail(
                        subject='New Visitor Check In',
                        message=message,
                        from_email=os.environ.get('EMAIL_HOST_USER', ''),
                        recipient_list=[host.email],
                        fail_silently=False,
                )
                send_message(host.phone_number.as_e164, message)
                return render(request, 'entryapp/showinfo.html',
                                    {'info': "Successfuly Check In!"})
            except Exception as err:
                print(err)
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

def checkout(request):
    form = CheckOutForm(request.POST or None)
    if(request.method == 'POST'):
        if form.is_valid():
            try:
                host = Host.objects.all().first()
                visitor = Visitor.objects.get(phone_number = form.cleaned_data['phone'])
                visitor.delete()
                visitor = PastVisitor.objects.get(phone_number = form.cleaned_data['phone'],
                                check_in = visitor.check_in)
                message = ('Name : ' + visitor.name +
                        '\nEmail : ' + visitor.email +
                        '\nPhone : ' + visitor.phone_number.as_e164 +
                        '\nCheck In : ' + visitor.check_in.strftime("%H:%M %p") +
                        '\nCheck Out : ' + visitor.check_out.strftime("%H:%M %p") +
                        '\nHost Name : ' + host.name +
                        '\nAddress Visited : ' + os.environ.get('ADDRESS', ''))
                send_mail(
                        subject='Visitor Check Out',
                        message=message,
                        from_email=os.environ.get('EMAIL_HOST_USER', ''),
                        recipient_list=[host.email],
                        fail_silently=False,
                )
                send_message(host.phone_number.as_e164, message)
                return render(request, 'entryapp/showinfo.html',
                                    {'info': "Successfuly Check Out!"})
            except Exception as err:
                print(err)
                return render(request, 'entryapp/showinfo.html',
                                    {'error': "First Check In"})
    return render(request, 'entryapp/checkout.html', {'form': form})
