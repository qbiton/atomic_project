@echo off
title Synchronizacja Partycji (Robocopy)
echo Trwa monitorowanie zmian... Nie zamykaj tego okna.
echo.

:: Ustawienia ścieżek
set zrodlo="I:\atomic_project"
set cel="D:\MloveMS\atomic_project"

:: Ustawienia wykluczeń (dodane Twoje foldery)
set wykluczenia="$Temp" ".git" ".tmp.drivedownload" ".tmp.driveupload"

:: Uruchomienie Robocopy z flagą /XD
robocopy %zrodlo% %cel% /MIR /Z /R:5 /W:5 /MT:32 /MON:1 /MOT:5 /V /TEE /XD %wykluczenia%