# RF-005 — Restauración de contraseña

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-005 |
| **Nombre** | Restauración de contraseña |
| **Módulo** | Autenticación |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir que los usuarios recuperen el acceso a su cuenta cuando olviden su contraseña, mediante un proceso seguro de restablecimiento.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Token de recuperación | Texto | Sí | Debe ser válido, vigente y no utilizado. |
| Nueva contraseña | Texto protegido | Sí | Debe cumplir los requisitos de seguridad. |
| Confirmación | Texto protegido | Sí | Debe coincidir con la nueva contraseña. |

---

## Proceso

1. El usuario selecciona la opción de recuperar contraseña.
2. El sistema genera un enlace de recuperación.
3. El usuario abre el enlace recibido.
4. Ingresa su nueva contraseña y la confirmación.
5. El backend verifica el token y los datos ingresados.
6. El sistema protege la nueva contraseña mediante hash.
7. Actualiza la contraseña de la cuenta.
8. Marca el token como utilizado.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Contraseña actualizada | 200 | Contraseña restablecida correctamente. |
| Token vencido | 400 | El enlace de recuperación ha expirado. |
| Token inválido | 400 | El enlace de recuperación no es válido. |
| Datos incorrectos | 422 | Las contraseñas no coinciden o no cumplen las validaciones. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/forgot-password` | No | Solicita el enlace de recuperación. |
| POST | `/api/v1/auth/reset-password` | No | Actualiza la contraseña mediante el token. |

---

## Reglas de negocio

- **RN-001:** El token debe tener un tiempo de vencimiento.
- **RN-002:** El token solo puede utilizarse una vez.
- **RN-003:** La nueva contraseña debe cumplir la política de seguridad.
- **RN-004:** La contraseña nunca debe enviarse por correo en texto plano.
