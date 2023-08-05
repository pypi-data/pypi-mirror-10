@echo off
cls

rem Copyright 2009-2015 Joao Carlos Roseta Matos
rem
rem This program is free software: you can redistribute it and/or modify
rem it under the terms of the GNU General Public License as published by
rem the Free Software Foundation, either version 3 of the License, or
rem (at your option) any later version.
rem
rem This program is distributed in the hope that it will be useful,
rem but WITHOUT ANY WARRANTY; without even the implied warranty of
rem MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
rem GNU General Public License for more details.
rem
rem You should have received a copy of the GNU General Public License
rem along with this program.  If not, see <http://www.gnu.org/licenses/>.

rem Usage:
rem
rem build - builds sdist and bdist_wheel or just sdist if app type is module
rem build src - builds sdist
rem build whl - builds bdist_wheel
rem build egg - builds bdist_egg
rem build win - builds bdist_wininst
rem build py2exe - builds windows exe on Py2 only for the moment
rem build cxf - not working for the moment
rem build pypi - uploads dists to PyPI
rem build pypitest - uploads dists to test
rem build test - run tests
rem build clean - clears dirs and files
rem build doc - builds doc
rem
rem Requires:
rem Python, Sphinx, Miktex, pytest, pytest-cov, twine, py2exe, cxf.

set OLDPATH=%PATH%

python setup_utils.py app_name()
if not exist app_name.txt goto :EXIT
for /f "delims=" %%f in (app_name.txt) do set PROJECT=%%f
del app_name.txt

if "%1"=="pypi" goto :PYPI
if "%1"=="pypitest" goto :PYPITEST

echo.
echo *** Cleanup and update basic info files
echo.
if exist app_ver.txt del app_ver.txt
if exist app_name.txt del app_name.txt
if exist app_type.txt del app_type.txt
if exist py_ver.txt del py_ver.txt
if exist *.pyc del *.pyc
if exist build rd /s /q build
if exist dist rd /s /q dist
if exist test\*.pyc del test\*.pyc

python setup_utils.py app_ver()
if not exist app_ver.txt goto :EXIT
for /f "delims=" %%f in (app_ver.txt) do set APP_VER=%%f
del app_ver.txt

if exist %PROJECT%\*.pyc del %PROJECT%\*.pyc
if exist %PROJECT%.egg-info rd /s /q %PROJECT%.egg-info
if exist %PROJECT%-%APP_VER% rd /s /q %PROJECT%-%APP_VER%
if exist %PROJECT%\doc rd /s /q %PROJECT%\doc

if "%1"=="clean" goto :EXIT

python setup_utils.py app_type()
if not exist app_type.txt goto :EXIT
for /f "delims=" %%f in (app_type.txt) do set PROJ_TYPE=%%f
del app_type.txt

python setup_utils.py py_ver()
if not exist py_ver.txt goto :EXIT
for /f "delims=" %%f in (py_ver.txt) do set PY_VER=%%f
del py_ver.txt

if "%PROJ_TYPE%"=="application" copy /y appinfo.py %PROJECT% > nul

copy /y LICENSE.rst %PROJECT%\LICENSE.txt > nul
copy /y AUTHORS.rst %PROJECT%\AUTHORS.txt > nul
copy /y ChangeLog.rst %PROJECT%\ChangeLog.txt > nul

python setup_utils.py upd_usage_in_readme()
copy /y README.rst %PROJECT%\README.txt > nul

if "%1"=="doc" goto :DOC

:TEST
if not exist test goto :DOC
echo.
echo *** Test
echo.

rem *** source doctest ***
rem python -m doctest %PROJECT%\%PROJECT%.py

rem *** doctest ***
rem python -m doctest -v test\test.rst

rem *** unittest ***
rem ren test\test_%PROJECT%.py pytest_test_%PROJECT%.py
rem ren test\doctest_test_%PROJECT%.py test_%PROJECT%.py
rem python -m unittest discover -v -s test
rem ren test\test_%PROJECT%.py doctest_test_%PROJECT%.py
rem ren test\pytest_test_%PROJECT%.py test_%PROJECT%.py

py.test --cov-report term-missing --cov %PROJECT% -v test
if ERRORLEVEL==1 goto :EXIT

if "%1"=="test" goto :EXIT

:DOC
if not exist doc goto :NO_DOC
pause

