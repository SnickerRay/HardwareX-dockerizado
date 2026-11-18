
# RF-012 — Límite de intentos de inicio de sesión

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-012 |
| **Nombre** | Límite de intentos de inicio de sesión |
| **Módulo** | Seguridad y autenticación |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe limitar a tres los intentos fallidos de inicio de sesión, bloqueando temporalmente el acceso cuando el usuario supere el número de oportunidades permitido.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Correo electrónico | Texto | Sí | Debe tener un formato válido. |
| Contraseña | Texto protegido | Sí | Se verifica durante cada intento. |
| Contador de intentos | Número entero | Sí | Debe registrar los intentos fallidos. |

---

## Proceso

1. El usuario intenta iniciar sesión.
2. El sistema verifica las credenciales.
3. Si son incorrectas, aumenta el contador de intentos.
4. Permite realizar nuevos intentos mientras no se alcance el límite.
5. Al completar tres intentos fallidos, bloquea temporalmente el acceso.
6. Muestra un mensaje informando sobre el bloqueo.
7. Permite intentar nuevamente cuando finalice el periodo establecido.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Primer o segundo intento fallido | 401 | Credenciales incorrectas. |
| Tercer intento fallido | 429 | Cuenta temporalmente bloqueada por intentos fallidos. |
| Acceso correcto | 200 | Inicio de sesión exitoso. |
| Cuenta bloqueada | 429 | Debe esperar para volver a intentar. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/login` | No | Valida credenciales y controla los intentos de acceso. |

---

## Reglas de negocio

- **RN-001:** El máximo permitido es de tres intentos fallidos.
- **RN-002:** Al alcanzar el límite se debe aplicar un bloqueo temporal.
- **RN-003:** El contador debe gestionarse desde el servidor.
- **RN-004:** Los intentos exitosos deben restablecer el contador según la política de seguridad.
- **RN-005:** El tiempo de bloqueo debe estar definido en la configuración del sistema.
