
# HU-ADMI-0003 — Visualizar reportes de fallas y estadísticas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-ADMI-0003 |
| **Título** | Visualizar reportes de fallas y estadísticas |
| **Módulo** | Reportes y estadísticas |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-022 |

---

## Historia

Como administrador, necesito visualizar reportes de fallas y estadísticas, con la finalidad de realizar seguimiento a los mantenimientos y conocer el comportamiento de los equipos tecnológicos registrados en Hardwarex.

---

## Criterios de aceptación

### CA-ADMI-0003.1 — Consulta exitosa de reportes

- **Dado que** existen registros de fallas y mantenimientos almacenados en Hardwarex.
- **Cuando** el administrador ingrese al módulo de reportes.
- **Entonces** el sistema debe mostrar las estadísticas y los reportes correspondientes de manera organizada.

### CA-ADMI-0003.2 — Sin información disponible

- **Dado que** no existen reportes registrados en el sistema.
- **Cuando** el administrador consulte el módulo de reportes.
- **Entonces** el sistema debe informar que no hay datos disponibles para mostrar.
