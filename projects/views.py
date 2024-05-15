from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

# def home(request):
#     return HttpResponse("This is home")

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    # page='projects'
    # number = 11
    # context={'page':page,'number':number,'projects':projectsList}
    projects=Project.objects.all()
    context={'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request,pk):
    # projectObj = None
    projectObj = Project.objects.get(id=pk)
    # msg = "hola"
    # for i in projectsList:
    #     if i['id'] == str(pk):
    #         projectObj=i
    return render(request,'projects/single-project.html',{'project':projectObj})