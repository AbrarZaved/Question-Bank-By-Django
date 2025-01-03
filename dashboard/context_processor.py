from dashboard.models import UserAttribute


def AttributeSetup(request):
    user = request.user
    print(user)
    uploads = 0
    downloads = 0
    try:
        if UserAttribute.objects.filter(user=user).exists():
            user_attribute = UserAttribute.objects.get(user=user)
            uploads = user_attribute.uploads
            downloads = user_attribute.downloads 
    except TypeError:
        pass

    return {"uploads": uploads, "downloads": downloads}
