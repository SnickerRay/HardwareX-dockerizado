
# RNF-014 — Capacidad de usuarios concurrentes

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RNF-014 |
| **Nombre** | Capacidad de usuarios concurrentes |
| **Categoría** | Rendimiento y escalabilidad |
| **Prioridad** | Alta |
| **Estado** | Por validar |

---

## Requisitos

### RNF-014.1 — Capacidad mínima de usuarios

Hardwarex debe soportar como mínimo X usuarios conectados simultáneamente sin afectar el funcionamiento de la plataforma.

### RNF-014.2 — Acceso simultáneo a módulos

Los usuarios deben poder utilizar al mismo tiempo los módulos de equipos, mantenimientos, garantías, usuarios y reportes.

### RNF-014.3 — Estabilidad durante la concurrencia

El sistema debe mantener su estabilidad y evitar cierres inesperados cuando se alcance el número mínimo de usuarios concurrentes establecido.

### RNF-014.4 — Procesamiento de solicitudes

La plataforma debe procesar las solicitudes de los usuarios sin generar pérdida de información ni errores en las operaciones.

### RNF-014.5 — Pruebas de concurrencia

Se deben realizar pruebas de rendimiento para comprobar que Hardwarex soporte la cantidad mínima de usuarios simultáneos definida.
