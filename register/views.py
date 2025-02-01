from django.shortcuts import render, redirect
from .forms import RegistrationForm  # Import the correct form
from .models import Student

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  # Use RegistrationForm
        if form.is_valid():
            # Save stage 1 data to the session
            request.session['stage1_data'] = form.cleaned_data
            return redirect('stage2')  # Redirect to stage 2
    else:
        form = RegistrationForm()  # Use RegistrationForm
    
    return render(request, 'register/reg.html', {'form': form})
from .forms import RegistrationForm, Stage2Form  # Import Stage2Form

def stage2(request):
    if 'stage1_data' not in request.session:
        return redirect('register')  # Redirect to stage 1 if no data

    if request.method == 'POST':
        form = Stage2Form(request.POST, request.FILES)  # Use Stage2Form for file uploads
        if form.is_valid():
            # Combine stage 1 and stage 2 data
            stage1_data = request.session.pop('stage1_data')
            student = Student(**stage1_data, **form.cleaned_data)
            student.save()
            return redirect('success')  # Redirect to success page
    else:
        form = Stage2Form()
    
    return render(request, 'register/stage2.html', {'form': form})

def success(request):
    return render(request, 'register/success.html')