
# RF-023 — Asignación de solicitudes de mantenimiento

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-023 |
| **Nombre** | Asignación de solicitudes de mantenimiento |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir que el administrador asigne las solicitudes de mantenimiento a los ingenieros disponibles, teniendo en cuenta los equipos que necesitan revisión o reparación.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID de solicitud | ID | Sí | Debe existir y estar pendiente. |
| ID del ingeniero | ID | Sí | Debe corresponder a un ingeniero registrado y activo. |
| Fecha de asignación | Fecha/hora | Sí | Generada por el sistema. |

---

## Proceso

1. El administrador ingresa al módulo de mantenimientos.
2. Consulta las solicitudes pendientes.
3. Selecciona la solicitud que desea asignar.
4. El sistema muestra los ingenieros disponibles.
5. El administrador selecciona al ingeniero responsable.
6. El sistema valida la información.
7. Guarda la asignación.
8. Actualiza el estado de la solicitud.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Asignación exitosa | 200 | Solicitud asignada correctamente. |
| Solicitud inexistente | 404 | No se encontró la solicitud. |
| Ingeniero no disponible | 409 | El ingeniero no puede recibir la asignación. |
| Datos inválidos | 422 | Información incorrecta. |
| Sin autorización | 403 | No tiene permisos para asignar mantenimientos. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/maintenance-requests/{id}/assign` | Sí | Asigna una solicitud a un ingeniero. |
| GET | `/api/v1/technicians/available` | Sí | Consulta los ingenieros disponibles. |

---

## Reglas de negocio

- **RN-001:** Solo el administrador puede asignar solicitudes.
- **RN-002:** El ingeniero debe estar registrado y activo.
- **RN-003:** La solicitud debe existir y encontrarse disponible para asignación.
- **RN-004:** Cada asignación debe conservar la fecha y el responsable.
