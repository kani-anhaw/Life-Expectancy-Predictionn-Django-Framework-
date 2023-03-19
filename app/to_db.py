from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Immunization, Economic, Mortality, Social, Health


def store(request):
 # Get the text
 g = float(request.POST['v7'])
 h = float(request.POST['v8'])
 k = float(request.POST['v11'])
 m = float(request.POST['v13'])
 Immunization.objects.create(g=g, h=h, k=k, m=m)
 return HttpResponseRedirect(reverse('mortality'))

def store1(request):
 b = float(request.POST['v2'])
 l = float(request.POST['v12'])
 f = float(request.POST['v6'])
 o = float(request.POST['v15'])
 s = float(request.POST['v19'])
 Economic.objects.create(b=b, f=f, l=l, o=o, s=s)
 return HttpResponseRedirect(reverse('social'))

def store2(request):
 i = float(request.POST['v9'])
 q = float(request.POST['v17'])
 r = float(request.POST['v18'])
 Health.objects.create(i=i, q=q, r=r)
 return HttpResponseRedirect(reverse('economic'))

def store3(request):
 c = float(request.POST['v3'])
 d = float(request.POST['v4'])
 e = float(request.POST['v5'])
 j = float(request.POST['v10'])
 n = float(request.POST['v14'])
 Mortality.objects.create(c=c, d=d, e=e, j=j, n=n)
 return HttpResponseRedirect(reverse('health'))

def store4(request):
 p = float(request.POST['v16'])
 t = float(request.POST['v20'])
 u = (request.POST['v21'])
 Social.objects.create(p=p, t=t, u=u)
 return HttpResponseRedirect(reverse('immunization'))








