from django import template

from dashboard.models import UserAttribute

register = template.Library()


@register.filter
def ratio(downloads, user):
    uploads = UserAttribute.objects.get(user=user).uploads
    return f"{uploads / downloads:.1f}" if downloads != 0 else "N/A"

@register.filter
def badge(uploads):
    if uploads <= 5:
        return "Newbie"
    elif uploads <= 10:
        return "Member"
    elif uploads <= 15:
        return "Regular"
    elif uploads <= 20:
        return "Elite"
    elif uploads <= 25:
        return "Supreme"
    else:
        return "Wizard"
