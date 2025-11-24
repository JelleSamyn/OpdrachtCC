@echo off
REM =============================================
REM Docker Compose Deployment Script - Windows
REM =============================================

REM Controleer of Docker Compose beschikbaar is
where docker-compose >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: docker-compose is not installed or not in PATH.
    pause
    exit /b 1
)

echo =============================================
echo Stopping old containers...
docker-compose down
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to stop containers.
    pause
    exit /b 1
)

echo =============================================
echo Building containers...
docker-compose build
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to build containers.
    pause
    exit /b 1
)

echo =============================================
echo Starting stack...
docker-compose up -d
IF %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to start containers.
    pause
    exit /b 1
)

echo =============================================
echo Deployment complete!
pause
