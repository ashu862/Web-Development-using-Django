from django.shortcuts import render,HttpResponse
from . models import Jobs, Resume
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request,'index.html') 

def jobs(request):
    if  request.method == 'POST':
        name = request.POST.get('name')
        exp = request.POST.get('exp')
        location = request.POST.get('location')
        emps = Jobs.objects.all()
        if name:
            emps = emps.filter(name__icontains=name)
        if exp:
            emps = emps.filter(exp=exp)
        if location:
            emps = emps.filter(location__icontains=location)
        
        context = {'emps': emps}
        return render(request, 'jobs.html', context)
    
    elif request.method == 'GET':
        emps = Jobs.objects.all()
        context = {'emps': emps}
        return render(request, 'jobs.html', context)
    
    else:
        return HttpResponse('Invalid occurrence')

def apply(request):
    return render(request,'apply.html') 




def form(request):
    if request.method == 'POST':
       full_name=request.POST['full_name']
       email=request.POST['email']
       phone=int(request.POST['phone'])
       resume_file=request.POST['resume_file']
       role = request.POST.get('role')
       new_emp=Resume(full_name=full_name, email=email, phone=phone, resume_file=resume_file, role=role)
       new_emp.save()
       return HttpResponse('application submitted succesfully')
    
    elif request.method == 'GET':
       return render(request, 'form.html')
    else:
       return HttpResponse('an error encountered,application cannot submitted')
    
def success(request):
    if request.method == 'POST' or request.method == 'GET':
        emps = Resume.objects.all()
        context = {'emps': emps}
        return render(request, 'success.html', context)
    else:
        return HttpResponse('an error occured')