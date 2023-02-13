
from django.conf import settings
from django.shortcuts import render, redirect
from projects.models import Project, Job, Technology, ArtWork
from .forms import ContactForm
from django.shortcuts import redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

def project_index(request):
    projects = Project.objects.all()
    jobs = Job.objects.all().order_by("-id")
    techs = Technology.objects.all()
    artworks = ArtWork.objects.all()

    context = {
        'projects': projects,
        'jobs': jobs,
        'techs': techs,
        'artworks': artworks
    }
    return render(request, 'project_index.html', context)

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/project_index')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
    

def redirect_view(request):
    response = redirect('redirect-success')
    return response

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def job_detail(request, pk):
    job = Job.objects.get(pk=pk)
    context = {
        'job': job
    }
    return render(request, 'job_detail.html', context)



# https://codepen.io/ettrics/pen/ZYqKGb
# https://codepen.io/mynoralexander/pen/gpyYOo
# https://realpython.com/get-started-with-django-1/

"""
def error_404_view(request, exception):

    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
            'first_name': form.cleaned_data['first_name'], 
            'last_name': form.cleaned_data['last_name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL], fail_silently=False) 
                messages.success(request, 'Thank you for contacting us!')
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect("project_index")
        else:
            messages.error(request, 'Boo! Hiss!')
        
    form = ContactForm()
    return render(request, "project_index.html", {'form':form})
 

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, "project_index.html", {'form': form})
"""