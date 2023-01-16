from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def SubAns(request):

    ev = int(request.GET.get('ev'))
    ans = int(request.GET.get('ans'))
    Answer.objects.create(answer=ans,event_id=ev,EntryAgent_id=request.user.profile.id)
    return render(request, 'apps/microsurveys/templates/microsurveys/SubAns.html')
