Write-Host "Running all tests (Bash, JS, Python, Java)." -ForegroundColor Cyan

# Bash tests (runs in bash - Git Bash or WSL)
Write-Host "Bash test (requires bash):"
pwsh -NoProfile -Command "& { .\run_bash_test.ps1 }" -ErrorAction SilentlyContinue

# Node/JS
Write-Host "JS test (requires Node):"
powershell -NoProfile -Command "& { .\run_js_test.ps1 }"

# Python
Write-Host "Python test (requires Python and pytest):"
python -m pytest -q tests/test_python_areas.py || Write-Host "Python tests failed or pytest is not installed"

# Java
Write-Host "Java test (requires JDK 21+):"
& .\run_java_test.ps1

Write-Host "All tests executed." -ForegroundColor Green
