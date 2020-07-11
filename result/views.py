from django.shortcuts import render,redirect
#from django.contrib import messages
from django.db.models import Q
from .models import *

# Create your views here.

def home(r):
    
    return render(r,'home.html')


def msearch(r):
    
    return render(r,'msearch.html')

def mresult(r):
    if r.method == "GET":
        roll = r.GET.get('rollno')
        rollcode = r.GET.get('rollcode')
        
        cond = Q(roll_no = roll) & Q(roll_code = rollcode)
        
        result = MatricResult.objects.filter(cond).count()
        
        if (result > 0 ):
            sst = MatricResult.objects.get(cond).sst
            sci = MatricResult.objects.get(cond).sci
            math = MatricResult.objects.get(cond).math
            hindi = MatricResult.objects.get(cond).hindi
            eng = MatricResult.objects.get(cond).eng
        
            marks = sst + sci + math + hindi + eng
            
            result = ""
            if (marks >= 300):
                result = "1st"
            elif (marks >= 250):
                result = "2nd"
            elif (marks >= 155):
                result = "fail"
              
        
            data = {
                "result":MatricResult.objects.filter(cond),
                "t_mark":marks,
                "division":result
                }
        else:
            return redirect(msearch)
    
    return render(r,'mresult.html',data)


def scisearch(r):
    
    return render(r,'scisearch.html')

def sciresult(r):
    if r.method == "GET":
        roll = r.GET.get('rollno')
        rollcode = r.GET.get('rollcode')
        
        cond = Q(roll_no = roll) & Q(roll_code = rollcode)
        
        check = InterResult.objects.filter(cond).count()
        
        if (check > 0 ):
            phy = InterResult.objects.get(cond).phy
            che = InterResult.objects.get(cond).che
            bio = InterResult.objects.get(cond).bio
            math = InterResult.objects.get(cond).math
            hindi = InterResult.objects.get(cond).hindi
            eng = InterResult.objects.get(cond).eng
        
            x = phy + che + bio + math + hindi + eng

            result = ""
            if (x >= 300):
                result = "1st"
            elif (x >= 250):
                result = "2nd"
            elif (x >= 155):
                result = "fail"
                
                
            data = {
                "result":InterResult.objects.filter(cond),
                "t_mark":x,
                'division':result
                }
            
        else:
            return redirect(scisearch)
        
    return render(r,'sciresult.html',data)


def besearch(r):
    
    return render(r,'besearch.html')


def notfond(r):
    
    return render(r,'notfond.html')


def beresult(r):
    if r.method == "GET":
        rollno = r.GET.get("rollno")
        rollcode = r.GET.get("rollcode")
        
        cond = Q(roll_no = rollno) & Q(roll_code = rollcode)
        
        check = BeResult.objects.filter(cond).count()
        
        if (check > 0):
            data = {"result":BeResult.objects.filter(cond)}
        
        else:
            #messages.warning(r,"field to submit")
            return redirect(besearch)
            
    return render(r,'beresult.html',data)
        
