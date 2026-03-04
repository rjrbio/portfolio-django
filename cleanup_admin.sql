-- Script SQL para limpiar usuarios inseguros en PostgreSQL
-- SOLO para emergencia: ejecutar directamente en BD si Django no funciona
-- 
-- Uso en psql:
--   \i cleanup_admin.sql
-- O desde línea de comandos:
--   psql -U portfolio_user -d portfolio_db -f cleanup_admin.sql

-- Mostrar usuarios antes
SELECT id, username, email, is_superuser, is_staff FROM auth_user ORDER BY date_joined;

-- Eliminar usuario admin (SOLO si existe)
DELETE FROM auth_user WHERE username = 'admin';

-- Eliminar otros usuarios por defecto (si existen)
DELETE FROM auth_user WHERE username IN ('administrator', 'root', 'test', 'demo', 'admin123');

-- Mostrar usuarios después
SELECT id, username, email, is_superuser, is_staff FROM auth_user ORDER BY date_joined;

-- Confirmación
\echo '✅ Limpieza de usuarios inseguros completada'
