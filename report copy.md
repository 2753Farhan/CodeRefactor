# Automated Refactoring Demonstration

This document demonstrates automated refactoring examples for the assignment. Each section shows the original code, the refactored result (manually prepared here) and a description of how an IDE (or GitHub Copilot) could be used to perform the automated refactor.

---

## Bash: Optimize find + wc

Original (examples/bash/count_lines_original.sh):

```bash
#!/bin/bash

# Original inefficient script: calls wc once for each file
# Find all .txt files and count lines in each
for file in $(find . -type f -name "*.txt"); do
    wc -l "$file"
done
```

Refactored (examples/bash/count_lines_refactored.sh):

```bash
#!/bin/bash

# Refactored: use -exec with + to pass multiple files to wc, reducing process invocations
find . -type f -name "*.txt" -exec wc -l {} +
```

Notes: Use the IDE/inline chat or suggest "optimize" on the loop in Copilot Chat to get this refactor. It reduces call overhead on many files.

---

## JavaScript: Move repeated calculations into a function

Original (examples/js/sales_original.js):

```javascript
// Original JS: repeated calculation performed inline
let totalSales = 0;

let applePrice = 3;
let applesSold = 100;
totalSales += applePrice * applesSold;

let orangePrice = 5;
let orangesSold = 50;
totalSales += orangePrice * orangesSold;

console.log(`Total: ${totalSales}`);
```

Refactored (examples/js/sales_refactored.js):

```javascript
// Refactored JS: move calculation into a function and use concise arrow notation
const calculateSales = (price, quantity) => price * quantity;

let totalSales = 0;

totalSales += calculateSales(3, 100); // apples
totalSales += calculateSales(5, 50); // oranges

console.log(`Total: ${totalSales}`);
```

Notes: Use inline chat and type "move repeated calculations into functions" to get the refactor suggestion.

---

## Python: Make functions concise and split responsibilities

Original (examples/python/areas_original.py) shows verbose function returns. Refactored (examples/python/areas_refactored.py) is more concise and uses `if __name__ == '__main__'`.

Original (examples/python/process_data_original.py) implemented a single function `process_data`. Refactored (examples/python/process_data_refactored.py) splits `cleanse_data` and `print_data`.

Use the inline chat "make this more concise" or "split into 2 separate functions" prompts to get these changes in your IDE.

---

## Java: Rewrite if/else chain with switch expression (Java 21)

Original (examples/java/AnimalSoundOriginal.java): uses if/else; Refactored (examples/java/AnimalSoundRefactored.java) uses a switch expression with null handling and pattern matching.

Use the IDE refactor features or inline chat to rewrite conditional blocks and add doc comments.

---

## How to run the demos and tests

- Bash (requires bash like Git Bash/WSL):

  - Run: `bash examples/bash/count_lines_refactored.sh` or run `tests/run_bash_test.ps1` from PowerShell (requires bash available)

- Node/JS (requires Node.js):

  - Run: `node examples/js/sales_refactored.js` or `tests/run_js_test.ps1`

- Python (requires Python and pytest installed):

  - Run: `python -m pytest -q tests/test_python_areas.py`

- Java (requires JDK 21+):
  - Compile: `javac examples/java/AnimalSoundRefactored.java`
  - Run: `java -cp examples/java AnimalSoundRefactored`

---

## Exporting this report to PDF

If Pandoc is installed:

```powershell
pandoc report.md -o report.pdf --pdf-engine=xelatex
```

Otherwise, open `report.md` in VS Code and export to PDF (Markdown: Open Preview -> Export to PDF) or print to PDF.

---

## Summary

This repository contains a simple set of manual refactorings and a report demonstrating each change. To meet the assignment requirement for automated refactorings, follow the steps above in your IDE (VS Code, Visual Studio, JetBrains, etc.), use the Copilot Chat or inline refactor features to apply the suggestions, then re-generate `report.pdf` with your notes/screenshots if required by your teacher.

---

## How to use Copilot/IDE automated refactoring for these examples

1. Open the file in your IDE and select the code you want to refactor.
2. Use inline chat (VS Code: Ctrl+i / Visual Studio: Alt+/) and ask for a specific refactor, for example:

- "optimize this script" (Bash optimization)
- "move repeated calculations into functions" (JS repeated calculation)
- "make this more concise" (Python simplification)
- "split into 2 separate functions" (Python splitting)
- "rewrite using switch expression and add docs" (Java conditional rewrite)

3. Review the suggested changes, click Accept or Preview to apply them.
4. Re-run the tests in the `tests` folder to ensure behavior remains the same.

Tip: To include visual proof for your teacher, take a screenshot of the IDE's refactor suggestion or the refactor preview that shows a before/after diff.
