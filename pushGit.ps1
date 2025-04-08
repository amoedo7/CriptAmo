# Configuración
$Username = "amoedo7"
$Repo = "CriptAmo"
$Branch = "main"
$Token = $env:GH_TOKEN

if (-not $Token) {
    Write-Host "[❌] GH_TOKEN no está definido en el entorno." -ForegroundColor Red
    Write-Host "Usá: `$env:GH_TOKEN = 'tu_token'" -ForegroundColor Yellow
    exit 1
}

# Mostrar estado
Write-Host "`n🔄 Preparando para hacer push al repositorio..." -ForegroundColor Cyan

# Construir URL con token
$Remote = "https://${Username}:${Token}@github.com/${Username}/${Repo}.git"

# Inicializar git si es necesario
if (-not (Test-Path ".git")) {
    git init
    git branch -M $Branch
    git remote add origin $Remote
} else {
    git remote set-url origin $Remote
}

# Agregar y hacer commit
git add .
$Fecha = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "🔁 Subida automática desde PowerShell - $Fecha"

# Hacer push
git push -u origin $Branch

# Confirmación
Write-Host "`n✅ ¡Push completado exitosamente!" -ForegroundColor Green
