
# HU-TEC-001 — Consultar solicitudes de mantenimiento asignadas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-TEC-001 |
| **Título** | Consultar solicitudes de mantenimiento asignadas |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-023, RF-025 |

---

## Historia

Como técnico, necesito consultar las solicitudes de mantenimiento que me han sido asignadas, con la finalidad de gestionar y atender las fallas reportadas por los usuarios de Hardwarex.

---

## Criterios de aceptación

### CA-TEC-001.1 — Visualización de solicitudes

- **Dado que** existen solicitudes de mantenimiento asignadas al técnico.
- **Cuando** ingrese a Hardwarex y consulte el módulo de mantenimientos.
- **Entonces** el sistema debe mostrar el listado de solicitudes pendientes que le han sido asignadas.

### CA-TEC-001.2 — Solicitudes sin asignar

- **Dado que** el técnico no tiene solicitudes de mantenimiento asignadas.
- **Cuando** consulte sus solicitudes.
- **Entonces** el sistema debe mostrar un mensaje indicando que no tiene solicitudes pendientes.

### CA-TEC-001.3 — Consulta de detalles

- **Dado que** el técnico tiene una solicitud de mantenimiento asignada.
- **Cuando** seleccione una solicitud del listado.
- **Entonces** el sistema debe mostrar la información completa de la falla reportada, el equipo relacionado y los datos de la solicitud.

### CA-TEC-001.4 — Acceso autorizado

- **Dado que** el técnico ha iniciado sesión en Hardwarex.
- **Cuando** intente ingresar al módulo de solicitudes asignadas.
- **Entonces** el sistema debe permitirle consultar únicamente las solicitudes que le corresponden.
