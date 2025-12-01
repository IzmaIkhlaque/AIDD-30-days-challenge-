<!--
Sync Impact Report:
Version change: None -> 1.0.0
Modified principles:
  - PROJECT_NAME: None -> Basic Calculator
  - PRINCIPLE_1_NAME: None -> Beginner-Friendly UX
  - PRINCIPLE_1_DESCRIPTION: None -> The application prioritizes a warm, clear, and forgiving user experience. This includes a welcoming message, a numbered menu for options, guided inputs, and very kind, helpful error messages in plain English, avoiding technical jargon.
  - PRINCIPLE_2_NAME: None -> CLI-First Design
  - PRINCIPLE_2_DESCRIPTION: None -> The calculator is exclusively a Command Line Interface (CLI) application. All interactions must occur via standard input/output. Design decisions should leverage the strengths of a CLI while mitigating its limitations for a beginner audience.
  - PRINCIPLE_3_NAME: None -> Modularity & Readability
  - PRINCIPLE_3_DESCRIPTION: None -> Code must be structured in a modular fashion, with clear separation of concerns (e.g., input handling, calculation logic, output formatting). Readability for beginners is paramount, using clear variable names, concise functions, and appropriate comments.
  - PRINCIPLE_4_NAME: None -> Robust Input Handling
  - PRINCIPLE_4_DESCRIPTION: None -> All user inputs must be validated to prevent errors and ensure smooth operation. The system should gracefully handle invalid inputs (e.g., non-numeric entry where numbers are expected) with clear, actionable feedback to the user, guiding them toward correct input without frustration.
  - PRINCIPLE_5_NAME: None -> Comprehensive Testing
  - PRINCIPLE_5_DESCRIPTION: None -> All core calculator functions and input handling logic must be covered by automated tests. This ensures correctness and reliability, and provides a safety net for future modifications. Tests should be clear and easy to understand for beginners examining the codebase.
Added sections:
  - Technical Constraints
  - Quality & Development Guidelines
Removed sections:
  - PRINCIPLE_6_NAME and its description
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .gemini/commands/sp.adr.toml: ✅ updated
  - .gemini/commands/sp.analyze.toml: ✅ updated
  - .gemini/commands/sp.checklist.toml: ✅ updated
  - .gemini/commands/sp.clarify.toml: ✅ updated
  - .gemini/commands/sp.constitution.toml: ✅ updated
  - .gemini/commands/sp.git.commit_pr.toml: ✅ updated
  - .gemini/commands/sp.implement.toml: ✅ updated
  - .gemini/commands/sp.phr.toml: ✅ updated
  - .gemini/commands/sp.plan.toml: ✅ updated
  - .gemini/commands/sp.specify.toml: ✅ updated
  - .gemini/commands/sp.tasks.toml: ✅ updated
  - GEMINI.md: ✅ updated
Follow-up TODOs: None
-->
# Basic Calculator Constitution

## Core Principles

### Beginner-Friendly UX
The application prioritizes a warm, clear, and forgiving user experience. This includes a welcoming message, a numbered menu for options, guided inputs, and very kind, helpful error messages in plain English, avoiding technical jargon.

### CLI-First Design
The calculator is exclusively a Command Line Interface (CLI) application. All interactions must occur via standard input/output. Design decisions should leverage the strengths of a CLI while mitigating its limitations for a beginner audience.

### Modularity & Readability
Code must be structured in a modular fashion, with clear separation of concerns (e.g., input handling, calculation logic, output formatting). Readability for beginners is paramount, using clear variable names, concise functions, and appropriate comments.

### Robust Input Handling
All user inputs must be validated to prevent errors and ensure smooth operation. The system should gracefully handle invalid inputs (e.g., non-numeric entry where numbers are expected) with clear, actionable feedback to the user, guiding them toward correct input without frustration.

### Comprehensive Testing
All core calculator functions and input handling logic must be covered by automated tests. This ensures correctness and reliability, and provides a safety net for future modifications. Tests should be clear and easy to understand for beginners examining the codebase.

## Technical Constraints

The application must be developed in Python. No external libraries beyond the Python standard library are permitted unless explicitly approved. The application must run on common operating systems (Windows, macOS, Linux) without platform-specific dependencies.

## Quality & Development Guidelines

Code must adhere to PEP 8 style guidelines. Functions should be well-documented using Python docstrings. All user-facing text (prompts, messages, errors) must be in clear, conversational English.

## Governance

This constitution serves as the foundational document for the Basic Calculator project. Any proposed amendments must be thoroughly discussed, documented, and approved by project maintainers. Versioning follows semantic principles for governance changes. All code reviews will verify adherence to these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-02 | **Last Amended**: 2025-12-02