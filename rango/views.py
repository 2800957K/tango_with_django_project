from django.shortcuts import render
from django.http import HttpResponse 
from rango.models import Category
def index(request):
    #return HttpResponse("Rango says hey there partner!\n <a href='/rango/about/'>About</a>")
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template! 
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier. 
    # Note that the first parameter is the template we wish to use. 
    return render(request, 'rango/index.html', context=context_dict)
    
def about(request):
    #return HttpResponse("Rango says here is the about page.\n <a href='/rango/'>Index</a>")
    context_dict = {}
    return render(request, "rango/about.html", context=context_dict)
    