from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import mysql.connector as sql



def Shivhome(request):

    return render (request, 'Shiv.html')

def Aboutpage(request):

    return render (request, 'about.html')

def Confipage(request):
    return render (request, 'annual.html')

def Registerpage(request):
    return render (request, 'register.html')

def Memberpage(request):

    return render (request, 'members.html')

def Achievementpage(request):

    return render (request, 'achievement.html')

# def Signuppage(request):
#     if request.method =='POST':
#         uname=request.POST.get('username')
#         Email=request.POST.get('email')
#         pass1=request.POST.get('pass1')
#         pass2=request.POST.get('pass2')
#         if pass1 != pass2:
#             return HttpResponse('password are not same ')
#         else:
#             my_user=User.objects.create_user(uname,Email,pass1)
#             my_user.save()
           
#             return redirect('Home')
        
#     return render (request, 'Signup.html')

def Loginpage(request):
    
    if request.method == 'POST':
         user=request.POST.get('username')
         pass1=request.POST.get('password')
         user=authenticate(request, username=user,password=pass1)
         if user is not None:
            login(request, user)
            return redirect('Config')
         else:
            context = {'error_message': "password doesn't match"}
            return render(request, 'error.html', context)

        #  print(user,pass1)

    return render (request, 'shivlog.html')

def logoutpage(request):
    logout(request)
    return redirect('login')



# un=''
# tel=''
# em=''
# gen=''


def form(request):
    global un,tel,em,gen
    if request.method=="POST":
        m=sql.connect(host='localhost',user='root',password='Tarun@9927',database='mohit')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='username':
                un=value
            if key=='mobile':
                tel=value
            if key=='email':
                em=value
            if key=='genre':
                gen=value
        c="insert into users999 Values('{}','{}','{}','{}')".format(un,tel,em,gen)                   
        cursor.execute(c)
        m.commit()
    return render (request,"mission.html")    

   
