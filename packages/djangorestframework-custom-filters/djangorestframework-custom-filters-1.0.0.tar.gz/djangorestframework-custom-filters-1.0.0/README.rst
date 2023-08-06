django-rest-framework-custom-filters
====================================

Custom filters for django rest framework

Compatibility
-------------

work with :
 * Python 2.7 / 3.4
 * Dango 1.6 / 1.7
 * Django Rest Framework 2.4 / 3.0

Installation
------------

Install the package from pypi: ::

    pip install djangorestframework-custom-filters

Add the application in your django settings: ::

    DJANGO_APPS = ('rest_framework_custom_filters',)
    
Usage
-----

Use it in your filters.py : ::

    import django_filters
    import rest_framework_custom_filters

    class MyFilter(django_filters.FilterSet):
        since = rest_framework_custom_filters.IsoDateTimeFilter(name='_per_modif', lookup_type='gte')
        ...
