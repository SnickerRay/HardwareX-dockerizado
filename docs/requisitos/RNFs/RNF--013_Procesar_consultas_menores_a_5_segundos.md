
# RNF-013 — Tiempo de respuesta de las consultas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RNF-013 |
| **Nombre** | Tiempo de respuesta de las consultas |
| **Categoría** | Rendimiento |
| **Prioridad** | Alta |
| **Estado** | Por validar |

---

## Requisitos

### RNF-013.1 — Tiempo máximo de consulta

Las consultas realizadas en Hardwarex deben procesarse en un tiempo inferior a 5 segundos bajo condiciones normales de funcionamiento.

### RNF-013.2 — Consulta de equipos

El sistema debe permitir consultar los equipos registrados y mostrar su información técnica sin generar retrasos innecesarios.

### RNF-013.3 — Consulta de mantenimientos

Las solicitudes, estados e historiales de mantenimiento deben mostrarse dentro del tiempo establecido.

### RNF-013.4 — Consulta de garantías

La información relacionada con las garantías, sus fechas de vencimiento y proveedores debe estar disponible de manera rápida.

### RNF-013.5 — Generación de reportes

El sistema debe procesar y mostrar los reportes de equipos y mantenimientos en un tiempo inferior a 5 segundos para los volúmenes de información definidos en las pruebas.

### RNF-013.6 — Optimización de consultas

Las consultas a la base de datos deben estar optimizadas para evitar tiempos de espera prolongados.
