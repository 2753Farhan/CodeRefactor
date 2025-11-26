param(
    [string]$input = "report.md",
    [string]$output = "report.pdf"
)

if (Get-Command pandoc -ErrorAction SilentlyContinue) {
    Write-Host "Running pandoc to convert $input to $output..."
    pandoc $input -o $output --pdf-engine=xelatex
    Write-Host "Output: $output"
} else {
    Write-Host "Pandoc is not installed. Please install Pandoc and a LaTeX engine, or use VS Code's 'Export to PDF' feature." -ForegroundColor Yellow
}
