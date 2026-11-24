
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
| **RF asociados** | RF-025 |

---

## Historia

Como técnico, necesito consultar los detalles de las solicitudes de mantenimiento que me han sido asignadas, con la finalidad de conocer la información de los equipos y las fallas reportadas para gestionar su atención.

---

## Criterios de aceptación

### CA-TEC-001.1 — Visualización de solicitudes asignadas

- **Dado que** existen solicitudes de mantenimiento asignadas al técnico.
- **Cuando** ingrese a Hardwarex y consulte el módulo de mantenimientos.
- **Entonces** el sistema debe mostrar las solicitudes que tiene asignadas.

### CA-TEC-001.2 — Solicitudes sin asignar

- **Dado que** el técnico no tiene solicitudes de mantenimiento asignadas.
- **Cuando** consulte sus solicitudes.
- **Entonces** el sistema debe mostrar un mensaje indicando que no tiene solicitudes asignadas.

### CA-TEC-001.3 — Consulta de detalles

- **Dado que** el técnico tiene una solicitud de mantenimiento asignada.
- **Cuando** seleccione una solicitud del listado.
- **Entonces** el sistema debe mostrar los detalles de la solicitud de mantenimiento, incluyendo la información del equipo relacionado y la falla reportada.

### CA-TEC-001.4 — Acceso autorizado

- **Dado que** el técnico ha iniciado sesión en Hardwarex.
- **Cuando** consulte las solicitudes de mantenimiento.
- **Entonces** el sistema debe permitirle visualizar únicamente las solicitudes que tiene asignadas o aquellas que su rol esté autorizado para consultar.
