from django.shortcuts import render_to_response
# from django.core.urlresolvers import reverse
# from django.http import HttpResponseRedirect
# from django.core.exceptions import ValidationError
# from django.views import generic

def index(request):
   return render_to_response('index.html')
