
# RF-008 — Verificación de la contraseña ingresada

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-008 |
| **Nombre** | Verificación de la contraseña ingresada |
| **Módulo** | Autenticación |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe comprobar que la contraseña ingresada por el usuario coincida con la contraseña almacenada de forma segura en la base de datos.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Correo electrónico | Texto | Sí | Debe identificar una cuenta válida. |
| Contraseña | Texto protegido | Sí | Debe coincidir con el hash almacenado. |

---

## Proceso

1. El usuario ingresa sus credenciales.
2. El sistema identifica la cuenta.
3. El backend obtiene el hash de la contraseña almacenada.
4. Compara la contraseña ingresada mediante el mecanismo seguro de verificación.
5. Si coincide, permite continuar con la autenticación.
6. Si no coincide, rechaza el acceso y registra el intento fallido.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Contraseña correcta | 200 | Credenciales verificadas. |
| Contraseña incorrecta | 401 | Correo o contraseña incorrectos. |
| Datos incompletos | 422 | Se deben completar las credenciales. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/login` | No | Comprueba las credenciales ingresadas. |

---

## Reglas de negocio

- **RN-001:** La contraseña debe coincidir con la registrada.
- **RN-002:** La verificación debe realizarse mediante un algoritmo seguro.
- **RN-003:** Las contraseñas no deben almacenarse en texto plano.
- **RN-004:** Los intentos fallidos deben registrarse para aplicar los controles de seguridad.
