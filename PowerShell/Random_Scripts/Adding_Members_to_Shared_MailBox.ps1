Connect-ExchangeOnline



Function Add_mailbox_Users {
    $shared_mailbox_options = read-host "Deseja adicionar um colaborador/grupo a um grupo de caixas de e-mail ou apenas a uma especifica? `n[1] - Caixa de e-mail especifica \ `n[2] - Grupo de caixas de e-mail`n"


    if ($shared_mailbox_options -eq 2) {
        $shard_mailbox_groups_options = read-host "Qual grupo de caixas de e-mail você deseja adicionar o colaborador? `n [1] Relacionamento Concessionarias"

        #Adicionar a caixa de e-mail aos relacionamentos com concessionarias 
        if ($shard_mailbox_groups_options -eq 1) { 
            Get-Mailbox -Filter { Name -like "*relacionamento*" -Or Name -like "*Consórcio*" }
            Write-Host "Irei sincronizar os membros do Grupo [FIT Energia - Relacionamento Concesionaria] com as caixas abaixo."
            $RC_Debs_Shared_Mailbox = Get-Mailbox -Filter { Name -like "*relacionamento*" -Or Name -like "*Consórcio*" }

            ForEach ($shared_mail_box in $RC_Debs_Shared_Mailbox) {
                $shared_mail_box_members = Get-MailboxPermission -Identity $shared_mail_box  | Select-Object User | Where-object User -like "*.com*"
                Write-Host $shared_mail_box_members

            }
        }
    }
}

Add_mailbox_Users