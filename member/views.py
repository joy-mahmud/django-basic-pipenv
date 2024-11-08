from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from member.models import Member
from django.views.decorators.http import require_http_methods



# Create your views here.
@require_http_methods(["GET","POST","DELETE","PUT"]) #it controls which type of request can we perform for this view
def home(request):
    mymembers=Member.objects.all().values()
    context={
        'mymembers':mymembers
    }
    return render(request,'home.html',context)

def add_member(request):
    member= Member(firstname="joy",lastname='mahmud')
    member.save()
    
def add_member_by_url(request):
    firstname=request.GET.get('firstname')
    lastname=request.GET.get('lastname')
    
    if not all([firstname,lastname]):
        return HttpResponse('missing required parameter')
    
    try:
        member=Member.objects.create(firstname=firstname,lastname=lastname)
        # return HttpResponse(f"member added id:{member.id}")
        return JsonResponse({'message':'member add','status':200})
    except:
        return HttpResponse('something went wrong')
    
def view_members(request):
    members = list(Member.objects.all().values())
    return JsonResponse({"members":members})
    
    
    
    
    
