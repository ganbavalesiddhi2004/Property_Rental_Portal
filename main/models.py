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



