####
## List Local Admin Users
####
##
## This script gathers all members of the LocalAdmin group on Windows systems with the SID S-1-5-32-544
##
## Version: 2.1.0
##
## Date: 2023-07-26
##
## Author: D. Lothmann

#Script for CheckMK to List Local Admin Users

$CMK_VERSION = "2.2.0"

Write-Output -InputObject "<<<list_local_admin_user>>>"

if((Get-WindowsFeature AD-Domain-Services).Installed){
	return '3'
}

if(Get-LocalGroupMember -SID S-1-5-32-544){
	$Member = Get-LocalGroupMember -SID S-1-5-32-544 | Select-Object -ExpandProperty Name

	$Member = [System.String]::Join(", ", $Member)

	$output = $Member


}else{
	$output = '2'
}
	return $output