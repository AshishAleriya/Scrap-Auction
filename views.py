from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

from mysite import models as mysite_models
from . import models

# Create your views here.
def adminhome(request):
    return render(request,"adminhome.html")

def manageusers(request):
    userDetails=mysite_models.Register.objects.filter(role="user")
    return render(request,"manageusers.html",{"userDetails":userDetails}) 

def manageuserstatus(request):
    s=request.GET.get("s")
    regid=int(request.GET.get("regid"))
    if s=="block":
        mysite_models.Register.objects.filter(regid=regid).update(status=0)
    elif s=="verify":
        mysite_models.Register.objects.filter(regid=regid).update(status=1)
    else:
        mysite_models.Register.objects.filter(regid=regid).delete() 
    return redirect("/myadmin/manageusers/")
def addcategory(request):
  if request.method=="GET":
    return render(request,"addcategory.html",{"output":""})
  else:
    catname=request.POST.get("catname")
    caticon=request.FILES["caticon"]
    fs = FileSystemStorage()
    filename = fs.save(caticon.name,caticon)
    p=models.Category(catname=catname,caticon=filename)
    p.save()
def addsubcategory(request):
  clist=models.Category.objects.filter()
  if request.method=="GET":
    return render(request,"addsubcategory.html",{"output":"","clist":clist})
  else:
    catname=request.POST.get("catname")
    subcatname=request.POST.get("subcatname")

    caticon=request.FILES["caticon"]
    fs = FileSystemStorage()
    filename = fs.save(caticon.name,caticon)
    p=models.SubCategory(catname=catname,subcatname=subcatname,subcaticon=filename)
    p.save()               
    return render(request,"addsubcategory.html",{"output":"SubCategory Added Successfully....","clist":"clist"})
