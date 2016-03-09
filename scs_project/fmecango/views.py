#django imports
from django.core.urlresolvers import reverse, resolve
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
# import forms and models of this project
from forms import *
from models import *

# view to show the fmeca table and add to it
def table(request, slug):
    # get context of request
    context = RequestContext(request)
    # create dictionary to pass data to templates
    context_dict = {}
    
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # pass in instance of the record to be updated
        form = ComponentForm(data=request.POST)
        # If the two forms are valid...
        if form.is_valid():
            # Save the form data to the database.
            component = form.save()
            
            # redirect to new page
            return redirect(reverse('table', args=[str(table.slug)]))

        # Invalid form or forms print problems to the terminal.
        else:
            print "ERROR", form.errors

    # Not a HTTP POST, so we render our form using a ModelForm instance.
    else:
        user_form = ComponentForm()
        
    # get the components
    
    return render_to_response('fmecango/table.html', context_dict, context)
  
def index(request):
  
    # get context of request
    context = RequestContext(request)
    # create dictionary to pass data to templates
    context_dict = {}
    
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # pass in instance of the record to be updated
        form = TableForm(data=request.POST)
        # If the two forms are valid...
        if form.is_valid():
            # Save the form data to the database.
            table = form.save()
            
            # redirect to new page
            return redirect(reverse('table', args=[str(table.slug)]))

        # Invalid form or forms print problems to the terminal.
        else:
            print "ERROR", form.errors

    # Not a HTTP POST, so we render our form using a ModelForm instance.
    else:
        form = TableForm()
        
    # get the components
  
    return render_to_response('fmecango/index.html', context_dict, context)