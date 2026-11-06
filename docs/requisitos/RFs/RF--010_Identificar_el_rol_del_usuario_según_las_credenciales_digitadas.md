
# RF-010 — Identificación del rol del usuario

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-010 |
| **Nombre** | Identificación del rol del usuario |
| **Módulo** | Gestión de roles y permisos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe identificar el rol asignado al usuario después de validar sus credenciales, para determinar las funcionalidades y los permisos disponibles dentro de Hardwarex.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Correo electrónico | Texto | Sí | Debe corresponder a una cuenta registrada. |
| Contraseña | Texto protegido | Sí | Debe ser válida. |
| Rol asignado | Texto o ID | Sí | Debe ser un rol permitido. |

---

## Proceso

1. El usuario ingresa sus credenciales.
2. El sistema valida el correo y la contraseña.
3. Consulta el rol asociado a la cuenta.
4. Comprueba los permisos correspondientes.
5. Identifica las funciones disponibles.
6. Permite el acceso a las opciones autorizadas.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Rol identificado | 200 | Se obtiene el rol y sus permisos. |
| Rol inexistente | 403 | El usuario no tiene un rol válido para acceder. |
| Credenciales incorrectas | 401 | No fue posible autenticar al usuario. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/auth/me` | Sí | Consulta la información y el rol del usuario autenticado. |
| GET | `/api/v1/roles` | Sí | Consulta los roles disponibles según permisos. |

---

## Reglas de negocio

- **RN-001:** Los roles permitidos son administrador, ingeniero y usuario.
- **RN-002:** Cada cuenta debe tener un rol asignado.
- **RN-003:** Los permisos deben aplicarse tanto en la interfaz como en el backend.
- **RN-004:** El usuario no puede modificar sus propios permisos sin autorización.
