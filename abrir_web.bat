@echo off
setlocal

title IDW WEB PROFISSIONAL

cd /d "%~dp0"

set "QGIS_PYTHON=C:\Program Files\QGIS 3.40.15\bin\python-qgis-ltr.bat"

echo ============================================================
echo IDW WEB PROFISSIONAL
echo ============================================================
echo.

if not exist "%QGIS_PYTHON%" (

    echo ERRO:
    echo Python do QGIS nao encontrado.
    echo.
    echo %QGIS_PYTHON%
    echo.

    pause

    exit /b 1
)


call "%QGIS_PYTHON%" "%~dp0servidor_local.py"

echo.
echo Servidor terminado.
echo.

pause
