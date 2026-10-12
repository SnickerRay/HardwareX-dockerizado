# Pruebas de HardwareX

Las pruebas están hechas para el proyecto Django actual y usan `unittest`/`django.test`.

## Qué se prueba

- Registro de usuario:
  - campos obligatorios;
  - correo duplicado;
  - nombre de usuario duplicado;
  - guardado directo mediante `Usuario.objects.create`;
  - manejo de error de base de datos.
- Inicio de sesión:
  - formulario;
  - credenciales incorrectas;
  - credenciales correctas;
  - creación de sesión.
- Cierre de sesión.
- Consulta de perfil.
- Servicios de usuarios y equipos.
- Vista de equipos.
- Integración básica de las plantillas `login.html` y `equipos.html`.
- Animación del formulario de login/registro.
- Prueba TDD para detectar el problema actual del botón `Register`.

## Ejecutar

Desde `HardwareX/backend`:

```powershell
py manage.py test tests
```

O:

```powershell
python manage.py test tests
```

## Importante: prueba roja actual

`tests/test_frontend.py` contiene una prueba que debe fallar con el código actual:

```html
<button type="button" onclick="window.location.href='{% url 'inicio' %}'">Register</button>
```

Ese botón no envía el formulario a `apps.usuarios.views.RegisterView`.

Para que la prueba pase, el botón debe quedar así:

```html
<button type="submit">Register</button>
```

No hace falta `fetch` ni una API para el registro: el formulario puede hacer POST directamente a:

```text
/usuarios/register/
```

El backend ya contiene el `Usuario.objects.create(...)` que guarda directamente en la base de datos.
