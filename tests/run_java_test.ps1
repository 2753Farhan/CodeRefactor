# Run Java tests (requires Java 21 to use switch expressions with pattern matching)
$src = Join-Path $PWD "..\examples\java"
Push-Location $src

javac AnimalSoundOriginal.java
java AnimalSoundOriginal > orig.txt

javac AnimalSoundRefactored.java
java AnimalSoundRefactored > refactored.txt

Write-Host "Original output:"; Get-Content orig.txt
Write-Host "Refactored output:"; Get-Content refactored.txt

Pop-Location
