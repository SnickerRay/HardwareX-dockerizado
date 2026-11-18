# RF-007 — Verificación del login ingresado

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-007 |
| **Nombre** | Verificación del login ingresado |
| **Módulo** | Autenticación |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe verificar que el correo electrónico o identificador ingresado por el usuario corresponda a una cuenta registrada en Hardwarex antes de continuar con el proceso de autenticación.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Correo electrónico | Texto | Sí | Debe tener un formato válido. |
| Identificador del usuario | ID | Según implementación | Debe corresponder a una cuenta registrada. |

---

## Proceso

1. El usuario ingresa su identificador en el formulario.
2. El sistema recibe la información.
3. El backend consulta la base de datos.
4. Comprueba si existe una cuenta asociada.
5. Si la encuentra, continúa con la validación de la contraseña.
6. Si no existe, rechaza el inicio de sesión.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Usuario encontrado | 200 | Se continúa con la validación de credenciales. |
| Usuario no encontrado | 401 | Credenciales incorrectas. |
| Formato inválido | 422 | El identificador ingresado no es válido. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/login` | No | Verifica el identificador durante el inicio de sesión. |

---

## Reglas de negocio

- **RN-001:** El usuario debe tener una cuenta registrada.
- **RN-002:** La búsqueda debe realizarse mediante el identificador correspondiente.
- **RN-003:** No se debe revelar información privada de otras cuentas.
