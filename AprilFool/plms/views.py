from django.shortcuts import render

def plms(request):
    return render(request, 'PLMS/plms.html', {})

def Course(request):
    return redner(request, 'PLMS/Course.html', {})
