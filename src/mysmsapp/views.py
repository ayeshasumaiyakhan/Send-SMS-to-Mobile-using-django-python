from django.shortcuts import render, HttpResponse
import json
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from .models import Contact_details
from django.views import generic
import urllib.request
import urllib.parse

class Index(View):

    def get(self, request):
        # The get request just renders the html page
        return render(request,'Index.html',{})

    def post(self, request, *args, **kwargs):
        # from this post request the variables get the phone_number, name and message
        phone_number = request.POST.get('phonenumber')
        name = request.POST.get('name')
        message = request.POST.get('message')
        #get your apikey from the official textlocal api website and insert it in the 1st parameter
        resp =  self.sendSMS('insert your own apikey', phone_number,'TXTLCL', message)
        print (resp)
        return render(request, 'Index.html',{})

    def sendSMS(self,apikey, numbers, sender, message):
        data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
            'message' : message, 'sender': sender})
        data = data.encode('utf-8')
        request = urllib.request.Request("https://api.textlocal.in/send/?")
        f = urllib.request.urlopen(request, data)
        fr = f.read()
        return(fr)

        return render(request, 'Index.html',{})
