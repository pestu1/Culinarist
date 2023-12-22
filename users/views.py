from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        #Näytä tyhjä lomake
        form = UserCreationForm()
    else:
        #prosessi valmis lomake
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            #kirjaa sisään ja ohjaa kotisivulle
            login(request, new_user)
            return redirect('culinarists:index')
            
    #näytä tyhjä tai invalidi formi
    context = {'form': form}
    return render(request, 'registration/register.html', context)

