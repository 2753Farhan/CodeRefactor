# Run bash test in Git Bash or WSL
# Creates a few sample .txt files and runs both scripts

Write-Host "Generating sample text files..."
$folder = Join-Path -Path $PWD -ChildPath "examples/bash"
Set-Location $folder

# Create sample files
"one`nline`nthree" > file1.txt
"line1`nline2" > file2.txt

Write-Host "Running original script (may invoke wc many times):"
bash ./count_lines_original.sh | Sort-Object
Write-Host "Running refactored script (single wc invocation):"
bash ./count_lines_refactored.sh | Sort-Object

Set-Location $PWD
