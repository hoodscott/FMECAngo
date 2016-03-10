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
    
    # get the curent table, 404 if no table at this url
    table = get_object_or_404(Table, slug=slug)
    context_dict['table'] = table
    
    #If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # check what form has been submitted
        print 'posted'
        if 'component' in request.POST:
            # handle component form
            component_form = ComponentForm(request.POST, prefix='component')
            if component_form.is_valid():
                component_form.save()
                # redirect to updated page
                return redirect(reverse('table', args=[str(table.slug)]))
            else:
                print "ERROR", component_form.errors
            # remake form incase of errors
            failuremode_form = FailureModeForm(prefix='failuremode')
            
        elif 'failuremode' in request.POST:
            # handle failuremode form
            failuremode_form = FailureModeForm(request.POST, prefix='failuremode')
            if failuremode_form.is_valid():
                failuremode_form.save()
                # redirect to updated page
                return redirect(reverse('table', args=[str(table.slug)]))
            else:
                print "ERROR", failuremode_form.errors
            # remake form incase of errors
            component_form = ComponentForm(prefix='component')
    else:
        # Not a HTTP POST, so we render our form using a ModelForm instance.
        failuremode_form = FailureModeForm(prefix='failuremode')
        component_form = ComponentForm(prefix='component')
        
    # add forms to dict
    context_dict['failuremode_form'] = failuremode_form
    context_dict['component_form'] = component_form
        
    # get the components and modes to show in table
    context_dict['components'] = Component.objects.all()
    
    return render_to_response('fmecango/table.html', context_dict, context)
  
# main page view, with explaination, list of tables, and a way to add more
def index(request):
  
    # get context of request
    context = RequestContext(request)
    # create dictionary to pass data to templates
    context_dict = {}
    
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # pass in instance of the record to be updated
        form = TableForm(request.POST, request.FILES)
        # If the two forms are valid...
        if form.is_valid():
            # hold off on saving until the diagram is attached
            table = form.save(commit=False)
            
            # add image to diagram
            if request.FILES['path']:
              table.diagram = request.FILES['path']
              
            # create the object
            table.save()
            
            # redirect to new page
            return redirect(reverse('table', args=[str(table.slug)]))

        # Invalid form or forms print problems to the terminal.
        else:
            print "ERROR", form.errors

    # Not a HTTP POST, so we render our form using a ModelForm instance.
    else:
        form = TableForm()
        
    # add form to dict
    context_dict['form'] = form
        
    # get the tables to show the user the already created ones
    context_dict['tables'] = Table.objects.all().order_by('name')
  
    return render_to_response('fmecango/index.html', context_dict, context)