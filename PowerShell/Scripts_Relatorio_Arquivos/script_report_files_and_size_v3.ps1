# ou com menos palavras:
gci -Recurse -File | ? Name -Like "*_migrando_*" | select Name, { "{0:N2}KB" -f ($_.Length / 1KB) }
