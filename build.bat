cd %~dp0

C:\Python27\Scripts\pyinstaller.exe -y supervisord.spec
del supervisord.zip
powershell.exe -nologo -noprofile -command "& { Add-Type -A 'System.IO.Compression.FileSystem'; [IO.Compression.ZipFile]::CreateFromDirectory('dist', 'supervisord.zip'); }"
