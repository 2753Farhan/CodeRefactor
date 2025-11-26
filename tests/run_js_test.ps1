# Run JS test (requires Node.js)
$orig = node "../examples/js/sales_original.js"
$ref = node "../examples/js/sales_refactored.js"
Write-Host "Original output: $orig"
Write-Host "Refactored output: $ref"
if ($orig -eq $ref) {Write-Host "JS test: PASS"} else {Write-Host "JS test: FAIL"}
