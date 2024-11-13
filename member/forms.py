from django import forms
from .models import Member

class MemberSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label='First Name or Last name',
        widget=forms.TextInput(attrs={'class': 'border-2 border-slate-400 px-2 rounded-lg'})
    )
    
class MemberAddForm(forms.ModelForm):
    class Meta:
        model=Member
        fields=["firstname","lastname"]
  

    