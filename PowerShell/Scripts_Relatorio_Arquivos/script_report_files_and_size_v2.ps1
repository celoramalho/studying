<# $_ 
É uma variável existente nos scriptsblocks usados em cmdlets de iteração, como por exemplo, o Where-Object

$_
#>
<#
seguir o Padrão: FILTER LEFT, FORMAT RIGHT
Filtrar na esquerda e formatar na direita
#>

Get-ChildItem -Recurse -File | Where-Object Name -Like "*_migrando_*" | Select-Object Name, { "{0:N2}KB" -f ($_.Length / 1KB) }