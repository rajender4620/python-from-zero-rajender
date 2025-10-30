@echo off
echo Resume Generator
echo ===============

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please run setup.bat first.
    pause
    exit /b 1
)

echo Generating resume...
python main.py

if %errorlevel% equ 0 (
    echo.
    echo ✅ Resume generated successfully!
    echo Check the 'output' folder for your PDF.
) else (
    echo ❌ Failed to generate resume.
    echo Please check the error messages above.
)

echo.
pause
