from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if hasattr(user, 'adminprofile'):
                login(request, user)
                return redirect('admin_dashboard')

            else:
                return render(
                    request,
                    'admin_panel/admin_login.html',
                    {
                        'error': 'You are not authorized as Admin.'
                    }
                )

        else:
            return render(
                request,
                'admin_panel/admin_login.html',
                {
                    'error': 'Invalid username or password.'
                }
            )

    return render(
        request,
        'admin_panel/admin_login.html'
    )
   


def admin_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    return render(
        request,
        'admin_panel/admin_dashboard.html'
    )


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


