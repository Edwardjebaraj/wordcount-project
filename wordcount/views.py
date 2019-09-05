from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def counts(request):
    vari=request.GET['fulltext']
    a=[]
    a=vari.split(" ")
    dic={i:a.count(i) for i in a}
    maxi=max(dic.values())
    li=[]
    for i in dic.keys():
        if dic[i]==maxi:
            li.append(i)
    return render(request,'count.html',{'a':len(a),'vari':vari,'max':li})
def about(request):
    return render(request,'about.html')
