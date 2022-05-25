from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    """User profile form to allow users to update their profile fields"""
    class Meta:
        """Get user data"""
        model = UserProfile
        fields = ('default_phone_number', 'default_street_address1', 'default_street_address2', 'default_town_or_city', 'default_county', 'default_postcode', 'default_country')
