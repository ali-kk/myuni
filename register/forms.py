from django import forms

# Define choices for college and department
COLLEGE_CHOICES = [
    ('', 'Select College'),  # Empty choice
    ('Medicine', 'College of Medicine'),
    ('Engineering', 'College of Engineering'),
    ('Science', 'College of Science'),
]

DEPARTMENT_CHOICES = [
    ('', 'Select Department'),  # Empty choice
    ('CS', 'Computer Science'),
    ('ME', 'Mechanical Engineering'),
    ('PH', 'Physics'),
]

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    second_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Second Name'})
    )
    third_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Third Name'})
    )
    college = forms.ChoiceField(
        choices=COLLEGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    department = forms.ChoiceField(
        choices=DEPARTMENT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

# Add a second form for stage 2 (e.g., file uploads)
class Stage2Form(forms.Form):
    national_id_front = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    national_id_back = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    uni_id_photo = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )