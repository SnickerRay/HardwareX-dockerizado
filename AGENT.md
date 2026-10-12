# [HardwareX]
Aplicacion para reportar y llevar un control ordenado de los equipos tecnologicos que fallan y son arreglados constantemente

## Stack
- Lenguaje: HTML, CSS, Python, JavaScript
- Framework / runtime: Django
- Base de datos: PostgreSQL


## Comandos

### Ejecutar el servidor

```bash
python manage.py runserver

py manage.py test tests -v 2 --force-color

### Detener el servidor

```text
Ctrl + C
```


## Estructura del proyecto
- `[.vscode]/` - carpeta creada por Visual Studio Code para almacenar configuraciones del editor.
- `[config]/` - carpeta generada por Django
- `[mantenimiento]/` - carpeta generada por Django
- `[static]/` - contiene los archivos CSS, JS e IMG los cuales se conectan con la carpeta templates
- `[templates]/` - contiene los archivos HTML
- No mover ni renombrar archivos o carpetas existentes sin autorización.


## Convenciones
- Mantener la estructura de plantillas de Django utilizando {% extends %}, {% block %} y {% include %} cuando corresponda.
- Estilo de los nombres CamelCase y snake_case

## No hagas
- corregir TODO el codigo si no te lo piden
- Limite duro, no instalar dependencias sin avisar
- Zona prohibida, no tocar las carpetas `.vscode, config` está congelada
- No modificar la estructura interna de la carpeta `mantenimiento` sin autorización.

## Flujo de trabajo

- Antes de hacer un tarea no trivial, propon un plan y espera mi OK
- Dime que cambiaste para que lo revise
- Si no estas seguro de algo al 80%, pregunta. No inventes

## Diseño

-Mantener el estilo blanco con azules
-No cambiar colores principales
-No modificar el orden de los componentes


## Base de datos
- No modificar modelos ni migraciones sin autorización.
- No eliminar tablas.
- No cambiar relaciones existentes.

## Calidad del código
- Escribir código limpio y legible.
- Reutilizar funciones existentes antes de crear nuevas.
- Evitar duplicar código.
- Mantener comentarios únicamente cuando expliquen lógica compleja.
- Mantener compatibilidad con el código existente.




## para el iker del futuro
piensa como desarrollador junior el cual va a arreglar las conexiones

mira el agent.md para ver el contexto

necesito que todas las urls de la carpeta apps sean funcionales, puedes guiarte de la url de usuario, esa es funcional, necesito que todas las urls sean parecidas a la de usuario

no quiero que uses API, puedes guiarte de como estamos haciendo el proyecto para saber como lo estamos haciendo
NO quiero que arregles otras cosas aparte de las urls de apps y que se conecte bien con las templates

arregla los archivos