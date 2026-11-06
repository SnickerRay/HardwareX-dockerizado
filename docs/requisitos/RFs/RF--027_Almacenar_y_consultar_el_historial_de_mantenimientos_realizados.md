
# RF-027 — Historial de mantenimientos realizados

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-027 |
| **Nombre** | Historial de mantenimientos realizados |
| **Módulo** | Historial de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe almacenar y permitir consultar el historial de los mantenimientos realizados a cada equipo tecnológico, conservando información sobre las actividades, fechas y responsables de cada intervención.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del equipo | ID | Sí | Debe existir. |
| ID del mantenimiento | ID | Sí | Debe corresponder a un mantenimiento registrado. |
| Actividad realizada | Texto | Sí | No puede estar vacía. |
| Responsable | ID | Sí | Debe corresponder a un usuario autorizado. |
| Fecha de realización | Fecha/hora | Sí | Debe ser válida. |

---

## Proceso

1. El responsable finaliza una actividad de mantenimiento.
2. El sistema recibe los datos de la intervención.
3. Verifica que el equipo y el mantenimiento existan.
4. Valida la información registrada.
5. Almacena los datos en el historial.
6. Relaciona el registro con el equipo correspondiente.
7. Permite consultar los mantenimientos anteriores.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Historial consultado | 200 | Listado de mantenimientos del equipo. |
| Registro creado | 201 | Actividad almacenada correctamente. |
| Equipo inexistente | 404 | No se encontró el equipo. |
| Sin registros | 200 | El equipo todavía no tiene mantenimientos registrados. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/equipment/{id}/maintenance-history` | Sí | Consulta el historial de un equipo. |
| POST | `/api/v1/maintenance-history` | Sí | Registra una actividad de mantenimiento. |

---

## Reglas de negocio

- **RN-001:** Cada registro debe relacionarse con un equipo existente.
- **RN-002:** El historial debe conservar las actividades realizadas.
- **RN-003:** Cada intervención debe identificar a su responsable.
- **RN-004:** Los registros históricos no deben modificarse sin autorización.
