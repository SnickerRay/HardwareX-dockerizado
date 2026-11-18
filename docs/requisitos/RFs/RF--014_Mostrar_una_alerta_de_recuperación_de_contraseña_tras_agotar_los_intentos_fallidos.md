
# RF-014 — Alerta de recuperación de contraseña

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-014 |
| **Nombre** | Alerta de recuperación de contraseña |
| **Módulo** | Seguridad y autenticación |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe mostrar una alerta al usuario cuando agote los intentos permitidos de inicio de sesión, ofreciéndole la opción de iniciar el proceso de recuperación de contraseña.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Identificador del usuario | Texto | Sí | Debe tener un formato válido. |
| Contador de intentos | Número entero | Sí | Debe alcanzar el límite de tres intentos. |
| Acción de recuperación | Booleano | No | Indica si el usuario selecciona recuperar contraseña. |

---

## Proceso

1. El usuario realiza intentos fallidos de inicio de sesión.
2. El sistema actualiza el contador.
3. Al alcanzar tres intentos, muestra una alerta.
4. La alerta informa que se agotaron las oportunidades de acceso.
5. El usuario puede seleccionar la opción de recuperar contraseña.
6. El sistema lo dirige al formulario correspondiente.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Límite alcanzado | 429 | Alerta de intentos agotados. |
| Recuperación solicitada | 200 | Se muestra el formulario de recuperación. |
| Intentos disponibles | 401 | Mensaje de credenciales incorrectas. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/login` | No | Controla los intentos de acceso. |
| POST | `/api/v1/auth/forgot-password` | No | Inicia la recuperación de contraseña. |

---

## Reglas de negocio

- **RN-001:** La alerta debe mostrarse al alcanzar tres intentos fallidos.
- **RN-002:** La opción de recuperación debe estar disponible desde la alerta.
- **RN-003:** La recuperación debe seguir el procedimiento seguro establecido.
- **RN-004:** La alerta no debe revelar información privada de la cuenta.
