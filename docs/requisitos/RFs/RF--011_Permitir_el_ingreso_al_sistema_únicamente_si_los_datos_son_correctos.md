
# RF-011 — Validación de acceso al sistema

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-011 |
| **Nombre** | Validación de acceso al sistema |
| **Módulo** | Autenticación |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir el ingreso a la plataforma únicamente cuando el usuario proporcione credenciales correctas y su cuenta cumpla con las condiciones de acceso establecidas.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Correo electrónico | Texto | Sí | Debe estar registrado. |
| Contraseña | Texto protegido | Sí | Debe coincidir con la registrada. |
| Estado de cuenta | Booleano | Sí | La cuenta debe estar habilitada. |

---

## Proceso

1. El usuario ingresa sus credenciales.
2. El sistema verifica el correo electrónico.
3. Comprueba la contraseña.
4. Consulta el estado de la cuenta.
5. Si los datos son correctos, inicia la sesión.
6. Si existe algún error, rechaza el acceso.
7. Muestra el resultado del proceso.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Acceso permitido | 200 | Sesión iniciada correctamente. |
| Credenciales incorrectas | 401 | Acceso rechazado por datos incorrectos. |
| Cuenta deshabilitada | 403 | La cuenta no está habilitada. |
| Datos incompletos | 422 | Se deben completar los campos obligatorios. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/login` | No | Valida las credenciales e inicia sesión. |

---

## Reglas de negocio

- **RN-001:** Solo las credenciales correctas permiten ingresar.
- **RN-002:** Las cuentas deshabilitadas no pueden iniciar sesión.
- **RN-003:** El acceso debe estar protegido mediante autenticación.
- **RN-004:** Los permisos dependen del rol asignado.
