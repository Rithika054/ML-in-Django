from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
        return render(request,"home.html")

def index(request):
        return render(request,"index.html")

def result(request):
        r=joblib.load('finalmodel.sav')
        lis=[]
        lis.append(request.GET['RI'])
        lis.append(request.GET['Na'])
        lis.append(request.GET['Mg'])
        lis.append(request.GET['AI'])
        lis.append(request.GET['Si'])
        lis.append(request.GET['K'])
        lis.append(request.GET['Ca'])
        lis.append(request.GET['Ba'])
        lis.append(request.GET['Fe'])
        print(lis)
        
        ans=r.predict([lis])
        return render(request,"result.html",{'ans':ans,'lis':lis})