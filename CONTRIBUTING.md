# 🤝 Contributing to CorStream

First off, thank you for taking the time to contribute! 🎉  
CorStream is a coroutine composition framework that thrives on clean code, thoughtful design, and strong testing. These guidelines help us maintain a healthy and consistent codebase as it grows.

---

## 📦 Project Structure Overview

```
corstream/
├── core.py                 # Stream class
├── ops/                    # All transformation operators
├── sinks/                  # Terminal consumers
├── tests/                  # One test file per operator/sink
└── examples/               # Usage demos and reference pipelines
```

---

## 🧰 Prerequisites

1. Python 3.9 or later
2. [Poetry](https://python-poetry.org/docs/#installation)
3. Clone the repository:
   ```bash
   git clone https://github.com/shivkun/corstream.git
   cd corstream
   poetry install
   ```

---

## 🧪 Running the Test Suite

All code must be fully tested before merging. To run tests:

```bash
poetry run pytest
```

Use `pytest-asyncio` to test async behavior. One test file per operator/sink. Keep tests fast and isolated.

To run formatting, type checking, and linting:

```bash
poetry run black corstream/
poetry run mypy corstream/
poetry run ruff check corstream/
```

---

## ✍️ Contributing Code

### ✅ DO:
- Match the style of the existing codebase.
- Write docstrings for all public methods and functions.
- Use descriptive variable and function names.
- Add tests for all new functionality.
- Include type annotations.
- Group related logic into logical modules (e.g., `ops/transform/`, `ops/control/`, etc.)

### 🚫 DO NOT:
- Introduce untyped or untested code.
- Include unrelated changes in your PR.
- Break backward compatibility unless clearly versioned.
- Add dependencies without discussion in a GitHub Issue.

---

## ✏️ Adding a New Operator or Sink

1. Add a new file to the appropriate subdirectory of `corstream/ops/` or `corstream/sinks/`.
2. Re-export it in the nearest `__init__.py` and the root `__init__.py`.
3. Add tests in `tests/`.
4. Document usage in a comment or in `examples/`.

---

## 📄 Commit Style

Follow this format:

```
feat: add map_async operator
fix: correct batch edge case with trailing items
refactor: clean up internal apply() logic
test: add tests for throttle operator
```

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

---

## 📥 Submitting a Pull Request

1. Fork the repo and create your branch:  
   `git checkout -b feat/your-feature`
2. Commit your changes with proper messages.
3. Push to your fork:  
   `git push origin feat/your-feature`
4. Open a PR describing:
   - What you added/changed
   - Why it’s needed
   - Any limitations or follow-ups

---

## 🙋 Need Help?

- Open a [GitHub Issue](https://github.com/shivkun/corstream/issues)
- Tag your PR with `WIP` if it's not ready yet
- PRs without tests or with failing lint will not be merged

---

Thank you for helping make **CorStream** better! 🧵✨
