
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import OwnerProfile
from django.shortcuts import render
from django.shortcuts import render
from .models import HomeHero

from django.shortcuts import render, redirect, get_object_or_404
# from .models import HomeFeature
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import HomeCategory


def home(request):
    return render(request, 'home.html')

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
   


# def admin_dashboard(request):

#     if not request.user.is_authenticated:
#         return redirect('admin_login')

#     if not hasattr(request.user, 'adminprofile'):
#         return redirect('admin_login')

#     return render(
#         request,
#         'admin_panel/admin_dashboard.html'
#     )


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import AdminProfile, OwnerProfile
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import HomeCategory


def admin_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    # Total normal users
    total_users = User.objects.filter(
        adminprofile__isnull=True,
        ownerprofile__isnull=True
    ).count()

    # Total owners
    total_owners = OwnerProfile.objects.count()

    context = {
        'total_users': total_users,
        'total_owners': total_owners,
    }

    return render(
        request,
        'admin_panel/admin_dashboard.html',
        context
    )


def admin_logout(request):
    logout(request)
    return redirect('admin_login')

# Owner Profile Views



# =========================
# OWNER REGISTER
# =========================
def owner_register(request):

    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check password
        if password != confirm_password:
            return render(
                request,
                'owner_panel/owner_register.html',
                {'error': 'Passwords do not match.'}
            )

        # Check email
        if User.objects.filter(username=email).exists():
            return render(
                request,
                'owner_panel/owner_register.html',
                {'error': 'An account with this email already exists.'}
            )

        # Create User
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=full_name
        )

        # Create Owner Profile
        OwnerProfile.objects.create(
            user=user,
            phone=phone
        )

        return redirect('owner_login')

    return render(
        request,
        'owner_panel/owner_register.html'
    )


# =========================
# OWNER LOGIN
# =========================
def owner_login(request):

    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            # Check whether user is an Owner
            if hasattr(user, 'ownerprofile'):

                if not user.ownerprofile.is_active:
                    return render(
                        request,
                        'owner_panel/owner_login.html',
                        {'error': 'Your owner account is inactive.'}
                    )

                login(request, user)

                return redirect('owner_dashboard')

            else:
                return render(
                    request,
                    'owner_panel/owner_login.html',
                    {'error': 'This account is not registered as an owner.'}
                )

        else:
            return render(
                request,
                'owner_panel/owner_login.html',
                {'error': 'Invalid email or password.'}
            )

    return render(
        request,
        'owner_panel/owner_login.html'
    )


# =========================
# OWNER DASHBOARD
# =========================
def owner_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('owner_login')

    if not hasattr(request.user, 'ownerprofile'):
        return redirect('owner_login')

    return render(
        request,
        'owner_panel/owner_dashboard.html'
    )




# =========================
# OWNER LOGOUT
# =========================
def owner_logout(request):

    logout(request)

    return redirect('owner_login')

from django.shortcuts import render

from .models import (
    HomeHero,
    HomeCategory,
    HomeArea,
    HomeFeature,
    HomeAISection,
    HomeCTA,
    HomeContact
)




def home(request):

    hero = HomeHero.objects.filter(
        is_active=True
    ).first()
    categories = HomeCategory.objects.filter(
        is_active=True
    ).order_by('display_order')
    return render(
        request,
        'home.html',
        {
            'hero': hero,
            'categories': categories
        }
    )

from .models import HomeHero
def homepage_management(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    heroes = HomeHero.objects.all().order_by('-created_at')

    return render(
        request,
        'admin_panel/homepage_management.html',
        {
            'heroes': heroes
            
        }
    )
def add_hero(request):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    if request.method == 'POST':

        HomeHero.objects.create(
            badge=request.POST.get('badge'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            button_text=request.POST.get('button_text'),
            button_link=request.POST.get('button_link'),
            image=request.FILES.get('image'),
            is_active=request.POST.get('is_active') == 'on'
        )

    return redirect('homepage_management')

def edit_hero(request, id):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    hero = get_object_or_404(HomeHero, id=id)

    if request.method == 'POST':

        hero.badge = request.POST.get('badge')
        hero.title = request.POST.get('title')
        hero.description = request.POST.get('description')
        hero.button_text = request.POST.get('button_text')
        hero.button_link = request.POST.get('button_link')

        # Update image only if a new image is selected
        if request.FILES.get('image'):
            hero.image = request.FILES.get('image')

        hero.is_active = request.POST.get('is_active') == 'on'

        hero.save()

    return redirect('homepage_management')



def delete_hero(request, id):

    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    hero = get_object_or_404(HomeHero, id=id)

    if request.method == 'POST':
        hero.delete()

    return redirect('homepage_management')



# Homepage Category Management Views
def add_category(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()

        if not name:
            messages.error(request, 'Category name is required.')
            return redirect('homepage_management')

        if HomeCategory.objects.filter(name__iexact=name).exists():
            messages.error(request, 'Category already exists.')
            return redirect('homepage_management')

        HomeCategory.objects.create(
            name=name,
            description=request.POST.get('description', '').strip(),
            icon=request.POST.get('icon', '').strip()
                 or 'fa-solid fa-house',
            display_order=request.POST.get('display_order') or 0,
            is_active=request.POST.get('is_active') == 'on'
        )

        messages.success(request, 'Category added successfully.')

    return redirect('homepage_management')

def edit_category(request, id):
    # Check admin login
    if not request.user.is_authenticated:
        return redirect('admin_login')

    # Allow only users who have an adminprofile
    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    category = get_object_or_404(HomeCategory, id=id)

    # Update only through POST
    if request.method != 'POST':
        return redirect('homepage_management')

    name = request.POST.get('name', '').strip()
    description = request.POST.get('description', '').strip()
    icon = request.POST.get('icon', '').strip()
    display_order = request.POST.get('display_order', '0')

    if not name:
        messages.error(request, 'Category name is required.')
        return redirect('homepage_management')

    if HomeCategory.objects.filter(
        name__iexact=name
    ).exclude(id=id).exists():
        messages.error(request, 'Category already exists.')
        return redirect('homepage_management')

    try:
        display_order = int(display_order)
        if display_order < 0:
            raise ValueError
    except (ValueError, TypeError):
        messages.error(request, 'Enter a valid display order.')
        return redirect('homepage_management')

    category.name = name
    category.description = description
    category.icon = icon or 'fa-solid fa-house'
    category.display_order = display_order
    category.is_active = request.POST.get('is_active') == 'on'

    category.save()

    messages.success(request, 'Category updated successfully.')
    return redirect('homepage_management')


def delete_category(request, id):
    # Check admin login
    if not request.user.is_authenticated:
        return redirect('admin_login')

    # Allow only users who have an adminprofile
    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    # Prevent deletion through a normal GET request
    if request.method != 'POST':
        return redirect('homepage_management')

    category = get_object_or_404(HomeCategory, id=id)
    category.delete()

    messages.success(request, 'Category deleted successfully.')
    return redirect('homepage_management')