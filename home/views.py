from django.shortcuts import render
from django.views.generic import View


class HomePage(View):
    def get(self, requset):
         return render(requset, 'home/home.html', context={})

# Create your views here.
