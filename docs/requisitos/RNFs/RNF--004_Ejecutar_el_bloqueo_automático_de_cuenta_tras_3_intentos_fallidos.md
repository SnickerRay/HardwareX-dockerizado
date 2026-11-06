
# RNF-004 — Bloqueo automático de cuentas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RNF-004 |
| **Nombre** | Bloqueo automático de cuentas |
| **Categoría** | Seguridad de la información |
| **Prioridad** | Crítica |
| **Estado** | Por validar |

---

## Requisitos

### RNF-004.1 — Control de intentos

El sistema debe contar los intentos fallidos de inicio de sesión realizados por cada usuario.

### RNF-004.2 — Bloqueo automático

Después de tres intentos consecutivos con credenciales incorrectas, Hardwarex debe bloquear temporalmente la cuenta.

### RNF-004.3 — Mensaje de bloqueo

El sistema debe mostrar un mensaje informando que la cuenta ha sido bloqueada temporalmente por superar el número de intentos permitidos.

### RNF-004.4 — Restablecimiento del acceso

El sistema debe permitir recuperar el acceso mediante un procedimiento seguro de desbloqueo.

### RNF-004.5 — Registro de intentos

Hardwarex debe almacenar los intentos fallidos para facilitar el seguimiento de posibles accesos no autorizados.
