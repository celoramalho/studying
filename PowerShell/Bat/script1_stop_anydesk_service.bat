@ECHO OFF
echo Buscando serviço "AnyDesk" no computador "FITENERGIA-N01"
sc \\FITENERGIA-N01 query "AnyDesk" | find /i "estado" | find /i "running"

IF %ERRORLEVEL% NEQ 0 (
	echo Ops, serviço não executado no computador!
) ELSE (
	echo Parando serviço...
	sc \\FITENERGIA-N01 stop "AnyDesk" > NUL
	echo Serviço parado com Sucesso!
)