from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import formuser,feedform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import random
from .models import txtmsg,UserProfile,feedbackform
import json
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse

def loginpage(request):
  if request.user.is_authenticated:
      return redirect('profile/')
  if request.method=="POST":
      forml=AuthenticationForm(request=request ,data=request.POST)
      if forml.is_valid():
         username=forml.cleaned_data['username']
         password=forml.cleaned_data['password']
         user=authenticate(username=username , password=password)
         if user is not None:
            login(request,user)
            return redirect("/")
  else:
      forml=AuthenticationForm()
    
  return render(request,"index.html",{'forml':forml})


def signup(request):
    if request.user.is_authenticated:
        return redirect('/profile/')
    if request.method=="POST":
        fm=formuser(request.POST)
        if fm.is_valid():
            fm.save()
            email=fm.cleaned_data['email']
            username=request.user.username
            subject = f'Welcome {username} to Secret Admirer '
            message = f'''Thank you for Registering to our app.
            Get honest feedback from your coworkers, friends and families.
            Just share your customised link and start recieving feebacks.
            Visit your profile here : http://www.secretadmirer.com:8000/profile/ '''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
            return redirect("/") 
        else:
            return render(request,"signup.html",{'form':fm})

    else:
        fm=formuser()
        return render(request,"signup.html",{'form':fm})

   

@login_required(login_url="/")
def profile(request):
    msgs=(txtmsg.objects.filter(user=request.user))
    length=len(msgs)
    msgs=reversed(txtmsg.objects.filter(user=request.user))
    rand1=random.randint(999,9999)
    rand2=random.randint(9999,99999)
    Id=UserProfile.objects.filter(user=request.user)
    if request.is_ajax() :
        data=json.load(request)
        value=data['post-data']
        text_msg=txtmsg(id=value)
        text_msg.delete()
        mydata={
            'mydata':value
        }
        print(mydata)
        return JsonResponse(mydata)
    if request.method=="POST":
        if (Id.exists()):
          user_profile =UserProfile(id=Id[0].id)
        else:
            user_profile =UserProfile()
        user_profile.user=(request.user)
        user_profile.picture=request.FILES["profilepic"]
        user_profile.save()
        pic=UserProfile.objects.filter(user=request.user)
        return render(request,"profile.html",{'rand1':rand1,'rand2':rand2,"msgs":msgs,"len":length,"range":range(length-1,-1,-1),"pic":pic[0]})
    else:
        if UserProfile.objects.filter(user=request.user).exists():
            pic=UserProfile.objects.filter(user=request.user)
            return render(request,"profile.html",{'rand1':rand1,'rand2':rand2,"msgs":msgs,"len":length,"range":range(length-1,-1,-1),"pic":pic[0]})
        else:
            pic=UserProfile.objects.filter(user=request.user)
            return render(request,"profile.html",{'rand1':rand1,'rand2':rand2,"msgs":msgs,"len":length,"range":range(length-1,-1,-1),"pic":pic})


@login_required(login_url="/")
def logmeout(request):
    logout(request)
    return redirect('/')

def sendmsg(request,Id):
    
    users=User.objects.filter(id=Id)
    us=users[0]
    if request.method=="POST":
        txt=request.POST["txtarea"]
        a=txtmsg(message=txt, user=users[0])
        # print(us.)
        a.save()
        subject = 'New message recieved'
        message = f'''Dear {us.username} ,You have recieved a new message :)
        Please check it out here: secretadmirer.com:8000/profile'''
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [us.email, ]
        send_mail( subject, message, email_from, recipient_list )
        if UserProfile.objects.filter(user=request.user).exists():
            pic=UserProfile.objects.filter(user=request.user)
            return render(request,"thankyou.html",{"reciever":users[0],"pic":pic[0]})
        else:
            pic=UserProfile.objects.filter(user=request.user)
            return render(request,"thankyou.html",{"reciever":users[0],"pic":pic})
        
    else:
        if UserProfile.objects.filter(user=request.user).exists():
            pic=UserProfile.objects.filter(user=request.user)
            return render(request,"msgsent.html",{"reciever":users[0],"pic":pic[0]})
        else:
            pic=UserProfile.objects.filter(user=request.user)
            return render(request,"msgsent.html",{"reciever":users[0],"pic":pic})
        


def aboutus(request):
     if UserProfile.objects.filter(user=request.user).exists():
            pic=UserProfile.objects.filter(user=request.user)
            return render(request,"about.html",{"pic":pic[0]})
     else:
            pic=UserProfile.objects.filter(user=request.user)
            return render(request,"about.html",{"pic":pic})

def feed(request):
    if request.method=="POST":
        frm=feedform(request.POST)
        if frm.is_valid():
            frm.save()
            email=frm.cleaned_data['email']
            subject = 'Secret Admirer feedback recieved'
            message = f'''Thank you {email} for filling out the feedback from.
            We really appreciate your efforts.
            Please share if you enjoyed it :).
            link: secretadmirer.com:8000'''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )

            if UserProfile.objects.filter(user=request.user).exists():
                 pic=UserProfile.objects.filter(user=request.user)
                 return render(request,"thankfeed.html",{"pic":pic[0],"frm":frm})
            else:
                pic=UserProfile.objects.filter(user=request.user)
                return render(request,"thankfeed.html",{"pic":pic,"frm":frm})
        else:
                if UserProfile.objects.filter(user=request.user).exists():
                    pic=UserProfile.objects.filter(user=request.user)
                    return render(request,"feedback.html",{"pic":pic[0],"frm":frm})
                else:
                    pic=UserProfile.objects.filter(user=request.user)
                    return render(request,"feedback.html",{"pic":pic,"frm":frm})     
    else:
        frm=feedform()
        if UserProfile.objects.filter(user=request.user).exists():
                 pic=UserProfile.objects.filter(user=request.user)
                 feed1=feedbackform.objects.all()
                 length=len(feed1)
                 return render(request,"feedback.html",{"pic":pic[0],"frm":frm,"feed":feed1,"len":length})
        else:
                pic=UserProfile.objects.filter(user=request.user)
                feed1=feedbackform.objects.all()
                length=len(feed1)
                return render(request,"feedback.html",{"pic":pic,"frm":frm,"feed":feed1,"len":length})