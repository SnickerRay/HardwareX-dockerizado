
# HU-TEC-002 — Actualizar el estado del mantenimiento

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-TEC-002 |
| **Título** | Actualizar el estado del mantenimiento |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-026, RF-028 |

---

## Historia

Como técnico, necesito actualizar el estado del mantenimiento, con la finalidad de informar el progreso del servicio realizado y mantener actualizado el seguimiento de los equipos en Hardwarex.

---

## Criterios de aceptación

### CA-TEC-002.1 — Cambio de estado

- **Dado que** existe un mantenimiento asignado al técnico.
- **Cuando** cambie el estado del mantenimiento.
- **Entonces** el sistema debe guardar el nuevo estado correctamente.

### CA-TEC-002.2 — Estado en proceso

- **Dado que** el mantenimiento asignado ha iniciado.
- **Cuando** el técnico seleccione el estado «En proceso».
- **Entonces** el sistema debe actualizar el estado del mantenimiento y mostrarlo como una actividad en ejecución.

### CA-TEC-002.3 — Estado finalizado

- **Dado que** el mantenimiento ha sido completado.
- **Cuando** el técnico seleccione el estado «Finalizado».
- **Entonces** el sistema debe registrar la fecha de finalización y actualizar el estado del mantenimiento.

### CA-TEC-002.4 — Validación de información

- **Dado que** faltan datos obligatorios para actualizar el mantenimiento.
- **Cuando** el técnico intente guardar los cambios.
- **Entonces** el sistema debe mostrar un mensaje indicando que debe completar la información requerida.
