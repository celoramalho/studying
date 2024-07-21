$todos_os_itens = Get-ChildItem -Recurse #gci is an alias to Get-Child-Item

Write-Output "Quantidade de todos os itens dessa pasta: " #echo is an alias to Write-Output
$todos_os_itens.length
$todos_os_arquivos = Get-ChildItem -Recurse -File

Write-Output "Quantidade de todos os arquivos dessa pasta: "
$todos_os_arquivos.length
