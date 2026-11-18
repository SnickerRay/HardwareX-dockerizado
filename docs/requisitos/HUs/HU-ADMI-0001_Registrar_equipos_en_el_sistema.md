
# HU-ADMI-0001 — Registrar equipos en el sistema

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-ADMI-0001 |
| **Título** | Registrar equipos en el sistema |
| **Módulo** | Gestión de equipos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-016 |

---

## Historia

Como administrador, necesito registrar equipos en el sistema, con la finalidad de llevar un control de los dispositivos tecnológicos de la organización y mantener organizada su información en Hardwarex.

---

## Criterios de aceptación

### CA-ADMI-0001.1 — Registro exitoso de equipo

- **Dado que** el administrador ingresa todos los datos obligatorios del equipo correctamente.
- **Cuando** seleccione la opción de registrar el equipo.
- **Entonces** el sistema debe guardar la información correctamente y mostrar un mensaje de confirmación.

### CA-ADMI-0001.2 — Campos vacíos

- **Dado que** faltan datos obligatorios en el formulario de registro.
- **Cuando** el administrador intente registrar el equipo.
- **Entonces** el sistema debe mostrar un mensaje de error solicitando completar los campos requeridos.
