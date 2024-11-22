from django import forms
from .models import Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['author','bio','website','birthDate']
        widgets = {
           # 'author': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for authors
            'bio': forms.Textarea(attrs={'class': 'border-[1px] border-black', 'rows': 3}),
            'website': forms.URLInput(attrs={'class': 'border-[1px] border-black'}),
            'birthDate': forms.DateInput(attrs={'class': 'border-[1px] border-black', 'type': 'date'}),
        }