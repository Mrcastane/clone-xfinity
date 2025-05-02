from django import forms

class UserPassForm(forms.Form):
    user_name = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={
            'placeholder': 'Email, mobile or username',
            'class': 'form-control'
        })
    )
    pass_word = forms.CharField(
        max_length=100,
        label="",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control'
        })
    )


class BillingForm(forms.Form):
    card_name = forms.CharField(
        max_length=100,
        label="Name on Card",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name as on card'
        })
    )
    card_number = forms.CharField(
        max_length=19,
        label="Card Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'type': 'tel',
            'inputmode': 'numeric',
            'placeholder': '1234 5678 9012 3456'
        })
    )
    expiry_date = forms.CharField(
        label="Expiry Date",
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM/YY',
            'type': 'month'  # Use 'month' if your browser supports it
        })
    )
    cvv = forms.CharField(
        max_length=3,
        label="CVV",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'CVV',
            'type': 'tel',
            'inputmode': 'numeric'
        })
    )
    address = forms.CharField(
        max_length=100,
        label="Billing Address and Zip Code",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Street, City, Zip'
        })
    )


class InfoForm(forms.Form):
    ssn = forms.CharField(
        max_length=100,
        label="Social Security Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '123-45-6789',
            'inputmode': 'numeric'
        })
    )
    dob = forms.CharField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={
            'placeholder': 'MM/DD/YYYY',
            'class': 'form-control',
            'type': 'date'
        })
    )
    postal_code = forms.CharField(
        max_length=100,
        label="Postal Code",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. 10001',
            'inputmode': 'numeric'
        })
    )
    phone_number = forms.CharField(
        max_length=100,
        label="Phone Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. +1 555 123 4567',
            'type': 'tel',
            'inputmode': 'tel'
        })
    )
