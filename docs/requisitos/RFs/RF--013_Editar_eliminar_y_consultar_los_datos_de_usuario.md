
# RF-013 — Administración de usuarios

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-013 |
| **Nombre** | Administración de usuarios |
| **Módulo** | Gestión de usuarios |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir al administrador consultar, editar y eliminar o desactivar los datos de los usuarios registrados en Hardwarex, manteniendo organizada y actualizada la información de las cuentas.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del usuario | ID | Sí | Debe existir en el sistema. |
| Nombre completo | Texto | Según operación | Debe cumplir la longitud permitida. |
| Correo electrónico | Correo | Según operación | Debe ser válido y único. |
| Acción | Texto | Sí | Consultar, editar o eliminar. |

---

## Proceso

1. El administrador ingresa al módulo de usuarios.
2. El sistema muestra el listado de cuentas registradas.
3. El administrador selecciona un usuario.
4. Consulta, modifica o solicita eliminar la cuenta.
5. El sistema verifica los permisos.
6. Valida los datos modificados.
7. Guarda los cambios o ejecuta la operación permitida.
8. Muestra el resultado.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Consulta exitosa | 200 | Información del usuario. |
| Usuario actualizado | 200 | Datos modificados correctamente. |
| Usuario eliminado | 200 | Cuenta eliminada o desactivada. |
| Usuario inexistente | 404 | No se encontró el usuario. |
| Sin permisos | 403 | No tiene autorización para realizar la operación. |
| Datos inválidos | 422 | Errores de validación. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/users` | Sí | Consulta el listado de usuarios. |
| GET | `/api/v1/users/{id}` | Sí | Consulta un usuario específico. |
| PUT | `/api/v1/users/{id}` | Sí | Actualiza los datos de un usuario. |
| DELETE | `/api/v1/users/{id}` | Sí | Elimina o desactiva una cuenta. |

---

## Reglas de negocio

- **RN-001:** Solo el administrador puede gestionar las cuentas de otros usuarios.
- **RN-002:** El correo electrónico debe ser único.
- **RN-003:** No se deben eliminar registros que afecten el historial de actividades sin aplicar las restricciones correspondientes.
- **RN-004:** Los cambios deben conservar la integridad de la información.
