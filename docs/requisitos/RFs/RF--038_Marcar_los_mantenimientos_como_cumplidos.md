
# RF-038 — Registro de mantenimientos cumplidos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-038 |
| **Nombre** | Registro de mantenimientos cumplidos |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir que los usuarios autorizados marquen como cumplidos los mantenimientos preventivos que hayan sido realizados, actualizando su estado y conservando la información de las actividades ejecutadas.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del mantenimiento | ID | Sí | Debe existir. |
| Estado | Texto | Sí | Debe permitir el estado cumplido. |
| Fecha de realización | Fecha/hora | Sí | Debe ser válida. |
| Observaciones | Texto | No | Deben corresponder a las actividades realizadas. |
| Responsable | ID | Sí | Debe ser un usuario autorizado. |

---

## Proceso

1. El responsable ingresa al módulo de mantenimientos.
2. Consulta los mantenimientos pendientes o en proceso.
3. Selecciona el mantenimiento que ya fue realizado.
4. Registra la fecha de ejecución.
5. Agrega observaciones sobre las actividades realizadas.
6. El sistema valida los datos y los permisos.
7. Actualiza el estado a cumplido.
8. Guarda la información en el historial de mantenimiento.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Mantenimiento cumplido | 200 | Estado actualizado correctamente. |
| Mantenimiento inexistente | 404 | No se encontró el mantenimiento. |
| Estado no permitido | 422 | No es posible realizar esta actualización. |
| Sin autorización | 403 | No tiene permisos para marcar el mantenimiento. |
| Error de actualización | 500 | No fue posible actualizar el registro. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| PATCH | `/api/v1/preventive-maintenance/{id}/complete` | Sí | Marca un mantenimiento como cumplido. |
| GET | `/api/v1/preventive-maintenance/{id}` | Sí | Consulta los detalles del mantenimiento. |

---

## Reglas de negocio

- **RN-001:** El mantenimiento debe estar registrado.
- **RN-002:** Solo los usuarios autorizados pueden marcarlo como cumplido.
- **RN-003:** Debe registrarse la fecha de realización.
- **RN-004:** La actividad realizada debe conservarse en el historial.
- **RN-005:** Un mantenimiento cumplido no debe marcarse nuevamente como pendiente sin una modificación autorizada.
