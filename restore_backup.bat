@echo off
REM Script para restaurar backup en Render desde Windows

echo ========================================
echo  Restaurar Backup en Render Database
echo ========================================
echo.

REM Pedir la connection string de Render
set /p CONNECTION_STRING="Ingresa la External Connection String de Render: "

echo.
echo Restaurando backup.sql...
echo.

REM Usar Docker para ejecutar psql
docker run --rm -i -v "%cd%":/backup postgres:15 psql "postgresql://portfolio_user:aDCzaEo3ZiDsXTffBj0hrK7tZ5WgnO11@dpg-d413gler433s73d1fo3g-a.oregon-postgres.render.com/portfolio_db_yegu" < backup.sql

echo.
echo ========================================
echo  Backup restaurado exitosamente!
echo ========================================
pause
