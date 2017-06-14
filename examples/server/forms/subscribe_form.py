# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# start tutorial
from django import forms
from django.core.exceptions import ValidationError
from djng.forms.fields import FloatField
from djng.styling.bootstrap3.forms import Bootstrap3Form


def validate_password(value):
    # Just for demo. Do not validate passwords like this!
    if value != 'secret':
        raise ValidationError('The password is wrong.')


class SubscribeForm(Bootstrap3Form):
    use_required_attribute = False

    CONTINENT_CHOICES = (('am', 'America'), ('eu', 'Europe'), ('as', 'Asia'), ('af', 'Africa'),
                         ('au', 'Australia'), ('oc', 'Oceania'), ('an', 'Antartica'),)
    TRAVELLING_BY = (('foot', 'Foot'), ('bike', 'Bike'), ('mc', 'Motorcycle'), ('car', 'Car'),
                     ('public', 'Public Transportation'), ('train', 'Train'), ('air', 'Airplane'),)
    NOTIFY_BY = (('email', 'EMail'), ('phone', 'Phone'), ('sms', 'SMS'), ('postal', 'Postcard'),)

    first_name = forms.CharField(label='First name', min_length=3, max_length=20)

    last_name = forms.RegexField(
        r'^[A-Z][a-z -]?',
        label='Last name',
        error_messages={'invalid': 'Last names shall start in upper case'})

    sex = forms.ChoiceField(
        choices=(('m', 'Male'), ('f', 'Female')),
        widget=forms.RadioSelect,
        error_messages={'invalid_choice': 'Please select your sex'})

    email = forms.EmailField(
        label='E-Mail',
        required=True,
        help_text='Please enter a valid email address')

    subscribe = forms.BooleanField(
        label='Subscribe Newsletter',
        initial=False, required=False)

    phone = forms.RegexField(
        r'^\+?[0-9 .-]{4,25}$',
        label='Phone number',
        error_messages={'invalid': 'Phone number have 4-25 digits and may start with +'})

    birth_date = forms.DateField(
        label='Date of birth',
        widget=forms.DateInput(attrs={'validate-date': '^(\d{4})-(\d{1,2})-(\d{1,2})$'}),
        help_text='Allowed date format: yyyy-mm-dd')

    continent = forms.ChoiceField(
        label='Living on continent',
        choices=CONTINENT_CHOICES,
        error_messages={'invalid_choice': 'Please select your continent'})

    weight = forms.IntegerField(
        label='Weight in kg',
        min_value=42,
        max_value=95,
        error_messages={'min_value': 'You are too lightweight'})

    height = FloatField(
        label='Height in meters',
        min_value=1.48,
        max_value=1.95,
        step=0.05,
        error_messages={'max_value': 'You are too tall'})

    traveling = forms.MultipleChoiceField(
        label='Traveling by',
        choices=TRAVELLING_BY,
        help_text='Choose one or more carriers',
        required=True)

    notifyme = forms.MultipleChoiceField(
        label='Notify by',
        choices=NOTIFY_BY,
        widget=forms.CheckboxSelectMultiple, required=True,
        help_text='Must choose at least one type of notification')

    annotation = forms.CharField(
        label='Annotation',
        required=True,
        widget=forms.Textarea(attrs={'cols': '80', 'rows': '3'}))

    agree = forms.BooleanField(
        label='Agree with our terms and conditions',
        initial=False,
        required=True)

    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput,
        validators=[validate_password],
        help_text='The password is "secret"')

    confirmation_key = forms.CharField(
        max_length=40,
        required=True,
        widget=forms.HiddenInput(),
        initial='hidden value')
