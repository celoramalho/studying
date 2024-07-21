#PowerShell Function to copy permissions between Folders in SharePoint Online
Function Copy-PnPFolderPermissions {
    [cmdletbinding()]
    param(
        [Parameter(Mandatory = $True)] [string] $WebURL,
        [Parameter(Mandatory = $True)] [string] $SourceFolderURL,
        [Parameter(Mandatory = $True)] [string] $TargetFolderURL,
        [Parameter(Mandatory = $False)] [Bool] $AppendToExisting = $True
    )
    Try {
        #Connect to PnP Online
        Connect-PnPOnline -Url $WebURL -Interactive
 
        #Get the Web
        $Web = Get-PnPweb
        $Ctx = Get-PnPContext
 
        #Get Source and Target Folders
        $SourceFolderItem = Get-PnPFolder -Url $SourceFolderURL -Includes ListItemAllFields.HasUniqueRoleAssignments
        $SourceFolder = $SourceFolderItem.ListItemAllFields
        $TargetFolderItem = Get-PnPFolder -Url $TargetFolderURL -Includes ListItemAllFields.HasUniqueRoleAssignments
        $TargetFolder = $TargetFolderItem.ListItemAllFields
 
        #if permissions are Inherited in Target Folder, Break the Inheritance
        If (!$TargetFolder.HasUniqueRoleAssignments) {
            If ($AppendToExisting -eq $True) {
                #Break Folder permissions - keep all existing permissions & Clear Item level permissions
                $TargetFolder.BreakRoleInheritance($True, $False)
            }
            else {
                $TargetFolder.BreakRoleInheritance($False, $False)
            }
        }
        Else {
            #If the Folder has unique Permissions already
            If ($AppendToExisting -eq $False) {
                $TargetFolder.ResetRoleInheritance()
                $TargetFolder.BreakRoleInheritance($False, $False)
            }
        }
        Invoke-PnPQuery
 
        #Get all permissions assigned to the source folder
        $SourceRoleAssignments = Get-PnPProperty -ClientObject $SourceFolder -Property RoleAssignments
  
        #Copy Source Folder permissions to Destination Folder
        ForEach ($RoleAssignment in $SourceRoleAssignments) {
            #Get RoleDefinitions of the Role Assignment
            Get-PnPProperty -ClientObject $RoleAssignment -Property RoleDefinitionBindings, Member
 
            #Leave the Hidden permissions
            If ($RoleAssignment.Member.IsHiddenInUI -eq $False) {
                $SourcePermissions = $RoleAssignment.RoleDefinitionBindings | Where-Object { $_.Name -notin ("Limited Access") }
                $PermissionLevels = ($SourcePermissions | Select-Object -ExpandProperty Name) -join "; "
 
                If ($SourcePermissions -ne $null) {
                    #Add Source Folder's Permission Level to the Target Folder
                    $RoleDefBindings = New-Object Microsoft.SharePoint.Client.RoleDefinitionBindingCollection($Ctx)
                    ForEach ($RoleDefinition in $SourcePermissions) {
                        $RoleDefBindings.Add($RoleDefinition)
                    }
                    $Permissions = $TargetFolder.RoleAssignments.Add($RoleAssignment.Member, $RoleDefBindings)
                    $TargetFolder.Update()
                    Invoke-PnPQuery
                    Write-host "Copied '$($RoleAssignment.Member.Title)' with Permissions '$PermissionLevels'"
                }
            }
        }
    }
    Catch {
        write-host -f Red "Error Copying Folder Permissions!" $_.Exception.Message
    }
}
$WebURL = "https://hybrazil.sharepoint.com/sites/HYBRAZIL_SOLAR"
Connect-PnPOnline -Url $WebURL -Interactive
#$WebURL = read-host "Web URL [Ex: https://crescent.sharepoint.com/sites/Marketing]: "
 
#Server Relative URLs of Source and Target Folders
#$SourceFolderURL = read-host "Source Folder URL [Ex: /sites/Marketing/Shared Documents/New]: "
#$TargetFolderURL = read-host "Target Folder URL [Ex: /sites/Marketing/Shared Documents/New]: "
 
#Set Parameters
$FolderSource = "/Shared Documents/07 - PROJETOS/FV009 - CORRENTES-PE - 2MW"
$FolderToIterate = "/Shared Documents/07 - PROJETOS"

#Call the function to copy Folder permissions
#Copy-PnPFolderPermissions -WebURL $WebURL -SourceFolderURL $SourceFolderURL -TargetFolderURL $TargetFolderURL

$FoldersToPastePermission = Get-PnPFolderItem -FolderSiteRelativeUrl $FolderToIterate -ItemType Folder | Where-Object ServerRelativeUrl -Match "/sites/HYBRAZIL_SOLAR/Shared Documents/07 - PROJETOS/FV010 - BOM JESUS DA LAPA-BA 5MW*"
$FoldersToCopyPermission = Get-PnPFolderItem -FolderSiteRelativeUrl $FolderSource -ItemType Folder

# $FoldersToCopyPermission = $FoldersToCopyPermission | select -First 9

#$ListaDeTeste2 | Select-Object Name,{$_.Name.Split('/')[-1]}

ForEach ($FolderPasteFor in $FoldersToPastePermission) { 
    $relative_path = $FolderPasteFor.ServerRelativeUrl.Split("/", 4)[-1]
    $pastas = Get-PnPFolderItem -FolderSiteRelativeUrl $relative_path -ItemType Folder
    # $temp = ($FoldersToCopyPermission | Where Name -Match $FolderPasteFor.Name)[0].ServerRelativeUrl
    forEach ($pasta in $pastas) {
        if ($pasta.ServerRelativeUrl -Match ("FV010")){
            $temp3 = ($FoldersToCopyPermission | where Name -Match $pasta.Name).ServerRelativeUrl.Split("/", 4)[-1]
            $tempcola = $pasta.ServerRelativeUrl.Split("/", 4)[-1]
            Copy-PnPFolderPermissions -WebURL $WebURL -SourceFolderURL $temp3 -TargetFolderURL $tempcola
            Write-Host $temp3 "Copied to" $pasta.ServerRelativeUrl
            Write-Host $pasta.ServerRelativeUrl
        }
    }
}
#Write-Host $FolderFor | Select-Object ServerRelativeUrl Copied to: $FolderPasteFor | Select-Object ServerRelativeUrl
# Copy-PnPFolderPermissions -WebURL $WebURL -SourceFolderURL $SourceFolderURL -TargetFolderURL $TargetFolderURL
    

#Read more: https://www.sharepointdiary.com/2021/11/copy-permissions-from-one-folder-to-another-in-sharepoint-online-using-powershell.html#ixzz84WIzpawY




