from django.shortcuts import render, get_object_or_404,redirect
from.forms import Todoforms

# Create your views here.

from.models import Blog


def home(request):
    b=Blog.objects.all()
    return render(request,'index.html',{'b':b})

def addblog(request):
    if request.user.is_authenticated:
        bl = Blog.objects.filter(auth=request.user)
        if request.method=='POST':
            name=request.POST.get('name')
            desc= request.POST.get('desc')
            img=request.FILES['img']
            auth = request.POST.get('auth')
            date = request.POST.get('date')
            b=Blog(name=name,desc=desc,img=img,auth=auth,date=date)
            b.save()
            print("blog added")
        return render(request,'blog.html',{'bl':bl})
    else:
        return redirect('login')

def blogdetail(request,id):
    det=Blog.objects.get(id=id)
    return render(request, 'view.html',{'det': det})

# def myblog(request):
#
#         bl = Blog.objects.filter(auth=request.user)
#         return render(request,'myblog.html',{'bl':bl})


def update(request,id):
    blog=Blog.objects.get(id=id)
    form=Todoforms(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('addblog')
    return render(request,'update.html',{'blog':blog,'form':form})

def delete(request,id):
    de=Blog.objects.get(id=id)
    if request.method=="POST":
        de.delete()
        return redirect('addblog')
    return render(request,'delete.html',{'de':de})


