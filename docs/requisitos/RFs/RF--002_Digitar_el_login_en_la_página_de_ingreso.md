# RF-002 — Ingreso de la contraseña

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-002 |
| **Nombre** | Ingreso de la contraseña |
| **Módulo** | Autenticación |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir que el usuario ingrese su contraseña en el formulario de inicio de sesión de Hardwarex, protegiendo los caracteres introducidos y validando posteriormente que coincidan con los datos registrados.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| password | Texto protegido | Sí | No puede estar vacío y debe coincidir con la contraseña registrada. |

---

## Proceso

1. El usuario ingresa al formulario de inicio de sesión.
2. Escribe su contraseña en el campo correspondiente.
3. El sistema oculta los caracteres introducidos.
4. El usuario selecciona la opción de ingresar.
5. El backend recibe la contraseña y realiza su validación segura.
6. El sistema informa si las credenciales son correctas.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Contraseña correcta | 200 | Contraseña validada correctamente. |
| Contraseña incorrecta | 401 | Mensaje de credenciales incorrectas. |
| Campo vacío | 422 | Mensaje indicando que la contraseña es obligatoria. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/login` | No | Valida las credenciales del usuario. |

---

## Reglas de negocio

- **RN-001:** La contraseña debe ingresarse obligatoriamente.
- **RN-002:** Los caracteres deben ocultarse por defecto.
- **RN-003:** La contraseña debe verificarse mediante un mecanismo seguro.
- **RN-004:** Las contraseñas no deben almacenarse en texto plano.
