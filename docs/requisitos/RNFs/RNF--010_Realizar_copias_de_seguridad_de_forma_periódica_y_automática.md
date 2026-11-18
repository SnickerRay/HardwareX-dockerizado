
# RNF-010 — Copias de seguridad de la información

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RNF-010 |
| **Nombre** | Copias de seguridad de la información |
| **Categoría** | Disponibilidad y recuperación |
| **Prioridad** | Alta |
| **Estado** | Por validar |

---

## Requisitos

### RNF-010.1 — Generación de copias

Hardwarex debe contar con un mecanismo para generar copias de seguridad periódicas de la base de datos.

### RNF-010.2 — Automatización

Las copias de seguridad deben realizarse automáticamente según una frecuencia previamente configurada.

### RNF-010.3 — Almacenamiento seguro

Las copias de seguridad deben almacenarse en una ubicación segura, diferente de la base de datos principal.

### RNF-010.4 — Recuperación de información

El sistema debe permitir restaurar la información mediante las copias de seguridad cuando se presenten fallas o pérdida de datos.

### RNF-010.5 — Verificación de respaldos

Se debe comprobar periódicamente que las copias de seguridad se generen correctamente y puedan utilizarse para recuperar la información.
