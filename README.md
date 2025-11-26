# Code Refactor Examples

This repository demonstrates several refactoring examples that you can use to practice automated refactoring in an IDE using GitHub Copilot or built-in IDE features.

Examples included:

- Bash: optimize find+wc loop to use -exec ... +
- JS: move repeated calculation to a function, rewrite to arrow and better parameter names
- Python: simplify functions (concise code), split functions into smaller units
- Java: rewrite if/else chain into a switch expression (Java 21 syntax)

How to use:

1. Open the project in your IDE (VS Code, Visual Studio, JetBrains, etc.).
2. Explore the `examples` folder. Each folder has `original` and `refactored` versions.
3. Use the IDE's automated refactor features or GitHub Copilot Chat/Inline to reproduce or create your changes.
4. Run the tests in the `tests` directory for verification.

Run tests (PowerShell):

```powershell
# Run all tests (requires appropriate runtimes installed and bash for the bash tests)
cd d:\Code_Refactor
pwsh .\tests\run_all.ps1
```

Convert the included `report.md` into a PDF to submit to your instructor. If Pandoc is installed, use:

```powershell
pwsh .\tools\convert_to_pdf.ps1 -input report.md -output submit/report.pdf
```

Alternatively, open `report.md` in VS Code and use the Markdown: Open Preview then export to PDF.
