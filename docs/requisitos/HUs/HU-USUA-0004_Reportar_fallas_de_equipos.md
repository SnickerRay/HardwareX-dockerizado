
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
| **RF asociados** | RF-013 |

---

## Historia

Como usuario, necesito reportar fallas de los equipos tecnológicos, con la finalidad de solicitar mantenimiento o soporte técnico y permitir que el administrador gestione la atención de los problemas presentados.

---

## Criterios de aceptación

### CA-USUA-0004.1 — Datos completos

- **Dado que** el usuario ha completado todos los campos obligatorios del formulario de reporte de fallas.
- **Cuando** envíe la solicitud.
- **Entonces** el sistema debe registrar la falla y enviar la solicitud al administrador de Hardwarex para su gestión.

### CA-USUA-0004.2 — Campos vacíos

- **Dado que** el usuario no ha completado todos los campos obligatorios del formulario.
- **Cuando** intente enviar la solicitud de mantenimiento.
- **Entonces** el sistema debe mostrar una alerta indicando cuáles son los campos que faltan por completar.

### CA-USUA-0004.3 — Datos incorrectos

- **Dado que** el usuario ha ingresado información incorrecta o que no cumple con las validaciones del formulario.
- **Cuando** intente enviar el reporte de falla.
- **Entonces** el sistema debe mostrar un mensaje de error indicando que debe corregir la información y no debe permitir el envío de la solicitud.
