
# HU-TEC-003 — Registrar observaciones del mantenimiento realizado

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-TEC-003 |
| **Título** | Registrar observaciones del mantenimiento realizado |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **RF asociados** | RF-040 |

---

## Historia

Como técnico, necesito registrar observaciones del mantenimiento realizado, con la finalidad de dejar evidencia del trabajo efectuado y conservar información importante sobre las actividades realizadas en los equipos tecnológicos.

---

## Criterios de aceptación

### CA-TEC-003.1 — Registro de observaciones

- **Dado que** el mantenimiento se encuentra en proceso o finalizado.
- **Cuando** el técnico agregue observaciones sobre el trabajo realizado.
- **Entonces** el sistema debe guardar la información registrada y relacionarla con el mantenimiento correspondiente.

### CA-TEC-003.2 — Observaciones vacías

- **Dado que** el campo de observaciones se encuentra vacío.
- **Cuando** el técnico intente guardar la información.
- **Entonces** el sistema debe solicitar el ingreso de las observaciones antes de continuar.

### CA-TEC-003.3 — Consulta de historial

- **Dado que** existen observaciones registradas anteriormente.
- **Cuando** el técnico consulte la información del mantenimiento.
- **Entonces** el sistema debe mostrar el historial de observaciones realizadas.

### CA-TEC-003.4 — Edición de observaciones

- **Dado que** el mantenimiento todavía no está finalizado.
- **Cuando** el técnico modifique las observaciones registradas.
- **Entonces** el sistema debe actualizar la información correctamente.
