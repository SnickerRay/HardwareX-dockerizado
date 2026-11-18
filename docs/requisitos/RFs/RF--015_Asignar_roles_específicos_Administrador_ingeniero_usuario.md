
# RF-015 — Asignación de roles a usuarios

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-015 |
| **Nombre** | Asignación de roles a usuarios |
| **Módulo** | Gestión de usuarios y permisos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir al administrador asignar roles específicos a los usuarios, como administrador, ingeniero o usuario, para controlar las funciones y los módulos a los que pueden acceder.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del usuario | ID | Sí | Debe existir. |
| Rol | Texto o ID | Sí | Debe corresponder a un rol permitido. |

---

## Proceso

1. El administrador ingresa al módulo de usuarios.
2. Selecciona la cuenta que desea modificar.
3. Consulta los roles disponibles.
4. Selecciona el rol correspondiente.
5. El sistema verifica que el rol exista.
6. Guarda la asignación.
7. Actualiza los permisos del usuario.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Rol asignado | 200 | Rol actualizado correctamente. |
| Usuario inexistente | 404 | No se encontró el usuario. |
| Rol inválido | 422 | El rol seleccionado no es válido. |
| Sin permisos | 403 | No tiene autorización para asignar roles. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| PUT | `/api/v1/users/{id}/role` | Sí | Asigna o modifica el rol de un usuario. |
| GET | `/api/v1/roles` | Sí | Consulta los roles disponibles. |

---

## Reglas de negocio

- **RN-001:** Solo el administrador puede asignar roles.
- **RN-002:** Los roles permitidos son administrador, ingeniero y usuario.
- **RN-003:** Cada usuario debe tener un rol válido.
- **RN-004:** Los permisos deben actualizarse según el rol asignado.
