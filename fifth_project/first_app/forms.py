from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="User name", initial='jamal', help_text='Highest 70 characters', required=False,widget=forms.Textarea(attrs={'placeholder': 'Enter your name'}))
    # file = forms.FileField()
    # email = forms.EmailField()
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    # CHOICES = [('S', 'Small'),('M', 'Medium'),('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    MEAL = [('P', 'Pepperoni'),('M', 'Mashroom'),('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    
# class studentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data['name']
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("Enter a name with at least 10 character")
#     #     return valname
#     # def clean_email(self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     return valemail
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("Enter a name with at least 10 character")
        
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")
           
class studentData(forms.Form):
    name = forms.CharField( validators=[validators.MinLengthValidator(10, message="Enter a name with at least 10 character")])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(34, message="Age must be max 34"), validators.MinValueValidator(24,message="Age must be at least 24")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="file extension ended with .pdf")])
    
class passwordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        valpass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        valname = self.cleaned_data['name']
        if valpass != val_conpass:
            raise forms.ValidationError("Password doesn't match")
        if len(valname) < 15:
            raise forms.ValidationError('Name must be at least 15 character')