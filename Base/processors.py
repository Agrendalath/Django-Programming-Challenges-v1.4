from django.conf import settings


# noinspection PyUnusedLocal
def site_name(request):
    return {'site_name': settings.SITE_NAME}
