$nomearquivocomp =  $env:COMPUTERNAME + "_" + $env:USERNAME + "_ComputerInfo_HyBrazil"
$nomearquivoadapt = $env:COMPUTERNAME + "_" + $env:USERNAME + "_NetAdapter_HyBrazil"
$nomearquivodisk = $env:COMPUTERNAME + "_" + $env:USERNAME + "_PhysicalDisk_HyBrazil"
$nomearquivogpu = $env:COMPUTERNAME + "_" + $env:USERNAME + "_VideoGpu_HyBrazil"
$nomearquivoram = $env:COMPUTERNAME + "_" + $env:USERNAME + "_Ram_HyBrazil"



Get-ComputerInfo | ConvertTo-Json | Out-File -FilePath $HOME\$nomearquivocomp.json

Get-NetAdapter | ConvertTo-Json | Out-File -FilePath $HOME\$nomearquivoadapt.json

wmic path win32_VideoController get name | ConvertTo-Json | Out-File -FilePath $HOME\$nomearquivogpu.json

wmic memorychip list full | ConvertTo-Json | Out-File -FilePath $HOME\$nomearquivoram.json

Get-PhysicalDisk | ConvertTo-Json | Out-File -FilePath $HOME\$nomearquivodisk.json