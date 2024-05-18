@echo off
echo.> switch.txt
echo startline1::: running = True :::endline1 >> switch.txt
echo startline2::: restarting_message = None :::endline2 >> switch.txt

echo -----------------------------
echo       Starting milFA...
echo -----------------------------
echo.

:loop
python files_checker.py
python main.py
IF %ERRORLEVEL% EQU 1 GOTO end
GOTO loop

:end
echo.> switch.txt
echo startline1::: running = False :::endline1 >> switch.txt
echo startline2::: restarting_message = None :::endline2 >> switch.txt

echo.
echo -----------------------------
echo  milFA has been switched off
echo -----------------------------