from django.shortcuts import render,get_object_or_404
from testapp.models import goods,cart
from testapp.forms import goods_modelform,signup_modelform
from django.http import  FileResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template import loader
from django.http import HttpResponse
def home(r):
    print("trying to store some data using session...")
    r.session["test"]="hellothis is for testing"
    print(10/0)
    print(r.user.id)
    e=goods.objects.all()
    return render(r,"home.html",{"goods":e})
def add_goods(r):
    if(r.method=="POST"):
        f=goods_modelform(r.POST,r.FILES)
        if(f.is_valid()):
            f.save()
            print("form save succesfully")
            return render(r,"home.html",{"goods":goods.objects.all()})
        else:
            return render(r,"add_goods.html",{"form":f})
    else:
        return render(r,"add_goods.html",{"form":goods_modelform()})
def view_img(r,id):
    e=get_object_or_404(goods,id=id)
    return FileResponse(e.gming)
def signup(r):
    if(r.method=="POST"):
        f=signup_modelform(r.POST)
        if(f.is_valid()):
            k=f.save()
            k.set_password(k.password)
            k.save()
            return render(r,"thankyou.html")
        else:
            return render(r,"signup.html",{"form":f})
    else:
        return render(r,"signup.html",{"form":signup_modelform()})
@login_required
def add_to_cart(r,id):
    print("----",r.session.get("test"))
    print(r.user,type(r.user))
    print(r.user._wrapped,type(r.user._wrapped))
    print(r.user._wrapped.__dict__)

    if(r.method=="POST" or r.method=="GET"):

        e=get_object_or_404(goods,id=id)
        if(int(e.gquantity)>0):
            e1=cart(gname=e.gname,gquantity=1,gprice=e.gprice,user_id=User.objects.get(id=r.user.id))
            e1.save()


            e.gquantity-=1
            e.save()
            e2=cart.objects.filter(user_id=r.user.id)
            print(e2)
            return render(r,"my_account.html",{"goods":goods.objects.all(),"cart_items":e2,"flag":True})
        else:
            return render(r,"my_account.html",{"goods":goods.objects.all(),"cart_items":cart.objects.filter(user_id=r.user.id),"flag":False})
    else:
        print("hellll")
        return render(r,"my_account.html",{"cart_items":cart.objects.filter(user_id=r.user.id),"flag":False})
def logout(r):
    return render(r,"logout.html")
@login_required
def billingview(r):
        e=cart.objects.filter(user_id=r.user.id)
        sum=0
        for x in e:
            sum=sum+x.gprice
        return render(r,"confirmation.html",{"cart_items":e,"total_sum":sum,"email":r.user._wrapped.email})
@login_required
def placeorder(r):
    e=cart.objects.filter(user_id=r.user.id)
    sum=0
    for x in e:
        sum=sum+x.gprice
    h=loader.render_to_string("placeorder.html",{"cart_items":e,"user_name":str(r.user),"total_sum":sum})
    print(h)
    send_mail("Order Invoice","Thankyou for placing order with E-commerce","python4048@gmail.com",[r.user._wrapped.email],html_message=h)
    print("mail sent succesfully")
    e.delete()
    print("cart cleared successfully")
    return HttpResponse("<h1 color='green' >Thankyou for shopping with us </h1>")
