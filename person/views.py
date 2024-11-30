from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from bson.json_util import dumps
from bson.objectid import ObjectId
from .models import personCollection,printCollection

# Create your views here.

def home(request):
    printCollection()
    return HttpResponse('<h2>django server is running</h2>')
def add_person(request):
    record=[
        {
        "name":'john',
        "email":'john@gmail.com'
        
        },
        {
         "name":'doe',
         "email":'doe@gmail.com'   
        }
        
    ]
    personCollection.insert_many(record)
   
    return HttpResponse('person record added successfully')
def view_all_person(request):
    persons=personCollection.find()
    person_json=[]
    for person in persons:
        person['_id']=str(person['_id'])
        person_json.append(person)
    return JsonResponse(person_json,safe=False)

def person_details(request):
    id="67497dcefb9111c61bf0cc57"
    person= personCollection.find_one({'_id':ObjectId(id)})
    print(person['name'])
    person['_id']=str(person['_id'])
    person_json=person
    return JsonResponse(person_json,safe=False)