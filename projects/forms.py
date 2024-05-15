from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # field = ['title']
        field = '__all__'