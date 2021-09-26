@echo off
set /P name="Enter file name "
javac %name%.java
java %name%
@pause