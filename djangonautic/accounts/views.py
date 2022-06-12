from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#============================================================================1
# Create your views here.
# def signup_view(request):
#     return render(request, 'home_page/accounts/singup.html')
#===============================================================================1
#===============================================================================2
# def signup_view(request):
#     form = UserChangeForm()
#     return render(request, 'home_page/accounts/singup.html',{"form":form})
#================================================================================2

#=================================================================================3
# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('articles:list')
    else:
        form = AuthenticationForm(request.POST)
        return render(request, 'home_page/accounts/login.html', {"form": form})
#===================================================================================3
#===================================================================================4
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
           #log the user in
            return redirect('articles:list')
    else:
        form = UserCreationForm(request.POST)
    return render(request, 'home_page/accounts/singup.html', {"form": form})



