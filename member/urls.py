from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home),
    path('addMember/',views.add_member, name="add_member"),
    path('addMemberByUrl/',views.add_member_by_url),
    path('viewMembers/',views.view_members)
]
