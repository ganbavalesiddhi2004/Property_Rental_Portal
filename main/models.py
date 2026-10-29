from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.utils import timezone


class AdminProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.user.username

# Owner Profile
class OwnerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=15
    )

    address = models.CharField(
        max_length=200,
        blank=True
    )

    is_approved = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    

    def __str__(self):
        return self.user.username


from django.db import models
from django.contrib.auth.models import User


class HomeHero(models.Model):

    badge = models.CharField(
        max_length=150,
        default="Smart Property Rental Platform"
    )

    title = models.CharField(
        max_length=200,
        default="Find Your Perfect Rental Property in Kolhapur"
    )

    description = models.TextField(
        blank=True
    )

    button_text = models.CharField(
        max_length=100,
        default="Explore Properties"
    )

    button_link = models.CharField(
        max_length=200,
        default="#properties"
    )

    image = models.ImageField(
        upload_to="homepage/hero/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title





class HomeArea(models.Model):

    name = models.CharField(
        max_length=100
    )

    icon = models.CharField(
        max_length=100,
        default="fa-solid fa-location-dot"
    )

    is_active = models.BooleanField(
        default=True
    )

    order = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        return self.name


class HomeFeature(models.Model):

    title = models.CharField(
        max_length=100
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        default="fa-solid fa-circle-check"
    )

    is_active = models.BooleanField(
        default=True
    )

    order = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        return self.title


class HomeAISection(models.Model):

    title = models.CharField(
        max_length=200,
        default="Find Properties with RentEase AI"
    )

    description = models.TextField()

    button_text = models.CharField(
        max_length=100,
        default="Try AI Property Search"
    )

    button_link = models.CharField(
        max_length=200,
        default="#"
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


class HomeCTA(models.Model):

    title = models.CharField(
        max_length=200,
        default="Ready to Find Your Next Home?"
    )

    description = models.TextField()

    button_text = models.CharField(
        max_length=100,
        default="Become an Owner"
    )

    button_link = models.CharField(
        max_length=200,
        default="#"
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title


class HomeContact(models.Model):

    location = models.CharField(
        max_length=200,
        default="Kolhapur, Maharashtra"
    )

    email = models.EmailField(
        default="support@renteaseai.com"
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.location    
# Home Category Model
from django.db import models
class HomeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.CharField(
        max_length=100,
        default="fa-solid fa-house"
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.name


# Home Feature Model

class WhyChooseFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(
        max_length=100,
        default="fa-solid fa-house"
    )
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.title

# Owner Dashboard Model
# Property Model
from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):

    CATEGORY_CHOICES = [
        ('Room', 'Room'),
        ('PG', 'PG'),
        ('1 BHK', '1 BHK'),
    ]

    FURNISHING_CHOICES = [
        ('Fully Furnished', 'Fully Furnished'),
        ('Semi Furnished', 'Semi Furnished'),
        ('Unfurnished', 'Unfurnished'),
    ]

    TENANT_CHOICES = [
        ('Any', 'Any'),
        ('Students', 'Students'),
        ('Working Professionals', 'Working Professionals'),
        ('Family', 'Family'),
        ('Girls', 'Girls'),
        ('Boys', 'Boys'),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rental_properties'
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    area = models.CharField(max_length=150)

    rent = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    furnishing = models.CharField(
        max_length=30,
        choices=FURNISHING_CHOICES,
        default='Unfurnished'
    )

    # Stores multiple amenities as a list
    amenities = models.JSONField(default=list, blank=True)

    parking = models.BooleanField(default=False)

    bedrooms = models.PositiveSmallIntegerField(
        default=0
    )

    bathrooms = models.PositiveSmallIntegerField(
        default=0
    )

    floor_number = models.IntegerField(
        default=0
    )

    available_from = models.DateField(
        null=True,
        blank=True
    )

    preferred_tenant = models.CharField(
        max_length=30,
        choices=TENANT_CHOICES,
        default='Any'
    )

    image = models.ImageField(
        upload_to='properties/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Booking Model

from django.conf import settings
from django.db import models


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    property = models.ForeignKey(
        'main.Property',
        on_delete=models.CASCADE,
        related_name='booking_requests'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='booking_requests'
    )
    booking_date = models.DateField()
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.property} - {self.status}"


# Review Model

from django.conf import settings
from django.db import models


class Review(models.Model):
    property = models.ForeignKey(
        'main.Property',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='property_reviews'
    )
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f'{i} Star') for i in range(1, 6)]
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property} - {self.rating} stars"


# Area Model
# ================= AVAILABLE AREA MODEL =================

class AvailableArea(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name