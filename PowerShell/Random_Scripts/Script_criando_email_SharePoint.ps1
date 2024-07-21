Connect-ExchangeOnline
Function CreateScp-SharedMailBox {
    [cmdletbinding()]
    param(
    [Parameter(Mandatory = $True)] [string] $identity
    )
    $aliasmail = $identity.Split("@")[0]
    $nameemail = (Get-Culture).TextInfo.ToTitleCase($aliasmail.Split(".")[1])
    #Write-Host $identity "\n" $aliasmail "\n" $nameemail
    #write-host "Alias:$alias23-  -Nome:$nome"
    Try{
        New-Mailbox -Shared -Name $nameemail -DisplayName $nameemail -PrimarySmtpAddress $identity -Alias $aliasmail
        Write-Host "Shared Mail Box $identity created" 
    }
    Catch {
        write-host -f Red "Error Creating Shared MailBox ("$identity")" $_.Exception.Message
    }
    Try{
        Add-MailboxPermission -Identity $identity -User felipe.fonseca@hybrazil.com -AccessRights FullAccess -InheritanceType All
        Add-MailboxPermission -Identity $identity -User marco.passos@hybrazil.com -AccessRights FullAccess -InheritanceType All
        Add-MailboxPermission -Identity $identity -User bernardo.oliveira@hybrazil.com -AccessRights FullAccess -InheritanceType All
        Add-MailboxPermission -Identity $identity -User wesley.pereira@hybrazil.com -AccessRights FullAccess -InheritanceType All
        Add-MailboxPermission -Identity $identity -User cor@hybrazil.com -AccessRights FullAccess -InheritanceType All
        Add-MailboxPermission -Identity $identity -User Clezio.Silva@hybrazil.com -AccessRights FullAccess -InheritanceType All
        Add-MailboxPermission -Identity $identity -User Edmundo.Soares@hybrazil.com -AccessRights FullAccess -InheritanceType All
        Add-MailboxPermission -Identity $identity -User Philippe.Machado@hybrazil.com -AccessRights FullAccess -InheritanceType All
    }
    Catch {
        write-host -f Red "Error Adding a member to de Shared Mail Box ("$identity")" $_.Exception.Message
    }
    #Set-Mailbox -Identity Sales -GrantSendOnBehalfTo MarketingSG
    #Add-MailboxPermission -Identity Sales -User MarketingSG -AccessRights FullAccess -InheritanceType All
}
#cgh.cachoeirinha@hybrazil.com

$emailsboxes = @("cgh.mariadafe@hybrazil.com",
    "cgh.saltodoscravos@hybrazil.com",
    "cgh.itajuba@hybrazil.com",
    "cgh.pitangas@hybrazil.com",
    "cgh.altobrejauba@hybrazil.com",
    "cgh.brejauba@hybrazil.com",
    "cgh.correntegrande@hybrazil.com",
    "cgh.farias@hybrazil.com",
    "cgh.antoniodias@hybrazil.com",
    "cgh.durande@hybrazil.com",
    "cgh.simonesia@hybrazil.com",
    "cgh.antonioprado@hybrazil.com",
    "cgh.vermelhovelho@hybrazil.com",
    "cgh.bicuiba@hybrazil.com",
    "cgh.areao@hybrazil.com",
    "pch.saoluiz@hybrazil.com",
    "cgh.vistaverde@hybrazil.com",
    "cgh.formoso@hybrazil.com",
    "cgh.pedralavada@hybrazil.com",
    "cgh.serranegra@hybrazil.com",
    "pch.lagoagrande@hybrazil.com",
    "pch.riachopreto@hybrazil.com",
    "pch.manuelalves@hybrazil.com",
    "pch.fazendavelha@hybrazil.com")
#>
ForEach ($identity in $emailsboxes){
    #write-host "$mailbox"
    CreateScp-SharedMailBox -identity $identity
}


<#

cgh.espraiado@hybrazil.com 
cgh.cachoeirinha@hybrazil.com
cgh.limoeiro@hybrazil.com
cgh.pardo@hybrazil.com
cgh.mariadafe@hybrazil.com
cgh.saltodoscravos@hybrazil.com
cgh.itajuba@hybrazil.com
cgh.pitangas@hybrazil.com
cgh.altobrejauba@hybrazil.com
cgh.brejauba@hybrazil.com
cgh.correntegrande@hybrazil.com
cgh.farias@hybrazil.com
cgh.antoniodias@hybrazil.com
cgh.durande@hybrazil.com
cgh.simonesia@hybrazil.com
cgh.antonioprado@hybrazil.com
cgh.vermelhovelho@hybrazil.com
cgh.bicuiba@hybrazil.com
cgh.areao@hybrazil.com
pch.saoluiz@hybrazil.com
cgh.vistaverde@hybrazil.com
cgh.formoso@hybrazil.com
cgh.pedralavada@hybrazil.com
cgh.serranegra@hybrazil.com
pch.lagoagrande@hybrazil.com
pch.riachopreto@hybrazil.com
pch.manuelalves@hybrazil.com
pch.fazendavelha@hybrazil.com



-WebURL $WebURL -SourceFolderURL $temp3 -TargetFolderURL $tempcola
#>