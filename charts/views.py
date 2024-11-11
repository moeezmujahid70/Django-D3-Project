from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView as DjangoLoginView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse

class LoginView(DjangoLoginView):
    template_name = 'charts/login.html'

@login_required
def sample_chart_view(request):
    # Example of dynamic data (could come from a database or API)
    labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    data = [12, 19, 3, 5, 2, 20]

    return render(request, 'charts/chart.html', {
        'labels': labels,
        'data': data
    })


@login_required
def generate_token_for_logged_in_user(request):
    user = request.user
    refresh = RefreshToken.for_user(user)
    return JsonResponse({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'email': user.email,
    })
