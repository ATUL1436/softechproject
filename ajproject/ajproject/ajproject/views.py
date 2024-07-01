from django.http import HttpResponse
import datetime

from django.shortcuts import render


def home(request):
    isActive=True
    if request.method=="POST":
        check=request.POST.get("check")
        print(check)
        if check is None:isActive=False
        else: isActive=True
    
    date=datetime.datetime.now()
    name="sbs"
    list_of_programs=["wap to check even or odd",
                      "wap to check prime number",
                      "wap to print all prime numbers from 1 to 100",
                      "wap to print pascals triangle"]
    student={"student_name":"atul",
             "student_collage":"xyz",
             "student_city":"latur"}
    data={"date":date,
          "isActive":isActive,
          "name":name,
          "list_of_programs":list_of_programs,
          "student_data":student}
    #return HttpResponse("<h1>Hello this is index page</h1>"+(str(date)))
    return render(request,"home.html",data)

def about(request):
    #return HttpResponse("<h1>this is about page</h1>")
    return render(request,"about.html",{})

def servises(request):
    #return HttpResponse("<h1>this is servises page</h1>")
    return render(request,"servises.html",{})