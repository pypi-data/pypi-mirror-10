from django.contrib.sites.models import Site

# Separate function for Django 1.7 migrations
def get_current_site():
    return Site.objects.get_current()
