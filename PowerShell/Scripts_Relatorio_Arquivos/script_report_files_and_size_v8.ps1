#Assim não usamos o .add e declaramos nossa Hashtable e seus elementos em um bloco

$nameExpr = @{
    Label= "Nome"
    Expression= { $_.Name}
}

$lengthExpr = @{
Label= "Tamanho"
Expression= { "{0:N2}KB" -f ($_.Length / 1KB) }
}

$params = ($nameExpr, $lengthExpr)

gci -Recurse -File | 
    ? Name -Like "*_migrando_*" |
    select $params