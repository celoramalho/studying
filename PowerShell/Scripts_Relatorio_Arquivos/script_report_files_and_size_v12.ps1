param($tipoDeExportacao)
$ErrorActionPreference = "Stop"

$nameExpr = @{
    Label= "Nome"
    Expression= { $_.Name}
}

$lengthExpr = @{
Label= "Tamanho"
Expression= { "{0:N2}KB" -f ($_.Length / 1KB) }
}

$params = ($nameExpr, $lengthExpr)

$resultado =
gci -Recurse -File | 
    ? Name -Like "*_migrando_*" |
    select $params

if ($tipoDeExportacao -eq "HTML") {
    $estilos = get-Content ".\styles.css"
    $styleTag= "<meta charset=`"UTF-8`"> <style> $estilos </style>" #Interpolação de String no PowerShell
    $tituloPagina = "Relatório de Scripts em Migração"
    $tituloBody = "<h1> $tituloPagina </h1>" 

    $resultado | ConvertTo-Html -Head $styleTag -Title $tituloPagina -Body $tituloBody |
    Out-File ".\relatorios\relatorio.html" #Out-File exporta

} elseif ($tipoDeExportacao -eq "JSON"){
    $resultado |
    ConvertTo-Json |
    Out-File ".\relatorios\relatorio.json"

} elseif ($tipoDeExportacao -eq "CSV"){
    $resultado |
    ConvertTo-Csv -Delimiter "," -NoTypeInformation |
    Out-File ".\relatorios\relatorio.CSV"
}