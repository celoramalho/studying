# Ou usando o PIP no fim do comando

gci -Recurse -File | 
? Name -Like "*_migrando_*" |
select `
Name,
{ "{0:N2}KB" -f ($_.Length / 1KB) }