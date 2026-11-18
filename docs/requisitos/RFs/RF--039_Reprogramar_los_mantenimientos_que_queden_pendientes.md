
# RF-039 — Reprogramación de mantenimientos pendientes

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-039 |
| **Nombre** | Reprogramación de mantenimientos pendientes |
| **Módulo** | Planificación de mantenimientos |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir modificar la fecha de los mantenimientos que continúen pendientes, facilitando la reorganización de las actividades cuando no puedan realizarse en la fecha inicialmente programada.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del mantenimiento | ID | Sí | Debe existir y estar pendiente. |
| Nueva fecha | Fecha/hora | Sí | Debe ser válida. |
| Motivo de reprogramación | Texto | No | Debe cumplir la longitud permitida. |
| Usuario responsable | ID | Sí | Debe tener autorización para modificar la programación. |

---

## Proceso

1. El usuario autorizado ingresa al módulo de mantenimientos.
2. Consulta los mantenimientos pendientes.
3. Selecciona el mantenimiento que necesita reprogramar.
4. Ingresa la nueva fecha.
5. Escribe el motivo del cambio si corresponde.
6. El sistema verifica que el mantenimiento siga pendiente.
7. Valida la nueva fecha y los permisos.
8. Guarda la modificación.
9. Actualiza la programación y los recordatorios asociados.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Reprogramación exitosa | 200 | Nueva fecha guardada correctamente. |
| Mantenimiento inexistente | 404 | No se encontró el mantenimiento. |
| Estado no permitido | 409 | El mantenimiento no puede reprogramarse. |
| Fecha inválida | 422 | La nueva fecha no es válida. |
| Sin autorización | 403 | No tiene permisos para reprogramar. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| PATCH | `/api/v1/preventive-maintenance/{id}/reschedule` | Sí | Modifica la fecha de un mantenimiento. |
| GET | `/api/v1/preventive-maintenance/pending` | Sí | Consulta los mantenimientos pendientes. |

---

## Reglas de negocio

- **RN-001:** Solo se pueden reprogramar mantenimientos pendientes.
- **RN-002:** La nueva fecha debe ser válida.
- **RN-003:** Cada cambio debe conservar la fecha anterior y la nueva.
- **RN-004:** La reprogramación debe actualizar los recordatorios correspondientes.
- **RN-005:** Solo los usuarios autorizados pueden modificar la programación.
