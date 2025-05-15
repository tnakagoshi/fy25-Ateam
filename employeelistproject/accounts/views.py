from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.views.generic import TemplateView


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list-employee')  # Redirect to a success page
        else:
            return render(request, 'registration/login.html', {'error': 'ユーザー名またはパスワードが正しくありません'})
    return render(request, 'registration/login.html')    

def logout_view(request):
    logout(request)
    return redirect('logout-success')  # Redirect to a success page

class LogoutSuccessView(TemplateView):
    template_name = 'registration/logout.html'
