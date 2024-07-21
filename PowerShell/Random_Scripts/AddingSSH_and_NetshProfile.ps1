# Ativar administrador
net user administrador /active:yes

# Definir senha pro administrador
$PASSWORD= ConvertTo-SecureString -AsPlainText -Force -String Hy@Brazil934
Set-LocalUser -Name "Administrador" -Password $PASSWORD

# Senha nunca expira pra todos os usuários
Set-LocalUser -Name "Administrador" -PasswordNeverExpires 1

# Baixar o arquivo de configuração

Invoke-WebRequest -Uri "http://10.0.0.73:8000/hybrazil.xml" -Outfile $home\hybrazil.xml

netsh wlan add profile filename=$home\hybrazil.xml

if(!(Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*')){
    # Install the OpenSSH Client
    Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
    Write-host "OpenSSH Client installed"
    # Install the OpenSSH Server
    Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
    Write-host "OpenSSH Server installed"
}else{
    Write-host "OpenSSH is already installed"
}

# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
}