
# RF-028 — Consulta del estado actual de mantenimiento

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-028 |
| **Nombre** | Consulta del estado actual de mantenimiento |
| **Módulo** | Consulta de equipos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe mostrar el estado actual de mantenimiento de cada equipo tecnológico, permitiendo conocer si tiene actividades pendientes, en proceso o finalizadas.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del equipo | ID | Sí | Debe corresponder a un equipo registrado. |
| Estado del mantenimiento | Texto | Sí | Debe pertenecer a los estados permitidos. |

---

## Proceso

1. El usuario ingresa al módulo de equipos.
2. Selecciona el equipo que desea consultar.
3. El sistema busca los mantenimientos asociados.
4. Identifica las solicitudes y sus estados actuales.
5. Organiza la información.
6. Muestra el estado de mantenimiento del equipo.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Consulta exitosa | 200 | Estado actual del mantenimiento. |
| Equipo sin mantenimientos | 200 | Mensaje indicando que no existen mantenimientos registrados. |
| Equipo inexistente | 404 | No se encontró el equipo. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/equipment/{id}/maintenance-status` | Sí | Consulta el estado de mantenimiento de un equipo. |

---

## Reglas de negocio

- **RN-001:** El equipo debe estar registrado.
- **RN-002:** El estado debe obtenerse de los mantenimientos almacenados.
- **RN-003:** La consulta no debe modificar la información.
- **RN-004:** Si existen varias solicitudes, deben mostrarse sus estados por separado.
