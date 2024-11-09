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
    
    if request.method=="POST":
        firstname =request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        member=Member.objects.create(firstname=firstname,lastname=lastname)
        return HttpResponse("member added successfully")
    # member= Member(firstname="joy",lastname='mahmud')
    # member.save()
    
def add_member_by_url(request):
    firstname=request.GET.get('firstname')
    lastname=request.GET.get('lastname')
    verified=request.GET.get('verified')
    
    if not all([firstname,lastname,verified]):
        return HttpResponse('missing required parameter')
    
    try:
        member=Member.objects.create(firstname=firstname,lastname=lastname,verified=verified)
        # return HttpResponse(f"member added id:{member.id}")
        return JsonResponse({'message':'member add','status':200,'id':member.id})
    except:
        return HttpResponse('something went wrong')
    
def view_members(request):
    members = list(Member.objects.all().values())
    verified=request.GET.get('verified')
    print(type(verified))
  
    if(verified=='1'):
        members=Member.objects.all()
        verifiedMembers=members.filter(verified=True)
        memberList=list(verifiedMembers.values())
        return JsonResponse({"members":memberList})
    elif(verified=='0'):
        members=Member.objects.all()
        NonVerifiedMembers=members.filter(verified=False)
        print(NonVerifiedMembers)
        memberList=list(NonVerifiedMembers.values())
        return JsonResponse({"members":memberList})
        #return HttpResponse('non verified')
    return JsonResponse({"members":members})
    
    
    
    
    
