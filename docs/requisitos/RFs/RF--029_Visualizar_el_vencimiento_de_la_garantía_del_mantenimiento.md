
# RF-029 — Consulta del vencimiento de garantías

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-029 |
| **Nombre** | Consulta del vencimiento de garantías |
| **Módulo** | Gestión de garantías |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir consultar la fecha de vencimiento de las garantías asociadas a los equipos tecnológicos, facilitando el seguimiento de su vigencia y cobertura.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del equipo | ID | Sí | Debe existir. |
| Fecha de inicio | Fecha | Según registro | Debe ser válida. |
| Fecha de vencimiento | Fecha | Según registro | Debe ser igual o posterior a la fecha inicial. |

---

## Proceso

1. El usuario ingresa al módulo de equipos.
2. Selecciona el equipo que desea consultar.
3. El sistema busca las garantías relacionadas.
4. Obtiene las fechas de inicio y vencimiento.
5. Compara la fecha de vencimiento con la fecha actual.
6. Determina si la garantía está vigente o vencida.
7. Muestra la información correspondiente.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Garantía encontrada | 200 | Información y fecha de vencimiento de la garantía. |
| Garantía vencida | 200 | Se muestra la garantía con estado vencido. |
| Sin garantía | 200 | El equipo no tiene una garantía registrada. |
| Equipo inexistente | 404 | No se encontró el equipo. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/equipment/{id}/warranties` | Sí | Consulta las garantías de un equipo. |

---

## Reglas de negocio

- **RN-001:** La garantía debe estar relacionada con un equipo registrado.
- **RN-002:** La fecha de vencimiento no puede ser anterior a la fecha de inicio.
- **RN-003:** El estado de vigencia debe determinarse con las fechas almacenadas.
- **RN-004:** La consulta debe mostrar información actualizada.
