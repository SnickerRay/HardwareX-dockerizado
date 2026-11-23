
# HU-TEC-006 — Visualizar la prioridad de las solicitudes asignadas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-TEC-006 |
| **Título** | Visualizar la prioridad de las solicitudes asignadas |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **RF asociados** | RF-025 |

---

## Historia

Como técnico, necesito visualizar la prioridad de las solicitudes asignadas, con la finalidad de atender primero las incidencias más críticas y organizar adecuadamente las actividades de mantenimiento.

---

## Criterios de aceptación

### CA-TEC-006.1 — Visualización de prioridad

- **Dado que** existen solicitudes de mantenimiento asignadas al técnico.
- **Cuando** consulte el listado de solicitudes.
- **Entonces** el sistema debe mostrar el nivel de prioridad correspondiente a cada solicitud.

### CA-TEC-006.2 — Ordenamiento automático

- **Dado que** existen solicitudes con diferentes niveles de prioridad.
- **Cuando** el técnico visualice el listado.
- **Entonces** el sistema debe organizar las solicitudes de acuerdo con su nivel de prioridad, mostrando primero las más urgentes.

### CA-TEC-006.3 — Identificación visual

- **Dado que** una solicitud tiene prioridad crítica.
- **Cuando** el técnico consulte la solicitud.
- **Entonces** el sistema debe resaltar visualmente su nivel de prioridad para facilitar su identificación.

### CA-TEC-006.4 — Priorización correcta

- **Dado que** el nivel de prioridad de una solicitud ha sido modificado.
- **Cuando** el técnico actualice o consulte nuevamente el listado.
- **Entonces** el sistema debe reflejar el nuevo nivel de prioridad y organizar las solicitudes correctamente.
