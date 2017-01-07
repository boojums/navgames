from django.conf import settings


def google_analytics(request):
    ''' Return data for Google Analytics tracking. '''
    ga_property_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
    ga_domain = getattr(settings, 'GOOGLE_ANALYTICS_DOMAIN', False)
    if not settings.DEBUG and ga_property_id and ga_domain:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': ga_property_id,
            'GOOGLE_ANALYTICS_DOMAIN': ga_domain,
        }
    return {}
