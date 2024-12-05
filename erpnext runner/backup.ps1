$containerId = "e46c8da2d88b"
$siteName = "frontend"
$backupDir = "/home/frappe/frappe-bench/sites/$siteName/private/backups"
$destDir = "S:\New"

# Run the backup command inside the Docker container
docker exec $containerId /bin/bash -c "bench --site $siteName backup"

# Check if the backup command was successful
if ($LASTEXITCODE -eq 0) {
    Write-Host "Backup successful. Copying backup files to destination." -ForegroundColor Green

    # Copy the backup files from the container to the host machine
    docker cp "${containerId}:${backupDir}" "${destDir}"

    # Check if the copy command was successful
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Backup files copied successfully to $destDir." -ForegroundColor Green
    }
    else {
        Write-Host "Failed to copy backup files to $destDir." -ForegroundColor Red
        exit 1
    }
}
else {
    Write-Host "Backup command failed." -ForegroundColor Red
    exit 1
}
