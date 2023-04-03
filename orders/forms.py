from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class Registration(UserCreationForm):
    # username = forms.CharField(label='Username', required=True, help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",max_length="50", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'jsmith'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"jsmith"})
        self.fields['password1'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"*******"})
        self.fields['password2'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"*******"})

class Login(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"jsmith"})
        self.fields['password'].widget.attrs.update({'class':'form-control form-control-sm rounded-0', 'placeholder':"*******"})