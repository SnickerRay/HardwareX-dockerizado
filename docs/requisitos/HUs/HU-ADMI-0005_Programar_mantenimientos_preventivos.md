
# HU-ADMI-0005 — Programar mantenimientos preventivos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-ADMI-0005 |
| **Título** | Programar mantenimientos preventivos |
| **Módulo** | Planificación de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-036 |

---

## Historia

Como administrador, necesito programar mantenimientos preventivos, con la finalidad de evitar daños futuros en los equipos tecnológicos y mantenerlos en buenas condiciones de funcionamiento.

---

## Criterios de aceptación

### CA-ADMI-0005.1 — Programación exitosa

- **Dado que** el equipo se encuentra registrado en Hardwarex.
- **Cuando** el administrador ingrese la información y programe el mantenimiento preventivo.
- **Entonces** el sistema debe guardar la programación correctamente y mostrar la fecha establecida.

### CA-ADMI-0005.2 — Fecha inválida

- **Dado que** la fecha ingresada para el mantenimiento no es válida.
- **Cuando** el administrador intente programar el mantenimiento.
- **Entonces** el sistema debe mostrar un mensaje de error indicando que debe ingresar una fecha válida.
