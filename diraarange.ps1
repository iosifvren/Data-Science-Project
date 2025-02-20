$sourceDirectory = "C:\Users\a880862\OneDrive - ATOS\Desktop\new proj" 
$destinationDirectory = Join-Path -Path $sourceDirectory -ChildPath "xlsx"

if (-Not (Test-Path -Path $sourceDirectory)) {
    Write-Host "The specified directory does not exist: $sourceDirectory"
    exit
}

if (-Not (Test-Path -Path $destinationDirectory)) {
    New-Item -ItemType Directory -Path $destinationDirectory | Out-Null
    Write-Host "Created directory: $destinationDirectory"
}

$xlsxFiles = Get-ChildItem -Path $sourceDirectory -Filter *.xlsx -File

if ($xlsxFiles.Count -eq 0) {
    Write-Host "No .xlsx files found in the directory: $sourceDirectory"
} else {
    foreach ($file in $xlsxFiles) {
        Move-Item -Path $file.FullName -Destination $destinationDirectory
        Write-Host "Moved file: $($file.Name) to $destinationDirectory"
    }

    Write-Host "All .xlsx files have been moved successfully!"
}