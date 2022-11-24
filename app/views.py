from django.shortcuts import render

# Create your views here.
def ifelse(request):
    d={'a':100,'b':2000}
    return render(request,'ifelse.html',d)
