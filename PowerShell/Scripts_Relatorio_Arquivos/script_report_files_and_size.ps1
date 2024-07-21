$nameExpr = @{
    Label= "Nome"
    Expression= { $_.Name}
}

$lengthExprr = @{
Label= "Tamanho"
Expression= { "{0:N2}KB" -f ($_.Length / 1KB) }
}

$params = ($nameExpr, $lengthExpr)

$resultado =
gci -Recurse -File | 
    ? Name -Like "*_migrando_*" |
    select $params

$resultado