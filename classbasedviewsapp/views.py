from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class GetInput(View):
    def get(self,request):
        return render(request,"getinput.html")
class PostInput(View):
    def get(self,request):
        return render(request,"postinput.html")
class Add(View):
    def get(self,request):
        v1=request.GET["t1"]
        v2=request.GET["t2"]
        try:
            i=int(v1)
            j=int(v2)
            k=i+j
            con_dict={"result":k}
            return render(request,'display.html',con_dict)
        except(ValueError):
            return HttpResponse("invalid input")
    def post(self,request):
        v1=request.POST["t1"]
        v2=request.POST["t2"]
        try:
            i=int(v1)
            j=int(v2)
            k=i+j
            con_dict={"result":k}
            return render(request,'display.html',con_dict)
        except(ValueError):
            return HttpResponse("invalid input")
