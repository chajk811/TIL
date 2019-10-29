from django.shortcuts import render

def team(request):
    return render(request, 'about/team.html')

def members(request):
    starting_members = ['이상해씨', '파이리', '꼬부기']
    context = {'startings': starting_members}
    return render(request, 'about/members.html', context)
