from django.shortcuts import render

# Create your views here.
def csk(request):
    d={'captian':'DHONI'}
    return render(request,'csk.html',context=d)