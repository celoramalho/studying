<# Hashtable
Indicado por -> @{}
#>

$nameExpr = @{}
$nameExpr.Add("Label", "Nome")
$nameExpr.Add("Expression", { $_.Name})#Script Block

$lengthExpr = @{}
$lengthExpr.Add("Label", "Tamanho")
$lengthExpr.Add("Expression", { "{0:N2}KB" -f ($_.Length / 1KB) })
$params = ($nameExpr, $lengthExpr)

gci -Recurse -File | 
    ? Name -Like "*_migrando_*" |
    select $params