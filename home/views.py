from django.shortcuts import render
from .models import Project, User, BugList, Edition, Modular
from django.http import HttpResponse
import datetime
import pytz


def project_list(request):
    pro_list = Project.objects.all()
    return render(request, 'project-list.html', {'pro_list': pro_list})


def overview(request):
    user_id = request.session['user_id']
    pro_id = request.GET.get("project_id")
    if request.GET.get("name"):
        name = request.GET.get("name")
        user = User.objects.all().get(id=user_id)
        Project.objects.create(founder=user, status=0, project_name=name)
        pro_id = Project.objects.all().get(project_name=name).id
        Edition.objects.create(project_name_id=pro_id, edition="默认版本")
        Modular.objects.create(project_name_id=pro_id, modular="默认模块")
        data = pro_id
        return HttpResponse(data)
    project = Project.objects.all().get(id=pro_id)
    bugs_high = BugList.objects.all().filter(project_name=project, priority="高危")
    bugs_new = BugList.objects.all().order_by('-create_time')
    return render(request, 'overview.html',
                  {'project': project, 'bugs_high': bugs_high, 'bugs_new': bugs_new, 'pro_id': pro_id})


def assign_for_me(request):
    user_id = request.session['user_id']
    pro_id = request.GET.get("project_id")
    bugs = BugList.objects.all().filter(handler_id=user_id, project_name_id=pro_id)
    return render(request, 'bug_list.html', {'bugs': bugs, 'pro_id': pro_id, 'bz': 1})


def my_create(request):
    user_id = request.session['user_id']
    pro_id = request.GET.get("project_id")
    bugs = BugList.objects.all().filter(founder_id=user_id, project_name_id=pro_id)
    return render(request, 'bug_list.html', {'bugs': bugs, 'pro_id': pro_id, 'bz': 0})


def bugs_all(request):
    pro_id = request.GET.get("project_id")
    bugs = BugList.objects.all().filter(project_name_id=pro_id)
    return render(request, 'bug_all.html', {'bugs': bugs, 'pro_id': pro_id})


def project_info(request):
    pro_id = request.GET.get("project_id")
    edition = Edition.objects.all().filter(project_name_id=pro_id)
    modular = Modular.objects.all().filter(project_name_id=pro_id)
    return render(request, 'project_management.html', {'pro_id': pro_id, 'edition': edition, 'modular': modular})


def todo_list(request):
    id = request.session['user_id']
    user = User.objects.all().get(id=id)
    do_list = BugList.objects.all().filter(handler=user)
    if request.method == "POST":
        num = do_list.count()
        return HttpResponse(num)
    return render(request, 'to-do_list.html', {'do_list': do_list})


def personal_data(request):
    id = request.session['user_id']
    personal = User.objects.all().filter(id=id)
    return render(request, 'personal_data.html', {'personal': personal})


def add_bug(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        title = request.POST.get("title")
        edition = request.POST.get("edition")
        modular = request.POST.get("modular")
        handler = request.POST.get("handler")
        priority = request.POST.get("priority")
        text = request.POST.get("text")
        pro_id = request.POST.get("pro_id")
        create_time = datetime.datetime.now(pytz.timezone('PRC'))
        if request.POST.get("bug_id"):
            bug_id = request.POST.get("bug_id")
            BugList.objects.filter(id=bug_id).update(title=title, founder_id=user_id, edition_id=edition, modular_id=modular, handler_id=handler, priority=priority, describe=text, project_name_id=pro_id, create_time=create_time)
        else:
            BugList.objects.create(title=title, founder_id=user_id, edition_id=edition, modular_id=modular, handler_id=handler, priority=priority, describe=text, project_name_id=pro_id, create_time=create_time)
        return HttpResponse(1)

    pro_id = request.GET.get("project_id")
    edition = Edition.objects.all().filter(project_name_id=pro_id)
    modular = Modular.objects.all().filter(project_name_id=pro_id)
    user = User.objects.all()
    if request.GET.get("bug_id"):
        bug_id = request.GET.get("bug_id")
        bug_edit = BugList.objects.get(id=bug_id)
        return render(request, 'edit_bug.html', {'pro_id': pro_id, 'edition': edition, 'modular': modular, 'user': user, 'bug_edit': bug_edit})
    return render(request, 'add_bug.html', {'pro_id': pro_id, 'edition': edition, 'modular': modular, 'user': user})


def guidang(request):
    pro_id = request.POST.get("project_id")
    Project.objects.all().filter(id=pro_id).update(status=1)
    return HttpResponse(1)
