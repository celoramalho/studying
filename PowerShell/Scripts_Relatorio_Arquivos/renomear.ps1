$newname = "script_report_files_and_size_"

$files = gci -Recurse -File | 
    Where-Object { $_.Name -Like "*_relatorio_*" } | 
    Select-Object Name, @{Name='Final'; Expression = { $_.Name.Split("_")[5] }}

#
foreach ($file in $files) {
    Rename-Item "$($file.Name)" "$($newname + $file.Final)"
}
