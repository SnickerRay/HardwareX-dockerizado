
# RF-037 — Recordatorios automáticos de mantenimiento

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-037 |
| **Nombre** | Recordatorios automáticos de mantenimiento |
| **Módulo** | Planificación y notificaciones |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe generar recordatorios automáticos sobre los mantenimientos preventivos programados que estén próximos a realizarse, permitiendo que los responsables conozcan las actividades pendientes.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del mantenimiento | ID | Sí | Debe corresponder a una programación registrada. |
| Fecha programada | Fecha/hora | Sí | Debe ser válida. |
| Fecha del recordatorio | Fecha/hora | Sí | Debe corresponder al periodo de anticipación establecido. |
| Responsable | ID | Sí | Debe corresponder a un usuario autorizado. |

---

## Proceso

1. El sistema consulta los mantenimientos programados.
2. Identifica las actividades que se aproximan a su fecha de realización.
3. Verifica que los mantenimientos continúen pendientes.
4. Genera los recordatorios correspondientes.
5. Relaciona cada recordatorio con el mantenimiento.
6. Los muestra a los usuarios responsables mediante el medio disponible.
7. Registra los recordatorios generados.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Recordatorio generado | 201 | Recordatorio creado correctamente. |
| Sin mantenimientos próximos | 200 | No existen mantenimientos próximos a realizarse. |
| Mantenimiento inexistente | 404 | No se encontró el mantenimiento. |
| Error de generación | 500 | No fue posible generar el recordatorio. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/notifications` | Sí | Consulta los recordatorios disponibles. |
| GET | `/api/v1/preventive-maintenance/upcoming` | Sí | Consulta los mantenimientos próximos. |

---

## Reglas de negocio

- **RN-001:** Los recordatorios deben generarse según la fecha programada.
- **RN-002:** Solo deben considerarse los mantenimientos pendientes.
- **RN-003:** No deben generarse recordatorios duplicados innecesariamente.
- **RN-004:** Los recordatorios deben estar relacionados con el equipo y el mantenimiento correspondiente.
