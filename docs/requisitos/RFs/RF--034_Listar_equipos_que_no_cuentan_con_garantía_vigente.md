
# RF-034 — Listado de equipos sin garantía vigente

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-034 |
| **Nombre** | Listado de equipos sin garantía vigente |
| **Módulo** | Gestión de garantías |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir consultar y mostrar los equipos tecnológicos que no tienen una garantía registrada o cuya garantía ya se encuentra vencida, facilitando el control de su cobertura.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Fecha de consulta | Fecha | Sí | Generada por el sistema. |
| Estado de garantía | Texto | No | Debe corresponder a un estado permitido. |
| ID del equipo | ID | No | Debe existir si se utiliza como filtro. |

---

## Proceso

1. El usuario autorizado ingresa al módulo de garantías.
2. Selecciona la opción de equipos sin garantía vigente.
3. El sistema consulta los equipos registrados.
4. Verifica las garantías asociadas.
5. Compara las fechas de vencimiento con la fecha actual.
6. Identifica los equipos sin cobertura vigente.
7. Muestra el listado de resultados.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Consulta exitosa | 200 | Listado de equipos sin garantía vigente. |
| Sin resultados | 200 | Todos los equipos consultados cuentan con garantía vigente. |
| Error de consulta | 500 | No fue posible generar el listado. |
| Sin autorización | 403 | No tiene permisos para realizar esta consulta. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/reports/equipment-without-warranty` | Sí | Lista equipos sin garantía vigente. |

---

## Reglas de negocio

- **RN-001:** Los equipos sin garantía registrada deben incluirse.
- **RN-002:** Las garantías vencidas no se consideran vigentes.
- **RN-003:** La consulta debe utilizar las fechas almacenadas.
- **RN-004:** Los resultados deben mostrarse de manera organizada.
