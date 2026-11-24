
# HU-TEC-003 — Registrar observaciones del mantenimiento preventivo

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-TEC-003 |
| **Título** | Registrar observaciones del mantenimiento preventivo |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **RF asociados** | RF-040 |

---

## Historia

Como técnico, necesito registrar observaciones técnicas del mantenimiento preventivo realizado, con la finalidad de dejar constancia de las actividades efectuadas y conservar información importante sobre el estado de los equipos tecnológicos.

---

## Criterios de aceptación

### CA-TEC-003.1 — Registro de observaciones preventivas

- **Dado que** el técnico está realizando un mantenimiento preventivo.
- **Cuando** registre las observaciones técnicas sobre las actividades efectuadas.
- **Entonces** el sistema debe guardar la información y relacionarla con el mantenimiento preventivo correspondiente.

### CA-TEC-003.2 — Observaciones vacías

- **Dado que** el campo de observaciones se encuentra vacío.
- **Cuando** el técnico intente guardar la información.
- **Entonces** el sistema debe solicitar el ingreso de las observaciones antes de continuar.

### CA-TEC-003.3 — Consulta de observaciones

- **Dado que** existen observaciones registradas de un mantenimiento preventivo.
- **Cuando** el técnico consulte la información de dicho mantenimiento.
- **Entonces** el sistema debe permitir visualizar las observaciones registradas.

### CA-TEC-003.4 — Edición de observaciones

- **Dado que** el mantenimiento preventivo todavía no está finalizado.
- **Cuando** el técnico modifique las observaciones registradas.
- **Entonces** el sistema debe actualizar la información correspondiente.
