from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = '/home/'  # Página para redirecionar após o login bem-sucedido
    
def index(request):
    return render(request, 'index.html')

@login_required
def home(request):
    user = request.user
    first_name = user.first_name if user.first_name else user.username
    is_staff_or_superuser = request.user.is_staff or request.user.is_superuser
    return render(request, 'home.html', {'first_name': first_name, 'is_staff_or_superuser': is_staff_or_superuser})

def custom_logout(request):
    logout(request)
    return redirect('login')



def traduzir(request):
    palavra = request.POST.get('palavra', '')
    traducao = ''
    if palavra:
        traducoes = {
            'carro': 'azul',
            'preto': 'aviao',
            'macaco': 'passaro'
            # Adicione mais traduções conforme necessário
        }
        traducao = traducoes.get(palavra, 'Palavra não encontrada')
    return render(request, 'sua_template.html', {'traducao': traducao})