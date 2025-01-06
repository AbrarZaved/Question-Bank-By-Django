from django import template

from dashboard.models import UserAttribute

register = template.Library()


@register.filter
def ratio(downloads, user):
    uploads = UserAttribute.objects.get(user=user).uploads
    return uploads / downloads if downloads != 0 else "N/A"
