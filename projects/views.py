from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    all_projects = Project.objects.all()
    context = {'all_projects': all_projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    single_project = Project.objects.get(id=pk)
    tags = single_project.tags.all()
    context = {'single_project': single_project, 'tags': tags}
    return render(request, 'projects/single_project.html', context)


def create_project(request):
    form = ProjectForm()

    # retrieving the posted information, verifying it, then saving it back to the db
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def update_project(request, pk):
    single_project = Project.objects.get(id=pk)
    form = ProjectForm(instance=single_project)  # pre-filling the form with the object's data

    # retrieving the new posted information, verifying it, then saving it back to the db
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=single_project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def delete_object(request, pk):
    remove_project = Project.objects.get(id=pk)

    # removing the selected project if the user clicks on the 'confirm' button
    if request.method == 'POST':
        remove_project.delete()
        return redirect('projects')

    context = {'remove_project': remove_project}
    return render(request, 'projects/delete_template.html', context)

