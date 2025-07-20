# Estructura mínima tipo Laravel para despliegue en Hostinger

Esta es la estructura base para validar que tu hosting despliega correctamente un sitio tipo Laravel.

```
/ (raíz del repo)
├── app/
│   └── Http/
│       └── Controllers/
├── public/
│   └── index.php
├── resources/
│   └── views/
│       └── welcome.blade.php
├── routes/
│   └── web.php
```

- Sube todo el contenido a tu hosting.
- Apunta la carpeta pública de tu dominio a `/public`.
- Cuando instales Laravel con Composer, esta estructura se completará automáticamente.
