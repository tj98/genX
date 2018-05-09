from django.shortcuts import render
from .models import *

# Create your views here.

def post(request):
	if(request.session['usn'] != 'EXIT'):
		if(request.method=='POST'):
			# name = request.POST.get('stu_name')
			# usn = request.POST.get('stu_usn')
			# branch = request.POST.get('stu_branch')
			# sem = request.POST.get('stu_sem')
			Usn=request.session['usn']
			Name=request.session['name2']
			Sem=request.session['sem2']
			Branch=request.session['branch2']
			clg_Visited = request.POST.get('clg_visited')
			eventName = request.POST.get('event_name')
			eventDateStart = request.POST.get('event_date_start')
			eventDateEnd = request.POST.get('event_date_end')
			description = request.POST.get('event_description')
			if(clg_Visited=="" or eventName=="" or eventDateStart==""):
				print('hi')

			else:
				form = table(Name=Name,USN=Usn,Sem=Sem,Branch=Branch,clgVisited=clg_Visited,EventName=eventName,EventDateStart=eventDateStart,EventDateEnd=eventDateEnd,Description=description)
				form.save()
				request.session['usn'] = 'EXIT'

				return render(request,'complete.html')
		return render(request,'login.html')
	return render(request,'login.html')

def index(request):
    return render(request,'complete.html')

def login(request):
	if(request.method=='POST'):
		USN = request.POST.get('usn')
		usn='\''+ USN.upper() +'\''
		if(StuRecord.objects.filter(username = usn).exists()):
			name = StuRecord.objects.filter(username = usn).values('first_name')
			Name= name[0]['first_name']
			sem = StuRecord.objects.filter(username = usn).values('sem')
			Sem = sem[0]['sem']
			branch = StuRecord.objects.filter(username = usn).values('department_id')
			Branch = branch[0]['department_id']
			Usn = usn
			if float(Branch) == float(1.0):
				Branch="CSE"
			elif float(Branch) == float(2.0):
				Branch="ISE"
			elif float(Branch) == float(3.0):
				Branch="CIV"
			elif float(Branch) == float(4.0):
				Branch="ECE"
			elif float(Branch) == float(5.0):
				Branch="EEE"
			elif float(Branch) == float(6.0):
				Branch="TCE"
			elif float(Branch) == float(7.0):
				Branch="MECH"
			context={'name1':Name,'sem1':Sem,'branch1':Branch,'usn1':Usn}
			request.session['usn'] = usn
			request.session['name2'] = Name
			request.session['branch2'] = Branch
			request.session['sem2'] = Sem
			return render(request,'index.html',context)
		return render(request,'login.html')
	return render(request,'login.html')
