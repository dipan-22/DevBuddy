from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from django.contrib.auth.decorators import  login_required
from .forms import ProjectForm
# Create your views here.

# def home(request):
#     return HttpResponse("This is home")

# projectsList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio Website',
#         'description': 'A personal website to write articles and display work'
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'An open source project built by the community'
#     }
# ]


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
    # tags = projectObj.tags.all()
    # msg = "hola"
    # for i in projectsList:
    #     if i['id'] == str(pk):
    #         projectObj=i
    # return render(request,'projects/single-project.html',{'project':projectObj,'tags':tags})
    return render(request,'projects/single-project.html',{'project':projectObj})

@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
            

    context={'form':form}
    return render(request,"projects/project_form.html",context)


# creating the update operations
@login_required(login_url="login")
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
            

    context={'form':form}
    return render(request,"projects/project_form.html",context)


# delete operations
@login_required(login_url="login")
def deleteProject(request, pk):
    
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context={'object':project}
    return render(request, 'projects/delete_template.html',context)