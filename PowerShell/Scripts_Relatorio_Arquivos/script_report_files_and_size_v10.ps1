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

$resultado | ConvertTo-Html | Out-File ".\relatorios\relatorio_v10.html" #ConvertTo-Html Converte em HTML