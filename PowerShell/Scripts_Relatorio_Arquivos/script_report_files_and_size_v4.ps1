# ou quebrar em linhas usando backtick ->   `  não esqueça do espaço antes do backtick
gci -Recurse -File `
| ? Name -Like "*_migrando_*" `
| select `
Name,
{ "{0:N2}KB" -f ($_.Length / 1KB) }