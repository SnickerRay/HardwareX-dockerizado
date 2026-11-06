
# RNF-002 — Almacenamiento seguro de contraseñas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RNF-002 |
| **Nombre** | Almacenamiento seguro de contraseñas |
| **Categoría** | Seguridad de la información |
| **Prioridad** | Crítica |
| **Estado** | Por validar |

---

## Requisitos

### RNF-002.1 — Cifrado mediante hash

Las contraseñas de los usuarios de Hardwarex deben almacenarse utilizando algoritmos seguros de hashing, como bcrypt o Argon2.

### RNF-002.2 — Protección de contraseñas

Las contraseñas nunca deben almacenarse en texto plano dentro de la base de datos.

### RNF-002.3 — Validación de contraseñas

El sistema debe verificar las contraseñas ingresadas comparándolas con el hash almacenado, sin recuperar ni mostrar la contraseña original.

### RNF-002.4 — Protección de información

Las contraseñas no deben aparecer en registros de errores, respuestas de la API ni mensajes del sistema.
