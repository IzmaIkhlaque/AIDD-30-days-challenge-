# Tasks: Menu-Driven Basic Calculator

**Input**: Design documents from `specs/001-menu-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: This plan includes test tasks as requested by the feature specification's focus on robust input handling and comprehensive testing.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create `src/calculator_cli.py` and basic `if __name__ == "__main__":` structure.
- [X] T002 Create `tests/unit/` and `tests/integration/` directories.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core input/output functions, and calculation logic that MUST be complete before ANY user story can be fully implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T003 [P] Implement `get_valid_number(prompt)` function in `src/calculator_cli.py` to get and validate numeric input, looping until valid.
- [X] T004 [P] Implement `get_valid_choice(min_val, max_val)` function in `src/calculator_cli.py` to get and validate menu choice, looping until valid.
- [X] T005 Implement `perform_calculation(op, num1, num2)` function in `src/calculator_cli.py` to execute arithmetic operations (addition, subtraction, multiplication, division).
- [X] T006 Implement function to display the main menu in `src/calculator_cli.py`.
- [X] T007 Implement function to display welcome banner in `src/calculator_cli.py`.
- [X] T008 Implement function to display goodbye message in `src/calculator_cli.py`.
- [X] T009 Implement generic `get_yes_no_input(prompt)` function in `src/calculator_cli.py` for 'continue' prompts.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform a single calculation (P1) 🎯 MVP

**Goal**: Enable a user to perform a single arithmetic calculation, from menu selection to result display.

**Independent Test**: Start the program, choose an operation, enter two valid numbers, and verify the correct calculation result is displayed before the "continue" prompt.

### Tests for User Story 1

- [X] T015 [US1] Write unit tests for `perform_calculation` in `tests/unit/test_calculator_logic.py`.
- [X] T016 [US1] Write integration test for single calculation flow (`select operation -> enter numbers -> show result`) in `tests/integration/test_single_calculation.py`.

### Implementation for User Story 1

- [X] T010 [US1] Integrate welcome banner display in `src/calculator_cli.py`.
- [X] T011 [US1] Integrate main menu display and get operation choice using `get_valid_choice` in `src/calculator_cli.py`.
- [X] T012 [US1] Get first number using `get_valid_number` in `src/calculator_cli.py`.
- [X] T013 [US1] Get second number using `get_valid_number` in `src/calculator_cli.py`.
- [X] T014 [US1] Call `perform_calculation` with user inputs and display result in `src/calculator_cli.py`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Continue with multiple calculations (P1)

**Goal**: Allow the user to perform multiple calculations sequentially or exit the program after any operation.

**Independent Test**: Perform a calculation, choose to continue, perform another calculation, then choose to exit.

### Tests for User Story 2

- [X] T019 [US2] Write integration test for continuous calculation and exit flow in `tests/integration/test_continuous_flow.py`.

### Implementation for User Story 2

- [X] T017 [US2] Implement the main program loop that continuously displays menu and performs calculations until exit is chosen in `src/calculator_cli.py`.
- [X] T018 [US2] Integrate 'Do you want to do another calculation? (y/n)' prompt using `get_yes_no_input` and decision logic in `src/calculator_cli.py`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Handle invalid input gracefully (P1)

**Goal**: Provide friendly error messages and robust re-prompting for all invalid user inputs.

**Independent Test**: Attempt various invalid inputs for menu choices, numbers (including division by zero), and continue/exit prompts, verifying friendly error messages and correct re-prompting.

### Implementation for User Story 3

- [X] T020 [US3] Refine `get_valid_number` with "Oops! That's not a valid number. Please try again 😊" message in `src/calculator_cli.py`.
- [X] T021 [US3] Refine `get_valid_choice` with "Please choose only 1, 2, 3, 4 or 5!" message in `src/calculator_cli.py`.
- [X] T022 [US3] Add division by zero check in `perform_calculation` or number input logic, with "Hey! I can't divide by zero, let's pick another second number 😉" message, re-prompting for second number in `src/calculator_cli.py`.
- [X] T023 [US3] Refine `get_yes_no_input` with appropriate error messages for invalid y/n input in `src/calculator_cli.py`.
- [X] T024 [US3] Update integration tests in `tests/integration/test_single_calculation.py` and `tests/integration/test_continuous_flow.py` to include invalid input scenarios.

**Checkpoint**: All user stories should now be independently functional

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Apply stylistic enhancements, final review of user experience, and documentation.

- [X] T025 Implement colorful welcome banner and goodbye messages (using ANSI escape codes or emojis) in `src/calculator_cli.py`.
- [X] T026 Ensure all output is formatted beautifully and consistently in `src/calculator_cli.py`.
- [X] T027 Review all user-facing messages for friendliness and clarity in `src/calculator_cli.py`.
- [X] T028 Add necessary Python docstrings and comments for all functions and modules in `src/calculator_cli.py`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Integrates with US1
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - Refines validation in all existing flows

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services (N/A for this project)
- Services before endpoints (N/A for this project)
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence