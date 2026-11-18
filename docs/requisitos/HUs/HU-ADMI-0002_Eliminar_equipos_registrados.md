
# HU-ADMI-0002 — Eliminar equipos registrados

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-ADMI-0002 |
| **Título** | Eliminar equipos registrados |
| **Módulo** | Gestión de equipos |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **RF asociados** | RF-018 |

---

## Historia

Como administrador, necesito eliminar equipos registrados, con la finalidad de depurar información innecesaria y mantener actualizada la base de datos de Hardwarex.

---

## Criterios de aceptación

### CA-ADMI-0002.1 — Eliminación correcta

- **Dado que** el equipo existe y se encuentra registrado en Hardwarex.
- **Cuando** el administrador seleccione la opción de eliminar y confirme la operación.
- **Entonces** el sistema debe eliminar el registro correctamente y actualizar el listado de equipos.

### CA-ADMI-0002.2 — Equipo no encontrado

- **Dado que** el equipo que se desea eliminar no existe en el sistema.
- **Cuando** el administrador intente realizar la eliminación.
- **Entonces** el sistema debe mostrar un mensaje indicando que no se encontró el equipo.
