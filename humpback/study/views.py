from django.shortcuts import render

# Create your views here.


def studylist(request):
    return render(request, 'study/studylist.html')


def studyuploadform(request):
    return render(request, 'study/upload.html')
