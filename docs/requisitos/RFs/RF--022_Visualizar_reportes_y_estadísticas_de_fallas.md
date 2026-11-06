
# RF-022 — Visualización de reportes y estadísticas de fallas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-022 |
| **Nombre** | Visualización de reportes y estadísticas de fallas |
| **Módulo** | Reportes y estadísticas |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir que el administrador consulte reportes y estadísticas relacionadas con las fallas registradas en los equipos, facilitando el seguimiento de los problemas presentados en la organización.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Fecha inicial | Fecha | No | Debe ser una fecha válida. |
| Fecha final | Fecha | No | No puede ser anterior a la inicial. |
| Estado de la falla | Texto | No | Debe corresponder a un estado permitido. |
| Equipo | ID | No | Debe existir si se selecciona. |

---

## Proceso

1. El administrador ingresa al módulo de reportes.
2. Selecciona la opción de estadísticas de fallas.
3. Define los filtros de consulta si los necesita.
4. El sistema consulta los reportes almacenados.
5. Organiza la información según los filtros.
6. Calcula los resultados y estadísticas disponibles.
7. Muestra los datos en la plataforma.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Consulta exitosa | 200 | Reportes y estadísticas de fallas. |
| Sin resultados | 200 | Mensaje indicando que no existen fallas para los filtros seleccionados. |
| Filtros inválidos | 422 | Error en los parámetros de consulta. |
| Sin autorización | 403 | No tiene permisos para consultar estadísticas. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/reports/faults` | Sí | Consulta los reportes de fallas. |
| GET | `/api/v1/reports/fault-statistics` | Sí | Obtiene estadísticas de fallas. |

---

## Reglas de negocio

- **RN-001:** Solo el administrador puede consultar las estadísticas administrativas.
- **RN-002:** Los resultados deben basarse en los reportes registrados.
- **RN-003:** Los filtros deben aplicarse correctamente.
- **RN-004:** La información debe mostrarse de manera organizada.
