INSERT INTO public.rol (nombre_rol, descripcion_rol, estado_rol)
VALUES
    ('Administrador', 'Administrador del sistema', 'Activo'),
    ('Usuario', 'Usuario normal del sistema', 'Activo'),
    ('Tecnico', 'Responsable del mantenimiento y reparacion de equipos', 'Activo')
ON CONFLICT (nombre_rol) DO NOTHING;
