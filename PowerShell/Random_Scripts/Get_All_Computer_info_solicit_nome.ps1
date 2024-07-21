$nomecolaborador = read-host "Nome do colaborador "

$nomepasta = $nomecolaborador + "_relatorio_maquina_hybrazil"
New-Item -Path $HOME\$nomepasta -ItemType Directory
$nomearquivocomp =  $env:COMPUTERNAME + "_" + $nomecolaborador + "_ComputerInfo_HyBrazil"
$nomearquivoadapt = $env:COMPUTERNAME + "_" + $nomecolaborador + "_NetAdapter_HyBrazil"
$nomearquivodisk = $env:COMPUTERNAME + "_" + $nomecolaborador + "_PhysicalDisk_HyBrazil"
$nomearquivogpu = $env:COMPUTERNAME + "_" + $nomecolaborador + "_VideoGpu_HyBrazil"
$nomearquivoram = $env:COMPUTERNAME + "_" + $nomecolaborador + "_Ram_HyBrazil"
$nomearquivoram2 = $env:COMPUTERNAME + "_" + $nomecolaborador + "_Ram_Complemento_HyBrazil"



Get-ComputerInfo | ConvertTo-Json | Out-File -FilePath $HOME\$nomepasta\$nomearquivocomp.json

Get-NetAdapter | ConvertTo-Json | Out-File -FilePath $HOME\$nomepasta\$nomearquivoadapt.json

wmic path win32_VideoController get name | ConvertTo-Json | Out-File -FilePath $HOME\$nomepasta\$nomearquivogpu.json

wmic memorychip list full | ConvertTo-Json | Out-File -FilePath $HOME\$nomepasta\$nomearquivoram.json

Get-CimInstance -ClassName Win32_PhysicalMemory | ConvertTo-Json | Out-File -FilePath $HOME\$nomepasta\$nomearquivoram2.json

Get-PhysicalDisk | ConvertTo-Json | Out-File -FilePath $HOME\$nomepasta\$nomearquivodisk.json