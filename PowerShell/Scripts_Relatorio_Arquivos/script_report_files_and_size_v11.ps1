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

$estilos = get-Content ".\css\styles.css"
$styleTag= "<style>" + $estilos + "</style>" #Concatenação de String
$tituloPagina = "Relatório de Scripts em Migração"
$tituloBody = "<h1> $tituloPagina </h1>" #Interpolação de String no PowerShell

$resultado | ConvertTo-Html -Head $styleTag -Title $tituloPagina -Body $tituloBody | Out-File ".\relatorios\relatorio_v11.html" #Out-File exporta