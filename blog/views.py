from django.shortcuts import render,redirect,HttpResponse
from .models import Student,About
from django.contrib.auth.models import auth,User
from django.contrib import messages
# from location_field.models.plain import PlainLocationField

def index(request):
	obj= Student.objects.all()
	data=''
	if request.method == 'POST':
		standard=request.POST['std']
		roll= int(request.POST['rollno'])
	
		for i in obj:
			stand=str(i.standard)
			roll_no=int(i.roll)
			if standard==stand and roll==roll_no:
				data=i
			else:
				res = 'No Record Found...'
		return render(request,'blog/index.html',{'data':data,'res':res})
	return render(request,'blog/index.html')

def insert(request):
	# roll=request.POST['rollno']
	return render(request,'blog/insert.html')

def update(request):
	obj= Student.objects.all()
	obj=Student.objects.order_by().values('standard').distinct()
	if request.method == 'POST':
		data=[]
		s=1
		standard=request.POST['std']
		name= request.POST['stdname']
		stu=Student.objects.filter(standard=standard)
		for i in stu:
			if name in i.name:
				data.append((s,i))
				s+=1
		return render(request,'blog/update.html',{'data':data})
	return render(request,'blog/update.html',{'obj':obj})

def delete(request):
	obj= Student.objects.all()
	obj=Student.objects.order_by().values('standard').distinct()
	if request.method == 'POST':
		data=''
		standard=request.POST['std']
		name= request.POST['stdname']
		stu=Student.objects.filter(standard=standard,name=name)
		if stu.exists():
			data=stu.first()
		else:
			HttpResponse("<h1>Data not found</h1>")
		return render(request,'blog/delete.html',{'data':data})
	return render(request,'blog/delete.html')

def about(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		enquiry=request.POST['enquiry']
		phone=request.POST['phone']
		message=request.POST['message']

		user=About.objects.create(name=name,email=email,enquiry=enquiry,phone=phone,message=message)
		user.save()
		print('User created')
		return redirect('/')
	return render(request,'blog/about.html')

def service(request):
	return render(request,'blog/service.html')

def contact(request):
	return render(request,'blog/contact.html')

def feedback(request):
	return render(request,'blog/feedback.html')



def register(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Already Exists !')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Already Exists !')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
				user.save()
				print('User created')
				return redirect('login')
		else:
			messages.info(request,'Password does not match !')
			return redirect('register')

	else:
		return render(request,'blog/register.html')

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'Invalid Username / Password !')
			return redirect('login')
	else:
		return render(request,'blog/login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def dashboard(request):
	return render(request,'blog/dashboard.html')