echo.
echo *** Sphinx
echo.
set SPHINXOPTS=-E
set PATH=d:\miktex\miktex\bin;%PATH%

copy /y README.rst README.rst.bak > nul
cd doc
cmd /c make clean

python ..\setup_utils.py remove_copyright()
cmd /c make html
if not exist ..\%PROJECT%\doc md ..\%PROJECT%\doc
xcopy /y /e _build\html\*.* ..\%PROJECT%\doc\ > nul

cmd /c make clean

if not exist index.ori ren index.rst index.ori
python ..\setup_utils.py prep_rst2pdf()

cmd /c make latex
cd _build\latex
pdflatex.exe %PROJECT%.tex
echo ***
echo *** Repeat to correct references
echo ***
pdflatex.exe %PROJECT%.tex
copy /y %PROJECT%.pdf ..\..\..\%PROJECT%\doc > nul
cd ..\..

if exist index.rst del index.rst
ren index.ori index.rst

cmd /c make clean
cd ..
del README.rst
ren README.rst.bak README.rst

python setup_utils.py create_doc_zip()

if "%1"=="doc" goto :EXIT

:NO_DOC
pause
cls

if "%1"=="whl" goto :WHL
if "%1"=="egg" goto :EGG
if "%1"=="win" goto :WIN
if "%1"=="cxf" goto :CXF
if "%1"=="py2exe" goto :PY2EXE

:SRC
python setup_utils.py sleep(5)
echo.
echo *** sdist build
echo.
python setup.py sdist
echo.
echo *** End of sdist build. Check for errors.
echo.
if "%PROJ_TYPE%"=="module" goto :MSG
if "%1"=="src" goto :MSG
pause

:WHL
echo.
echo *** bdist_wheel build
echo.
python setup.py bdist_wheel
echo.
echo *** End of bdist_wheel build. Check for errors.
echo.
if "%1"=="whl" goto :MSG
if "%1"=="" goto :MSG
pause

:EGG
echo.
echo *** bdist_egg build
echo.
python setup.py bdist_egg
echo.
echo *** End of bdist_egg build. Check for errors.
echo.
if "%1"=="egg" goto :MSG
pause

:WIN
echo.
echo *** bdist_wininst build
echo.
python setup.py bdist_wininst
echo.
echo *** End of bdist_winist build. Check for errors.
echo.

:MSG
echo.
echo *** If there were filesystem errors (eg. directory not empty), random syntax or unicode errors, try repeating the build up to 3 times. At least on my system that works.
echo.
goto :EXIT

:CXF
echo.
echo *** CXF
echo.
echo Not working yet...
rem python cxf_setup.py build bdist_msi
rem python cxf_setup.py build_exe
rem cxfreeze cxf_setup.py build_exe
rem echo ***
rem echo *** Copy datafiles
rem echo ***
rem copy build\exe.win32-%PY_VER%\%PROJECT%\*.* build\exe.win32-%PY_VER%
goto :EXIT

:PY2EXE
echo.
echo *** PY2EXE
echo.
python setup_py2exe.py py2exe
if exist dist\__main__.exe ren dist\__main__.exe %PROJECT%.exe
goto :EXIT

:PYPI
echo.
echo *** PyPI: Register and upload
echo.
python setup.py register -r pypi
twine upload dist/*
rem *** old way ***
rem if "%PROJ_TYPE%"=="module" python setup.py sdist upload -r pypi
rem if "%PROJ_TYPE%"=="module" goto :EXIT
rem rem python setup.py sdist bdist_egg bdist_wininst bdist_wheel upload -r pypi
rem python setup.py sdist bdist_wheel upload -r pypi

if exist %PROJECT%\doc python setup.py register upload_docs --upload-dir=%PROJECT%\doc
goto :EXIT

:PYPITEST
echo.
echo *** PYPITEST: Register and upload
echo.
python setup.py register -r test
twine upload -r test dist/*
rem *** old way ***
rem if "%PROJ_TYPE%"=="module" python setup.py sdist upload -r test
rem if "%PROJ_TYPE%"=="module" goto :EXIT
rem rem python setup.py sdist bdist_egg bdist_wininst bdist_wheel upload -r test
rem python setup.py sdist bdist_wheel upload -r test

:EXIT
set PATH=%OLDPATH%
set OLDPATH=
set PY_VER=
set APP_VER=
set PROJ_TYPE=
set PROJECT=
set SPHINXOPTS=
