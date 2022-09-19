function getIP{
    (Get-NetIPAddress).ipv4address | Select-String "192*"
    }
function getUSER{
    whoami
}
function getHOST{
    hostname
    }
function getPSMV{
    $Host.Version.Major
    }
Function getDATE{
    Get-Date -format "dddd MM/dd/yyyy"
    }


$IP = getIP
$HOSTNAME = getHOST
$PSMV = getPSMV
$date = getDATE
$user = getUSER

echo("This machine's IP is $IP. User is $user. Hostname is $HOSTNAME. PowerShell Version $PSMV. Today's Date is $date.") | out-file -FilePath C:\IT-3080c-Scripts\powershell\sysinfo.txt


