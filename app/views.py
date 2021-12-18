from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
import json
from django.db.models import Q
from .models import *
from .serialize import UserSerializer





def datatables(request):
    
    
    #counter
    draw=int(request.GET.get('draw'))
    print(draw)
    
    #row to start from in requested page
    start=int(request.GET.get('start'))
    print(start)
    
    #length of entries to show
    length=int(request.GET.get('length'))
    print(f"length {length}")
    
    #checking page number
    page_no=start/length
    page_no=page_no+1
    print(f"page no {page_no}")
    
    
    if page_no==0:
       
       limit=length
              
    else:
     limit=int(page_no*length)



    print(f"limit {limit}")
    queryset=UserModel.objects.all()
    records=queryset.count()
    queryset=queryset[start:limit]
  #  print(f" returning number of queries after filter {queryset.count()}")
    
    serializer=UserSerializer(queryset,many=True)
   
    
   
    #converting list of list of lists into list of list
    # for i in serializer.data:
    #     for j in i:
        
    #         data.append(j)
    
    
    return JsonResponse({
    "draw": draw,
    #total records in draw
    "recordsTotal":records,
    #total entries in records
    "recordsFiltered": records,
    "data":serializer.data
    #when we send both filtered and total as same, it will not
    #show (filtered from text which is basically not needed)
    #this is not mentioned in documentation
    })










def pagination(request,entries):
    users=UserModel.objects.all().order_by('id')
    #returns paginator object
                              #Default no' of entries (4)
    paginator=Paginator(users,entries)
    print(entries)
    #total number of data and set orphans
    paginator.orphans=paginator.count%int(entries)
    
    #Return a 1-based range of pages for iterating
    # through within a template for loop 
    pages=paginator.page_range
    
    #Takes the requested page number
    page_number=request.GET.get('page')
    
    #Returns paginator object with given 1-based index 
    #page number 
    page_obj=paginator.get_page(page_number)
    
    return page_obj,pages



def home(request):

   
    return render(request,'app/home.htm')


class Add(View):
   def get(self,request): 
    form=UserModelForm()
    return render(request,'app/add.htm',{'form':form})
   
   def post(self,request):
    print(request.POST)
    form=UserModelForm(request.POST)
    if form.is_valid():
       form.save()
       form=UserModelForm()
       messages.success(request,"User has been Successfully Added")
       return render(request,'app/add.htm',{'form':form})
  
class Update(View):
 
 def post(self,request,pk):
     form=UserModelForm(request.POST)
     if form.is_valid():
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        designation=form.cleaned_data['designation']
       #update without loading the object
        UserModel.objects.filter(id=pk).update(name=name,email=email,designation=designation)
      
        messages.success(request,"User has been Successfully Updated")
     else:
        messages.error(request,'Please Enter Valid information')  
     return render(request,'app/updateform.htm',{'id':pk,'form':form})
 
 def get(self,request,pk=None):
     if pk is None :
      entries=request.GET.get('entry',3)
      page_obj,pages=pagination(request,entries)
      print("Why page is not loading")
      return render(request,'app/update.htm',{'pages':pages,'users':page_obj})
     
    
     else:
         
          user=UserModel.objects.get(id=int(pk))
          form=UserModelForm(instance=user)
        
          return render(request,'app/updateform.htm',{'form':form,'id':pk}) 
  


class Delete(View):
 def post(self,request,pk):
     users=UserModel.objects.all().order_by('id')
     users.get(id=pk).delete()

     messages.warning(request,"User has been Successfully Deleted")
       
     return HttpResponseRedirect('/')
 
 def get(self,request,pk=None):
        
      users=UserModel.objects.get(id=pk)
    
      return render(request,'app/delete.htm',{'users':users})

class Manage(View):
    
   def get(self,request): 
    entries=request.GET.get('entry',3)
    page_obj,pages=pagination(request,entries)
    form=UserModelForm()
    return render(request,'app/manage.htm',{'users':page_obj,'pages':pages,'form':form})

 