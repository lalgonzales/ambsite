# AMBSITE - Master Class SIG con IA

Landing page para la Master Class gratuita sobre Sistemas de Información Geográfica (SIG) con Inteligencia Artificial.

## 🚀 Características

- **Landing Page Moderna**: Diseño responsive y optimizado para conversiones
- **Sistema de Leads**: Captura y gestión de leads interesados
- **Privacidad Compliance**: Políticas de privacidad simples y técnicas que cumplen con GDPR
- **Analytics Integrado**: Google Analytics y Meta Pixel para seguimiento
- **Middleware de Privacidad**: Anonimización automática de datos sin consentimiento

## 🛠️ Tecnologías

- **Backend**: Django 5.2+
- **Base de Datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Frontend**: HTML5, CSS3, JavaScript
- **Testing**: Django TestCase + Coverage.py
- **Gestión de Dependencias**: uv

## 📦 Instalación

### Prerrequisitos

- Python 3.13+
- uv (gestor de paquetes)

### Instalación Rápida

```bash
# Clonar el repositorio
git clone <repository-url>
cd ambsite

# Instalar dependencias
uv sync

# Ejecutar migraciones
uv run python manage.py migrate

# Crear superusuario (opcional)
uv run python manage.py createsuperuser

# Ejecutar servidor de desarrollo
uv run python manage.py runserver
```

## 🧪 Testing

### Ejecutar Tests

```bash
# Todos los tests
uv run python manage.py test

# Tests con coverage
uv run coverage run manage.py test
uv run coverage report
uv run coverage html

# Tests específicos
uv run python manage.py test landings.tests.WebinarViewsTest
uv run python manage.py test landings.tests.IntegrationTest
```

### Cobertura de Tests

- **Cobertura Total**: 87%
- **Tests Activos**: 30+ tests
- **Módulos Testeados**:
  - ✅ Models (Analytics, Landings)
  - ✅ Views (Webinar, Privacy Policies)
  - ✅ Middleware (Cookie Consent, Data Retention)
  - ✅ Templates (Rendering, Context)
  - ✅ Integration (Flujos completos)

## 🔒 Privacidad y Compliance

### Políticas de Privacidad

- **Simple**: Versión amigable para usuarios (`/privacy-policy/`)
- **Técnica**: Detalles completos para compliance (`/privacy-policy-technical/`)

### Middleware de Privacidad

- Anonimización automática de IP sin consentimiento
- Headers de seguridad (HSTS, CSP, etc.)
- DNT (Do Not Track) cuando no hay consentimiento
- Cookies opcionales para analytics

## 📊 CI/CD

### GitHub Actions

El proyecto incluye un pipeline completo de CI/CD:

- **Tests Automáticos**: En cada push/PR
- **Coverage Reports**: Reportes HTML generados
- **Security Checks**: Verificación de dependencias
- **Linting**: Preparado para herramientas de linting

### Estados del Pipeline

- ✅ **Tests**: 30+ tests pasando
- ✅ **Coverage**: 87% cobertura
- ✅ **Security**: Checks básicos implementados
- 🔄 **Linting**: Configurado para futuras mejoras

## 🏗️ Arquitectura

```
ambsite/
├── analytics/          # App de leads y analytics
├── landings/           # App principal de landing pages
├── mysite/            # Configuración Django
├── templates/         # Templates base
├── static/            # Archivos estáticos
└── .github/workflows/ # CI/CD pipelines
```

## 📈 URLs Principales

- `/` - Home (redirect to webinar)
- `/webinar/` - Landing page principal
- `/webinar/thank-you/` - Página de agradecimiento
- `/privacy-policy/` - Política simple
- `/privacy-policy-technical/` - Política técnica
- `/admin/` - Panel de administración

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

- **Email**: privacidad@ambienteysig.com
- **Website**: [ambienteysig.com](https://ambienteysig.com)

---

**Última actualización**: November 2025
