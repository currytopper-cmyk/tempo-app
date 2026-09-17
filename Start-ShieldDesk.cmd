@echo off
cd /d "%~dp0"
where node >nul 2>nul
if errorlevel 1 (
  echo Install the current Node.js LTS on this computer, then open this file again.
  pause
  exit /b 1
)
echo Installing ShieldDesk's dependencies...
call npm ci
if errorlevel 1 (
  echo Installation did not finish. Check your internet connection and try again.
  pause
  exit /b 1
)
echo Open Expo Go on your phone. Keep your phone and computer on the same Wi-Fi.
call npm start
pause
