#PowerShell Function to copy permissions between Folders in SharePoint Online
Function Copy-PnPFolderPermissions
{
    [cmdletbinding()]
     param(
         [Parameter(Mandatory=$True)] [string] $WebURL,
         [Parameter(Mandatory=$True)] [string] $SourceFolderURL,
         [Parameter(Mandatory=$True)] [string] $TargetFolderURL,
         [Parameter(Mandatory=$False)] [Bool] $AppendToExisting = $True
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
        If(!$TargetFolder.HasUniqueRoleAssignments)
        {
            If($AppendToExisting -eq $True)
            {
                #Break Folder permissions - keep all existing permissions & Clear Item level permissions
                #Herdando
            }
            else
            {
                
            }
        }
        Else #If the Folder has unique Permissions already
        {
            If($AppendToExisting -eq $False)
            {
                #Unique permision
            }
        }
        Invoke-PnPQuery
 
        #Get all permissions assigned to the source folder
        $SourceRoleAssignments = Get-PnPProperty -ClientObject $SourceFolder -Property RoleAssignments
  
        #Copy Source Folder permissions to Destination Folder
        ForEach($RoleAssignment in $SourceRoleAssignments)
        {
            #Get RoleDefinitions of the Role Assignment
            Get-PnPProperty -ClientObject $RoleAssignment -Property RoleDefinitionBindings, Member
 
            #Leave the Hidden permissions
            If($RoleAssignment.Member.IsHiddenInUI -eq $False)
            {
                $SourcePermissions = $RoleAssignment.RoleDefinitionBindings | Where {$_.Name -notin("Limited Access")}
                $PermissionLevels = ($SourcePermissions | Select -ExpandProperty Name) -join "; "
 
                If($SourcePermissions -ne $null)
                {
                    #Add Source Folder's Permission Level to the Target Folder
                    $RoleDefBindings = New-Object Microsoft.SharePoint.Client.RoleDefinitionBindingCollection($Ctx)
                    ForEach($RoleDefinition in $SourcePermissions)
                    {
                        $RoleDefBindings.Add($RoleDefinition)
                    }
                    $Permissions = $TargetFolder.RoleAssignments.Add($RoleAssignment.Member,$RoleDefBindings)
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
 
#Set Parameters
$WebURL = read-host "Web URL [Ex: https://crescent.sharepoint.com/sites/Marketing]: "
 
#Server Relative URLs of Source and Target Folders
$SourceFolderURL = read-host "Source Folder URL [Ex: /sites/Marketing/Shared Documents/New]: "
$TargetFolderURL = read-host "Target Folder URL [Ex: /sites/Marketing/Shared Documents/New]: "
 
#Call the function to copy Folder permissions
Copy-PnPFolderPermissions -WebURL $WebURL -SourceFolderURL $SourceFolderURL -TargetFolderURL $TargetFolderURL


#Read more: https://www.sharepointdiary.com/2021/11/copy-permissions-from-one-folder-to-another-in-sharepoint-online-using-powershell.html#ixzz84WIzpawY