from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from points.models import Team

# Create your views here.
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    team_list = Team.objects.order_by('-points')[:5]
    context_dict = {'teams':team_list, 'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'points/index.html', context=context_dict)

def show_team(request, team_name_slug):
    context_dict = {}
    try:
        team = Team.objects.get(slug=team_name_slug)
        context_dict['team'] = team

    except Team.DoesNotExist:
        context_dict['team'] = None

    return render(request, 'points/team.html', context=context_dict)


def add_5points(request, team_name_slug):
    a = Team.objects.get(slug=team_name_slug)
    count = a.points
    count = count + 5
    a.points = count
    a.save()

    return HttpResponseRedirect("/team/"+team_name_slug)

def remove_5points(request, team_name_slug):
    a = Team.objects.get(slug=team_name_slug)
    count = a.points
    count = count - 5
    a.points = count
    a.save()

    return HttpResponseRedirect("/team/"+team_name_slug)

def late(request, team_name_slug):
    a = Team.objects.get(slug=team_name_slug)
    count = a.points
    count = count - 5
    late = a.late
    a.late = late + 1
    a.points = count
    a.save()

    return HttpResponseRedirect("/team/"+team_name_slug)

def first(request, team_name_slug):
    a = Team.objects.get(slug=team_name_slug)
    count = a.points
    count = count + 30
    first = a.first
    a.first = first + 1
    a.points = count
    a.save()

    return HttpResponseRedirect("/")

def second(request, team_name_slug):
    a = Team.objects.get(slug=team_name_slug)
    count = a.points
    count = count + 30
    second = a.second
    a.second = second + 1
    a.points = count
    a.save()

    return HttpResponseRedirect("/")

def third(request, team_name_slug):
    a = Team.objects.get(slug=team_name_slug)
    count = a.points
    count = count + 30
    third = a.third
    a.third = third + 1
    a.points = count
    a.save()

    return HttpResponseRedirect("/")


def add_team():
    pass