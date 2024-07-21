#Melhorando o código usando variaveis

$nameExpr = "Name"
$lengthExpr = { "{0:N2}KB" -f ($_.Length / 1KB) }

$params = ($nameExpr, $lengthExpr)


gci -Recurse -File |
    ? Name -like "*_migrando_*" |
    Select-Object $params

# (1, 2, 3).GetType().name  -> retorna -> Object[] -> Que é um Array
# (1).GetType().name  -> retorna -> Int32 -> Número Inteiro
# (,1).GetType().name  -> retorna -> Object[] -> Que é um Array
# @(1).GetType().name  -> retorna -> Object[] -> Que é um Array
# O arroba diz que é um array
