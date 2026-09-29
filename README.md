# Aplicacion basica de login

Aplicacion de login hecha con Python y Flask. Incluye una ruta protegida, sesiones y cierre de sesion.

## Requisitos

- Python 3.10 o superior

## Instalacion

En PowerShell, desde esta carpeta:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

Si PowerShell bloquea la activacion del entorno, ejecuta:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

## Ejecucion

```powershell
py app.py
```

Abre <http://127.0.0.1:5000> en el navegador.

Usuario de prueba:

- Usuario: `admin`
- Contrasena: `python123`

Para un entorno real, cambia `SECRET_KEY`, usa una base de datos y no dejes credenciales demo en el codigo.
