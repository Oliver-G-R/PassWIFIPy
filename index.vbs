Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "index.exe" & Chr(34), 0
WshShell.Run chr(34) & "DISCLETTER:\ROOT\FILE.EXTENSION" & Chr(34), 0
Set WshShell = Nothing 