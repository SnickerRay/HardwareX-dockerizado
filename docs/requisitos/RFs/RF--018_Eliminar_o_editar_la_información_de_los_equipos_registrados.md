
# RF-018 — Edición y eliminación de equipos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-018 |
| **Nombre** | Edición y eliminación de equipos |
| **Módulo** | Gestión de equipos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir al administrador modificar la información de los equipos registrados o eliminarlos cuando sea necesario, conservando la integridad de los registros relacionados con sus mantenimientos.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del equipo | ID | Sí | Debe existir. |
| Nombre | Texto | Según operación | Longitud válida. |
| Marca | Texto | Según operación | No puede estar vacía. |
| Modelo | Texto | Según operación | No puede estar vacío. |
| Acción | Texto | Sí | Editar o eliminar. |

---

## Proceso

1. El administrador ingresa al módulo de equipos.
2. Busca y selecciona el equipo.
3. Selecciona la opción de editar o eliminar.
4. Si modifica los datos, el sistema valida la información.
5. Si solicita eliminarlo, verifica los registros relacionados.
6. Guarda los cambios o aplica la eliminación permitida.
7. Muestra el resultado de la operación.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Equipo actualizado | 200 | Información modificada correctamente. |
| Equipo eliminado | 200 | Equipo eliminado o desactivado. |
| Equipo inexistente | 404 | No se encontró el equipo. |
| Operación no permitida | 409 | El equipo tiene registros relacionados que impiden su eliminación. |
| Sin autorización | 403 | No tiene permisos suficientes. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| PUT | `/api/v1/equipment/{id}` | Sí | Modifica los datos del equipo. |
| DELETE | `/api/v1/equipment/{id}` | Sí | Elimina o desactiva un equipo. |

---

## Reglas de negocio

- **RN-001:** Solo el administrador puede editar o eliminar equipos.
- **RN-002:** El equipo debe existir.
- **RN-003:** No se deben perder los historiales de mantenimiento asociados.
- **RN-004:** Los cambios deben conservar la integridad de la base de datos.
