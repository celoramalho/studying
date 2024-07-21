<#
O PowerShell possui algumas variáveis de preferência para
definirmos seu comportamento em situações específicas em nosso contexto.
Se queremos que, no erro de qualquer comando de um script,
o PowerShell pare imediatamente sua execução,
devemos definir a variável de preferência $ErrorActionPreference para “Stop”
 $ErrorActionPreference  = Stop

Break – Insira o depurador quando ocorrer um erro ou quando uma exceção for gerada.
Continuar: (Padrão) Exibe a mensagem de erro e continua a execução.

Ignorar: suprime a mensagem de erro e continua a executar o comando.
O valor Ignorar destina-se ao uso por comando,
não ao uso como preferência salva.
Ignorar não é um valor válido
para a $ErrorActionPreference variável.

Consultar: Exibe a mensagem de erro e pergunta se você deseja continuar.

SilentlyContinue: Sem efeito. A mensagem de erro não é
exibida e a execução continua sem interrupção.
Parar: Exibe a mensagem de erro e interrompe a execução.
Além do erro gerado, o valor Stop gera um objeto
ActionPreferenceStopException para o fluxo de erros.

Suspender: suspende automaticamente um trabalho de fluxo de
trabalho para permitir uma investigação mais aprofundada.
Após a investigação, o fluxo de trabalho pode ser retomado.
O valor Suspend destina-se ao uso por comando,
não ao uso como preferência salva.
Suspend não é um valor válido para a $ErrorActionPreference variável.
#>
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

$resultado