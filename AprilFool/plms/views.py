from django.shortcuts import render

def plms(request):
    return render(request, 'PLMS/plms.html', {})
def Course(request):
    return render(request, 'PLMS/Course.html', {})
def CProgramming(request):
    return render(request, 'PLMS/CProgramming.html', {})
def Notice(request):
    return render(request, 'PLMS/Notice.html', {})
def Retest(request):
    return render(request, 'PLMS/Retest.html', {})
def TestList(request):
    return render(request, 'PLMS/TestList.html', {})
