# pushGit.ps1

# Verifica si el token está presente
if (-not $env:GH_TOKEN) {
    Write-Host "❌ GH_TOKEN no está definido. Usá: `$env:GH_TOKEN = 'tu_token'"
    exit 1
}

# Datos del usuario y repo
$Username = "amoedo7"
$Repo = "CriptAmo"
$Remote = "https://${Username}:${env:GH_TOKEN}@github.com/${Username}/${Repo}.git"

# Git automático
git init
git add .
git commit -m "🔁 Subida automática desde PowerShell - $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
git branch -M main
git remote remove origin 2>$null
git remote add origin $Remote
git push -u origin main
