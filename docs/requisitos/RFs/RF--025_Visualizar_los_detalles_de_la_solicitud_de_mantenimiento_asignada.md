
# RF-025 — Consulta de detalles de mantenimiento asignado

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-025 |
| **Nombre** | Consulta de detalles de mantenimiento asignado |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir que los ingenieros consulten los detalles de las solicitudes de mantenimiento que tienen asignadas, incluyendo la información del equipo, la falla reportada y las actividades que deben realizar.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID de solicitud | ID | Sí | Debe existir. |
| ID del ingeniero | ID | Sí | Debe estar autorizado para consultar la solicitud. |

---

## Proceso

1. El ingeniero inicia sesión en Hardwarex.
2. Ingresa al módulo de mantenimientos.
3. Consulta las solicitudes asignadas.
4. Selecciona una solicitud.
5. El sistema verifica que el ingeniero tenga permiso para consultarla.
6. Obtiene los datos relacionados con el equipo y la falla.
7. Muestra los detalles de la solicitud.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Consulta exitosa | 200 | Detalles completos de la solicitud. |
| Solicitud inexistente | 404 | No se encontró el mantenimiento. |
| Sin autorización | 403 | No tiene permiso para consultar esta solicitud. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/maintenance-requests/{id}` | Sí | Consulta los detalles de una solicitud. |
| GET | `/api/v1/technicians/me/maintenance-requests` | Sí | Consulta las solicitudes asignadas al ingeniero autenticado. |

---

## Reglas de negocio

- **RN-001:** El ingeniero debe estar autenticado.
- **RN-002:** Solo puede consultar las solicitudes que tiene asignadas o aquellas autorizadas por su rol.
- **RN-003:** La información debe corresponder al mantenimiento seleccionado.
- **RN-004:** Los datos deben mantenerse actualizados.
