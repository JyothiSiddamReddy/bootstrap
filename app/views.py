from django.shortcuts import render

# Create your views here.
def bootstrapdown(request):
    return render(request,'bootstrap.down.html')