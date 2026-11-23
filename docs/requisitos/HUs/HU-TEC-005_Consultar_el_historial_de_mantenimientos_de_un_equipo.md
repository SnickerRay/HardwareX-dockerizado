
# HU-TEC-005 — Consultar el historial de mantenimientos de un equipo

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-TEC-005 |
| **Título** | Consultar el historial de mantenimientos de un equipo |
| **Módulo** | Historial de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-027 |

---

## Historia

Como técnico, necesito consultar el historial de mantenimientos de un equipo, con la finalidad de conocer las fallas anteriores y los trabajos realizados para tener un mejor seguimiento de su estado.

---

## Criterios de aceptación

### CA-TEC-005.1 — Consulta de historial

- **Dado que** existen mantenimientos realizados anteriormente al equipo.
- **Cuando** el técnico consulte el historial del equipo.
- **Entonces** el sistema debe mostrar los mantenimientos realizados y su información correspondiente.

### CA-TEC-005.2 — Historial inexistente

- **Dado que** el equipo no tiene registros de mantenimientos anteriores.
- **Cuando** el técnico consulte su historial.
- **Entonces** el sistema debe mostrar un mensaje informando que no existen registros disponibles.

### CA-TEC-005.3 — Visualización cronológica

- **Dado que** el técnico selecciona un registro del historial.
- **Cuando** haga clic sobre el mantenimiento.
- **Entonces** el sistema debe mostrar la información completa del registro, incluyendo fechas, actividades y observaciones disponibles.

### CA-TEC-005.4 — Acceso autorizado

- **Dado que** el técnico tiene una sesión iniciada en Hardwarex.
- **Cuando** intente ingresar al historial de mantenimientos.
- **Entonces** el sistema debe permitir el acceso de acuerdo con los permisos de su rol.
