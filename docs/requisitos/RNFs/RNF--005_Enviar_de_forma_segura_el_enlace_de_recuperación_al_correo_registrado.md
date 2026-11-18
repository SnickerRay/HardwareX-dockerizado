
# RNF-005 — Seguridad en la recuperación de contraseñas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RNF-005 |
| **Nombre** | Seguridad en la recuperación de contraseñas |
| **Categoría** | Seguridad de la información |
| **Prioridad** | Alta |
| **Estado** | Por validar |

---

## Requisitos

### RNF-005.1 — Envío del enlace

El sistema debe enviar el enlace de recuperación de contraseña al correo electrónico registrado por el usuario.

### RNF-005.2 — Generación de token seguro

El enlace debe contener un token único y seguro que permita identificar la solicitud de recuperación.

### RNF-005.3 — Tiempo de expiración

El enlace de recuperación debe tener un tiempo de vencimiento establecido y no permitir su utilización después de expirar.

### RNF-005.4 — Uso único

El token de recuperación debe utilizarse una sola vez para evitar que otras personas puedan reutilizarlo.

### RNF-005.5 — Protección de la cuenta

El sistema no debe permitir cambiar la contraseña sin validar previamente el enlace de recuperación.
