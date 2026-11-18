
# RF-024 — Notificación de solicitudes asignadas al ingeniero

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-024 |
| **Nombre** | Notificación de solicitudes asignadas al ingeniero |
| **Módulo** | Notificaciones y mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe generar una notificación para el ingeniero cuando el administrador le asigne una nueva solicitud de mantenimiento, permitiéndole conocer los trabajos que debe atender.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID de solicitud | ID | Sí | Debe existir y estar asignada. |
| ID del ingeniero | ID | Sí | Debe corresponder al responsable asignado. |
| Fecha de asignación | Fecha/hora | Sí | Generada por el sistema. |

---

## Proceso

1. El administrador asigna una solicitud de mantenimiento.
2. El sistema guarda la información de la asignación.
3. Identifica al ingeniero responsable.
4. Genera una notificación sobre la nueva solicitud.
5. Almacena la notificación.
6. El ingeniero puede consultar la notificación desde la plataforma.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Notificación generada | 201 | Notificación creada correctamente. |
| Solicitud inexistente | 404 | No se encontró la solicitud asignada. |
| Ingeniero inexistente | 404 | No se encontró el ingeniero. |
| Error de notificación | 500 | No fue posible generar la notificación. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/maintenance-requests/{id}/assign` | Sí | Realiza la asignación y genera la notificación. |
| GET | `/api/v1/notifications` | Sí | Consulta las notificaciones del usuario. |

---

## Reglas de negocio

- **RN-001:** La notificación debe dirigirse al ingeniero asignado.
- **RN-002:** Debe generarse después de confirmar la asignación.
- **RN-003:** La notificación debe relacionarse con la solicitud correspondiente.
- **RN-004:** Un error de notificación no debe eliminar la asignación.
