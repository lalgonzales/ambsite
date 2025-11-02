"""
Middleware para manejar consentimiento de cookies y privacidad
"""
from django.utils.deprecation import MiddlewareMixin


class CookieConsentMiddleware(MiddlewareMixin):
    """
    Middleware que maneja el consentimiento de cookies y anonimiza datos
    cuando el usuario no ha dado consentimiento.
    """

    def process_request(self, request):
        """
        Procesa la solicitud para verificar consentimiento de cookies
        """
        # Verificar si el usuario ha dado consentimiento
        cookie_consent = request.COOKIES.get('cookie-consent') or \
                        getattr(request, 'session', {}).get('cookie-consent')

        analytics_consent = request.COOKIES.get('analytics-consent') or \
                           getattr(request, 'session', {}).get('analytics-consent')

        marketing_consent = request.COOKIES.get('marketing-consent') or \
                           getattr(request, 'session', {}).get('marketing-consent')

        # Agregar información de consentimiento al request
        request.cookie_consent = {
            'has_consent': cookie_consent == 'accepted',
            'analytics': analytics_consent == 'true',
            'marketing': marketing_consent == 'true',
        }

        # Si no hay consentimiento, anonimizar datos sensibles
        if not request.cookie_consent['has_consent']:
            # Anonimizar IP
            if hasattr(request, 'META'):
                original_ip = request.META.get('REMOTE_ADDR', '')
                if original_ip:
                    # Técnica simple de anonimización: mantener solo primeros 2 octetos
                    ip_parts = original_ip.split('.')
                    if len(ip_parts) == 4:
                        request.META['REMOTE_ADDR'] = f"{ip_parts[0]}.{ip_parts[1]}.0.0"

            # Limpiar user agent para análisis
            if hasattr(request, 'META') and 'HTTP_USER_AGENT' in request.META:
                # Solo mantener información básica del navegador
                ua = request.META['HTTP_USER_AGENT']
                if 'Chrome' in ua:
                    request.META['HTTP_USER_AGENT'] = 'Chrome (Anonimizado)'
                elif 'Firefox' in ua:
                    request.META['HTTP_USER_AGENT'] = 'Firefox (Anonimizado)'
                elif 'Safari' in ua:
                    request.META['HTTP_USER_AGENT'] = 'Safari (Anonimizado)'
                else:
                    request.META['HTTP_USER_AGENT'] = 'Browser (Anonimizado)'

    def process_response(self, request, response):
        """
        Procesa la respuesta para agregar headers de privacidad
        """
        # Agregar headers de privacidad recomendados
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'

        # Si no hay consentimiento, agregar header de no-track
        if hasattr(request, 'cookie_consent') and not request.cookie_consent['has_consent']:
            response['DNT'] = '1'  # Do Not Track

        return response


class DataRetentionMiddleware(MiddlewareMixin):
    """
    Middleware que marca datos para eliminación automática según políticas
    """

    def process_request(self, request):
        """
        Verifica si hay solicitudes de eliminación de datos
        """
        # Aquí podríamos agregar lógica para procesar solicitudes GDPR
        # Por ejemplo, verificar tokens de eliminación en la URL
        pass