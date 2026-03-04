@echo off

echo Checking if Docker is installed...

docker --version >nul 2>&1

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo Docker is not installed on this system.
    echo Please install Docker Desktop from:
    echo https://www.docker.com/products/docker-desktop
    echo.
    pause
    exit /b
)

echo Docker detected successfully.
echo.

echo Building Docker image...
docker build -t wizeline-ml .

echo Running container...
docker run -p 8000:8000 wizeline-ml

pause