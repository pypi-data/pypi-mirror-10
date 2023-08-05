from django import forms
from django.db import models
from django.conf import settings

MAPS_API_KEY = 'AIzaSyAiRXVH2BsDZSaNucSVWWw7tO9LPRo5GEY'

class LocationPickerWidget(forms.TextInput):

    class Media:
        css = {
            'all': (
                settings.STATIC_URL + 'monocle_googlemap/monocle_googlemap.css',
            )
        }
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js',
            'http://www.google.com/jsapi?key=' + MAPS_API_KEY,
            settings.STATIC_URL + 'monocle_googlemap/monocle_googlemap.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(LocationPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        if None == attrs:
            attrs = {}
        attrs['class'] = 'location_picker'
        return super(LocationPickerWidget, self).render(name, value, attrs)

class LocationField(models.TextField):

    def formfield(self, **kwargs):
        kwargs['widget'] = LocationPickerWidget
        return super(LocationField, self).formfield(**kwargs)