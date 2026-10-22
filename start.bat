@echo off
title War of Realms: Pixel Lane Defense
cd /d "%~dp0"

echo ===================================================
echo   War of Realms: Pixel Lane Defense (Kids Edition)
echo ===================================================
echo Membuka browser ke http://localhost:8080 ...
echo.

start "" http://localhost:8080

where node >nul 2>nul
if %errorlevel% equ 0 (
    node server.js
) else (
    where python >nul 2>nul
    if %errorlevel% equ 0 (
        python -m http.server 8080
    ) else (
        echo Node.js atau Python tidak ditemukan di PATH.
        pause
    )
)
