
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
# Add with your other imports
from .models import Property, Review

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
    properties = Property.objects.filter(
        owner=request.user
    ).order_by('-id')

    context = {
        'properties': properties,
        'total_properties': properties.count(),
        'booking_requests': 0,  # Replace with your booking count when available.
    }
    return render(
        request,
        'owner_panel/owner_dashboard.html',
        context
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
    categories = HomeCategory.objects.all().order_by('display_order')
    why_choose_features = WhyChooseFeature.objects.all()
    return render(
        request,
        'admin_panel/homepage_management.html',
        {
            'heroes': heroes,
            'categories': categories,
            'why_choose_features': why_choose_features,
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


from .models import WhyChooseFeature

def add_why_choose_feature(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    if request.method != 'POST':
        return redirect('homepage_management')

    title = request.POST.get('title', '').strip()
    description = request.POST.get('description', '').strip()
    icon = request.POST.get('icon', '').strip()
    display_order = request.POST.get('display_order', '0')

    if not title or not description:
        messages.error(request, 'Title and description are required.')
        return redirect('homepage_management')

    try:
        display_order = int(display_order)
        if display_order < 0:
            raise ValueError
    except (ValueError, TypeError):
        messages.error(request, 'Enter a valid display order.')
        return redirect('homepage_management')

    WhyChooseFeature.objects.create(
        title=title,
        description=description,
        icon=icon or 'fa-solid fa-house',
        display_order=display_order,
        is_active=request.POST.get('is_active') == 'on'
    )

    messages.success(request, 'Feature added successfully.')
    return redirect('homepage_management')


def edit_why_choose_feature(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    feature = get_object_or_404(WhyChooseFeature, id=id)

    if request.method != 'POST':
        return redirect('homepage_management')

    title = request.POST.get('title', '').strip()
    description = request.POST.get('description', '').strip()
    icon = request.POST.get('icon', '').strip()
    display_order = request.POST.get('display_order', '0')

    if not title or not description:
        messages.error(request, 'Title and description are required.')
        return redirect('homepage_management')

    try:
        display_order = int(display_order)
        if display_order < 0:
            raise ValueError
    except (ValueError, TypeError):
        messages.error(request, 'Enter a valid display order.')
        return redirect('homepage_management')

    feature.title = title
    feature.description = description
    feature.icon = icon or 'fa-solid fa-house'
    feature.display_order = display_order
    feature.is_active = request.POST.get('is_active') == 'on'
    feature.save()

    messages.success(request, 'Feature updated successfully.')
    return redirect('homepage_management')


def delete_why_choose_feature(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if not hasattr(request.user, 'adminprofile'):
        return redirect('admin_login')

    if request.method != 'POST':
        return redirect('homepage_management')

    feature = get_object_or_404(WhyChooseFeature, id=id)
    feature.delete()

    messages.success(request, 'Feature deleted successfully.')
    return redirect('homepage_management')

# Property Management Views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Property


@login_required
def add_property(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        area = request.POST.get('area', '').strip()
        rent = request.POST.get('rent')
        image = request.FILES.get('image')

        if not all([category, title, description, area, rent]):
            messages.error(request, 'Please fill in all required fields.')
            return redirect('add_property')

        try:
            rent = float(rent)
            if rent <= 0:
                raise ValueError
        except (ValueError, TypeError):
            messages.error(request, 'Enter a valid rent amount.')
            return redirect('add_property')

        Property.objects.create(
            owner=request.user,
            category=category,
            title=title,
            description=description,
            area=area,
            rent=rent,
            image=image
        )

        messages.success(request, 'Property added successfully!')
        return redirect('owner_dashboard')

    return render(request, 'owner_panel/add_property.html')


@login_required
def my_properties(request):
    properties = Property.objects.filter(
        owner=request.user
    ).order_by('-created_at')

    return render(
        request,
        'owner_panel/my_properties.html',
        {'properties': properties}
    )
# myproperties edit and delete views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Property


@login_required
def edit_property(request, property_id):
    property_obj = get_object_or_404(
        Property,
        id=property_id,
        owner=request.user
    )

    if request.method == 'POST':
        property_obj.category = request.POST.get('category')
        property_obj.title = request.POST.get('title')
        property_obj.description = request.POST.get('description')
        property_obj.area = request.POST.get('area')
        property_obj.rent = request.POST.get('rent')

        if request.FILES.get('image'):
            property_obj.image = request.FILES['image']

        property_obj.save()

        messages.success(request, 'Property updated successfully.')
        return redirect('owner_dashboard')

    return render(
        request,
        'owner_panel/edit_property.html',
        {'property': property_obj}
    )


@login_required
def delete_property(request, property_id):
    if request.method == 'POST':
        property_obj = get_object_or_404(
            Property,
            id=property_id,
            owner=request.user
        )

        property_obj.delete()
        messages.success(request, 'Property deleted successfully.')

    return redirect('owner_dashboard')

# My Profile View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

User = get_user_model()


@login_required
def edit_owner_profile(request):
    if request.method == 'POST':
        user = request.user

        if getattr(user, 'role', '') != 'OWNER':
            messages.error(request, 'Only owners can edit this profile.')
            return redirect('owner_dashboard')

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()

        if password:
            user.set_password(password)

        if User.objects.filter(username=username).exclude(pk=user.pk).exists():
            messages.error(request, 'This username is already taken.')
            return redirect('/owner-dashboard/#edit-profile-section')

        if User.objects.filter(email=email).exclude(pk=user.pk).exists():
            messages.error(request, 'This email is already in use.')
            return redirect('/owner-dashboard/#edit-profile-section')

        user.username = username
        user.password = password if password else user.password
        user.email = email
        user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('owner_dashboard')

    return redirect('owner_dashboard')


@login_required
def delete_owner_profile(request):
    if request.method != 'POST':
        return redirect('owner_dashboard')

    user = request.user

    if getattr(user, 'role', '') != 'OWNER':
        messages.error(request, 'Only owners can delete this profile.')
        return redirect('owner_dashboard')

    logout(request)
    user.delete()

    messages.success(request, 'Your profile has been deleted.')
    return redirect('owner_login')



# User Registration View

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Property

def user_register(request):
    category = request.GET.get('category', '')

    if request.method == 'POST':
        category = request.POST.get('category', '')
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'user_panel/user_register.html',
                          {'category': category})

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'user_panel/user_register.html',
                          {'category': category})

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'user_panel/user_register.html',
                          {'category': category})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Remember the selected category until after login.
        request.session['selected_category'] = category

        messages.success(request, 'Registration successful. Please log in.')
        return redirect('user_login')

    return render(request, 'user_panel/user_register.html',
                  {'category': category})


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', '').strip()
#         password = request.POST.get('password', '')
#         category = request.POST.get('category', '')

#         user = authenticate(
#             request,
#             username=username,
#             password=password
#         )

#         if user is not None:
#             if not user.is_active:
#                 messages.error(request, 'Your account is inactive.')
#                 return redirect('user_login')

#             login(request, user)

#             # Use the category saved during registration if available.
#             category = request.session.pop(
#                 'selected_category', category
#             )

#             property_url = reverse('property_list')

#             if category:
#                 return redirect(
#                     f'{property_url}?category={category}'
#                 )

#             return redirect('property_list')

#         messages.error(request, 'Invalid username or password.')

#     category = request.session.get('selected_category', '')
#     return render(request, 'user_panel/user_login.html',
#                   {'category': category})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        category = request.POST.get('category', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            if not user.is_active:
                messages.error(
                    request,
                    'Your account is inactive.'
                )
                return redirect('user_login')

            login(request, user)

            # Preserve the selected category for the dashboard.
            if category:
                request.session['selected_category'] = category

            # Redirect to the logged-in user's dashboard.
            return redirect('user_dashboard')

        messages.error(
            request,
            'Invalid username or password.'
        )

    category = request.session.get('selected_category', '')

    return render(
        request,
        'user_panel/user_login.html',
        {'category': category}
    )


@login_required
def property_list(request):
    category = request.GET.get(
        'category',
        request.session.get('selected_category', '')
    )

    properties = Property.objects.filter(
        is_approved=True,
        is_available=True
    )

    if category:
        properties = properties.filter(property_type__iexact=category)

    return render(request, 'user_panel/user_properties.html', {
        'properties': properties,
        'category': category
    })


def user_logout(request):
    logout(request)
    return redirect('home')


# user dashboard view


from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@login_required
def user_dashboard(request):
    section = request.GET.get('section', 'dashboard')

    allowed_sections = [
        'dashboard',
        'profile',
        'properties',
        'bookings',
        'reviews',
    ]

    if section not in allowed_sections:
        section = 'dashboard'

    user = request.user

    # Redirect back to the Profile section after form submission.
    profile_url = reverse('user_dashboard') + '?section=profile'

    if request.method == 'POST':
        action = request.POST.get('action')

        # EDIT PROFILE
        if action == 'edit_profile':
            username = request.POST.get('username', '').strip()
            first_name = request.POST.get('first_name', '').strip()
            last_name = request.POST.get('last_name', '').strip()
            email = request.POST.get('email', '').strip()

            if not username:
                messages.error(request, 'Username cannot be empty.')

            elif User.objects.filter(
                username=username
            ).exclude(pk=user.pk).exists():
                messages.error(request, 'This username is already taken.')

            elif email and User.objects.filter(
                email=email
            ).exclude(pk=user.pk).exists():
                messages.error(request, 'This email is already registered.')

            else:
                user.username = username
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()

                messages.success(
                    request,
                    'Profile updated successfully.'
                )

            return redirect(profile_url)

        # CHANGE PASSWORD
        elif action == 'change_password':
            old_password = request.POST.get('old_password', '')
            new_password = request.POST.get('new_password', '')
            confirm_password = request.POST.get('confirm_password', '')

            if not user.check_password(old_password):
                messages.error(
                    request,
                    'Your current password is incorrect.'
                )

            elif new_password != confirm_password:
                messages.error(
                    request,
                    'New passwords do not match.'
                )

            else:
                try:
                    validate_password(new_password, user=user)

                    user.set_password(new_password)
                    user.save()

                    # Keep the user logged in after changing the password.
                    update_session_auth_hash(request, user)

                    messages.success(
                        request,
                        'Password changed successfully.'
                    )

                except ValidationError as error:
                    for error_message in error.messages:
                        messages.error(request, error_message)

            return redirect(profile_url)

        # DELETE ACCOUNT
        elif action == 'delete_account':
            password = request.POST.get('delete_password', '')

            if not user.check_password(password):
                messages.error(
                    request,
                    'Incorrect password. Your account was not deleted.'
                )
                return redirect(profile_url)

            # Log out and delete the account.
            logout(request)
            user.delete()
            request.session.flush()

            return redirect('user_login')
    recent_properties = Property.objects.all().order_by('-id')
    context = {
        'section': section,
        'user': user,
        'total_properties': Property.objects.count(),
        'total_bookings': 0,
        'total_reviews': 0,
        'recent_properties': recent_properties,
    }

    return render(
        request,
        'user_panel/user_dashboard.html',
        context
    )



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def user_profile(request):
    return render(
        request,
        'user_panel/user_profile.html',
        {'user': request.user}
    )
