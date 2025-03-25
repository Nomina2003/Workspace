@echo off
set WPY_PATH=..\WPy64-31290\python\python.exe
"%WPY_PATH%" -m ipykernel install --user --name "winpython" --display-name "WinPython"

pause
