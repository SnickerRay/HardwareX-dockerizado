# RF-003 — Registro de un usuario nuevo

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-003 |
| **Nombre** | Registro de un usuario nuevo |
| **Módulo** | Gestión de usuarios |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir registrar nuevos usuarios en Hardwarex mediante un formulario en el que se ingresen los datos necesarios para crear una cuenta y acceder a la plataforma.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Nombre completo | Texto | Sí | Mínimo 2 caracteres y máximo 255. |
| Correo electrónico | Texto | Sí | Formato válido y único. |
| Contraseña | Texto protegido | Sí | Debe cumplir los requisitos de seguridad establecidos. |

---

## Proceso

1. El usuario ingresa al formulario de registro.
2. Digita su nombre completo, correo y contraseña.
3. El sistema valida que los campos estén completos.
4. El backend verifica que el correo no esté registrado.
5. Se protege la contraseña mediante un algoritmo de hash.
6. El sistema almacena la información del nuevo usuario.
7. Se confirma la creación de la cuenta.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Registro exitoso | 201 | Usuario creado correctamente. |
| Correo duplicado | 409 | El correo electrónico ya está registrado. |
| Datos inválidos | 422 | Detalle de los errores de validación. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/register` | No | Registra una nueva cuenta de usuario. |

---

## Reglas de negocio

- **RN-001:** El correo electrónico debe ser único.
- **RN-002:** Los campos obligatorios deben estar completos.
- **RN-003:** La contraseña debe almacenarse de forma segura.
- **RN-004:** Cada usuario debe contar con un identificador único.
