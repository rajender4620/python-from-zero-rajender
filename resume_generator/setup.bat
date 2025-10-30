@echo off
echo Installing Resume Generator Dependencies...
echo ==========================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH.
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo Python found. Installing dependencies...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo ✅ Setup completed successfully!
    echo.
    echo To generate your resume, run:
    echo   python main.py
    echo.
) else (
    echo ❌ Failed to install dependencies.
    echo Please check your internet connection and try again.
)

pause
