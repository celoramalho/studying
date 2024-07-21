# Input Parameters  

$siteURL= read-host "Site Url [Ex: https://pacman.sharepoint.com/sites/Games]"  

$folder= read-host "Folder [Ex: /Folder]"

 

# Loop through to get all the folders and subfolders  

Function GetFolders($folderUrl)  

{      
    $folderColl=Get-PnPFolderItem -FolderSiteRelativeUrl $folderUrl -ItemType Folder  

    # Loop through the folders  

    foreach($folder in $folderColl)  

    {                      

       $newFolderURL= $folderUrl+"/"+$folder.Name  

       write-host -ForegroundColor Green $folder.Name " - " $newFolderURL  

       # Call the function to get the folders inside folder  

       GetFolders($newFolderURL)  

    }          

}  

 

# Connect to SharePoint Online site  

Connect-PnPOnline -Url $siteURL -Credentials (Get-Credential)  

 

# Call the functions  

GetFolders($folder)  