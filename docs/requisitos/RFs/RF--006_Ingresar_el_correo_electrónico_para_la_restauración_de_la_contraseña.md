# RF-006 — Ingreso del correo para restaurar contraseña

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-006 |
| **Nombre** | Ingreso del correo para restaurar contraseña |
| **Módulo** | Autenticación |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir que el usuario ingrese su correo electrónico para solicitar un enlace que le permita recuperar el acceso a su cuenta.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Correo electrónico | Texto (correo) | Sí | Debe tener un formato válido y no superar 255 caracteres. |

---

## Proceso

1. El usuario selecciona la opción de recuperar contraseña.
2. El sistema muestra el formulario correspondiente.
3. El usuario ingresa su correo electrónico.
4. El backend valida el formato del correo.
5. Busca la cuenta asociada.
6. Si corresponde a una cuenta, genera un enlace seguro.
7. El sistema muestra un mensaje de confirmación.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Solicitud procesada | 200 | Se muestran instrucciones para recuperar la contraseña. |
| Correo inválido | 422 | El formato del correo no es válido. |
| Error interno | 500 | No fue posible procesar la solicitud. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/forgot-password` | No | Recibe el correo e inicia la recuperación. |

---

## Reglas de negocio

- **RN-001:** El correo debe tener un formato válido.
- **RN-002:** El sistema no debe revelar si una cuenta está registrada.
- **RN-003:** Las solicitudes de recuperación deben limitarse para evitar abusos.
- **RN-004:** El enlace debe ser seguro y tener vencimiento.
