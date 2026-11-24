
# HU-USUA-0004 — Reportar fallas de equipos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-USUA-0004 |
| **Título** | Reportar fallas de equipos |
| **Módulo** | Gestión de fallas |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-019, RF-020, RF-021 |

---

## Historia

Como usuario, necesito reportar fallas de los equipos tecnológicos y describir detalladamente el problema presentado, con la finalidad de solicitar mantenimiento o soporte técnico y permitir que el administrador gestione la atención de la falla.

---

## Criterios de aceptación

### CA-USUA-0004.1 — Registrar una falla

- **Dado que** el usuario ha iniciado sesión y tiene equipos registrados disponibles.
- **Cuando** seleccione un equipo y envíe un reporte de falla.
- **Entonces** el sistema debe registrar el reporte asociado al equipo seleccionado.

### CA-USUA-0004.2 — Descripción detallada del problema

- **Dado que** el usuario está diligenciando el formulario de reporte de fallas.
- **Cuando** describa el problema técnico presentado en el equipo.
- **Entonces** el sistema debe permitir registrar una descripción detallada de la falla.

### CA-USUA-0004.3 — Descripción obligatoria

- **Dado que** el usuario intenta enviar un reporte sin ingresar la descripción del problema.
- **Cuando** envíe el formulario.
- **Entonces** el sistema debe mostrar un mensaje indicando que debe completar la descripción y no debe registrar el reporte.

### CA-USUA-0004.4 — Notificación al administrador

- **Dado que** el usuario ha registrado correctamente una nueva falla.
- **Cuando** el sistema confirme el registro del reporte.
- **Entonces** debe notificar al administrador sobre la nueva falla para que pueda gestionar su atención.
