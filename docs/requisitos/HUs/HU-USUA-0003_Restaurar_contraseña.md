
# HU-USUA-0003 — Restaurar contraseña

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-USUA-0003 |
| **Título** | Restaurar contraseña |
| **Módulo** | Recuperación de contraseña |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-005, RF-006 |

---

## Historia

Como usuario, necesito restaurar mi contraseña, con la finalidad de recuperar el acceso a la aplicación Hardwarex cuando no recuerde mis credenciales.

---

## Criterios de aceptación

### CA-USUA-0003.1 — Correo válido

- **Dado que** el correo electrónico ingresado se encuentra registrado en Hardwarex.
- **Cuando** el usuario presione el botón «Restaurar contraseña».
- **Entonces** el sistema debe enviar un código o enlace de recuperación al correo electrónico registrado para permitirle restablecer su contraseña.

### CA-USUA-0003.2 — Correo inválido

- **Dado que** el correo electrónico ingresado no existe en el sistema.
- **Cuando** el usuario solicite restaurar su contraseña.
- **Entonces** el sistema debe mostrar un mensaje informando que no se encontró una cuenta asociada al correo ingresado.
