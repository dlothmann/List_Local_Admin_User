####
## List Local Admin Users
####
##
## This script gathers all members of the LocalAdmin group on Windows systems with the SID S-1-5-32-544
##
## Version: 1.0.0
##
## Date: 2023-07-21
##
## Author: D. Lothmann

#Script for CheckMK to List Local Admin Users

Write-Output "<<<list_local_admin_users>>>"

if((Get-WindowsFeature AD-Domain-Services).Installed){
	return '3 "Local Administrator Group Member" - Seems this is a domain controller. No Local Admin Group Available.'
}

if(Get-LocalGroupMember -SID S-1-5-32-544){
	$Member = Get-LocalGroupMember -SID S-1-5-32-544 | Select-Object -ExpandProperty Name

	$Member = [System.String]::Join(", ", $Member)

	$output = '0 "Local Administrator Group Member" - ' + "$($Member)"


}else{
	$output = '2 "Local Administrator Group Member" - No Group with SID S-1-5-32-544 found. Are you sure this is a windows?'
}
	return $output