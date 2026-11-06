
# RF-026 — Actualización del estado del mantenimiento

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-026 |
| **Nombre** | Actualización del estado del mantenimiento |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir que el ingeniero actualice el estado de las solicitudes de mantenimiento, indicando si se encuentran pendientes, en proceso o finalizadas, para facilitar el seguimiento de las actividades realizadas.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del mantenimiento | ID | Sí | Debe existir. |
| Estado | Texto | Sí | Pendiente, en proceso o finalizado. |
| Observaciones | Texto | No | Deben corresponder al mantenimiento. |
| Fecha de actualización | Fecha/hora | Sí | Generada por el sistema. |

---

## Proceso

1. El ingeniero ingresa al módulo de mantenimientos.
2. Selecciona una solicitud asignada.
3. Consulta el estado actual.
4. Selecciona el nuevo estado.
5. Agrega observaciones si es necesario.
6. El sistema valida los datos y los permisos.
7. Guarda la actualización.
8. Actualiza el historial del mantenimiento.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Estado actualizado | 200 | Mantenimiento actualizado correctamente. |
| Mantenimiento inexistente | 404 | No se encontró la solicitud. |
| Estado inválido | 422 | El estado seleccionado no es válido. |
| Sin autorización | 403 | No tiene permisos para modificar el estado. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| PATCH | `/api/v1/maintenance-requests/{id}/status` | Sí | Actualiza el estado del mantenimiento. |

---

## Reglas de negocio

- **RN-001:** Solo los usuarios autorizados pueden actualizar el estado.
- **RN-002:** Los estados permitidos son pendiente, en proceso y finalizado.
- **RN-003:** Cada actualización debe conservar la fecha y el responsable.
- **RN-004:** El historial debe reflejar los cambios realizados.
