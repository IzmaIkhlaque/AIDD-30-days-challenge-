# Data Model: Menu-Driven Basic Calculator

**Date**: 2025-12-02

## Summary

This basic CLI calculator does not require a formal data model or persistent storage. Operations are performed in-memory on user-provided numeric inputs.

## Entities

No complex entities are defined or managed by the application. The primary data elements are:

*   **User Input**: Numbers (integers or floats) for calculations, and single characters/integers for menu choices and continuation prompts.
*   **Results**: The computed output of arithmetic operations.

## Relationships

N/A. No relationships between entities as no formal entities are maintained.

## Validation Rules

Input validation is handled at the point of user interaction (refer to `spec.md` for details), ensuring numbers are valid and menu choices are within range.