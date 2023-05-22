Write-Host "What is your github username?"
$username = Read-Host
Write-Host "What is your e-mail connected to $username"
$email = Read-Host

git config --global user.name "$username"
git config --global user.email "$email"

