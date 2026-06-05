from django.shortcuts import render, HttpResponse

def testPage(request):
    return HttpResponse("Working as intended!")


# Create your views here.
