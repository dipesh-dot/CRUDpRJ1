from django.shortcuts import render,HttpResponseRedirect

from .forms import studentRegistration

from  .models  import User
from django.contrib import messages




def entryData(request):
    
    if request.method == 'POST':
        fm = studentRegistration(request.POST)
        if fm.is_valid():
            n= fm.cleaned_data['name']
            E = fm.cleaned_data['email']
            p= fm.cleaned_data['password']  
            print('clean data:', fm.cleaned_data)
            reg= User( name = n,email=E,password=p )            
            reg.save()
            fm = studentRegistration()
           
            messages.add_message(request,messages.SUCCESS,'YOUR DATA IS SUBMITED')
            return render(request, 'myapp/success.html',{'nm':n})         

    else:
        fm = studentRegistration()
    stud = User.objects.all()    
    return render(request, 'myapp/addandshow.html',{'form':fm,'stu':stud})        



def delete_data(request,id):

    
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
   

def Update_data(request,id):
    if request.method == 'POST':
       pi = User.objects.get(pk=id)

       fm = studentRegistration(request.POST,instance = pi) 
       if fm.is_valid():
    
        fm.save()
       

    else:
       pi = User.objects.get(pk=id)

       fm = studentRegistration(instance = pi) 

    return render(request, 'myapp/updatestudent.html',{'form' :fm,'id':id})        
       