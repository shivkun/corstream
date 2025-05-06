# ✅ CorStream TODO

A living list of upcoming features, improvements, and refinements to track the evolution of the CorStream framework.

---

## 🚧 PHASE 3 — Operator Wrapping, Error Contexts, DX

### 🧠 Design & Architecture
- [ ] Add a wrapping layer to all operators (for `.catch()` and `.retry()` to function properly)
- [ ] Implement operator context stack (for better tracebacks and error origin tracking)
- [ ] Add optional debug ID or name to each Stream stage (e.g., `.map(..., name="double")`)

### 🧪 Testing & Validation
- [ ] Add unit tests for `.catch()` (once operator wrapping is in place)
- [ ] Add unit tests for `.retry()` (with simulated transient errors)
- [ ] Introduce randomized stress test pipelines (fuzz testing operator combinations)

---

## 🔬 PHASE 4 — Observability & Introspection

- [ ] `.visualize()` — generate a DAG or graph of the pipeline (DOT, Mermaid, etc.)
- [ ] `.tee()` — inject side-effects (e.g., logging, metrics) without altering flow
- [ ] `.metrics()` — track throughput, item counts, time per operator
- [ ] Pipeline timing profiler (report exec time per stage)

---

## 🧩 PHASE 5 — Dynamic & Reactive Extensions

- [ ] `.watch()` — re-evaluate stream source on filesystem or socket changes
- [ ] `.split()` — broadcast stream into multiple independent branches
- [ ] `.merge()` — combine multiple streams into one
- [ ] `.debounce()` and `.buffer()` operators
- [ ] Optional push-based stream support

---

## 🧹 Maintenance & Refactoring

- [ ] Consolidate error types into a structured exception hierarchy
- [ ] Improve typing across all operators with bounded generics
- [ ] Replace `# type: ignore` with proper type declarations where possible
- [ ] Add property-based testing for core operators

---

## 📄 Documentation

- [ ] Add usage examples for each operator in the README
- [ ] Add `docs/` folder for API reference using Markdown or Sphinx
- [ ] Include animated diagrams of pipelines (e.g. in `.visualize()` docs)
- [ ] Document performance best practices

---

## 🧪 CI/CD (Final Phase)

- [ ] Add GitHub Actions for:
  - Formatting checks (`black`, `ruff`)
  - Type checking (`mypy`)
  - Tests (`pytest`)
- [ ] Upload coverage reports to Codecov
- [ ] Enforce passing CI before merge

---

## 🧃 Nice-to-Have

- [ ] Realtime pipeline visual debugger (via WebSocket or CLI)
- [ ] Interactive stream builder (REPL GUI or terminal DSL)
- [ ] Built-in CLI runner: `corstream run ./my_pipeline.py`
- [ ] Typed DSL mode (`stream | filter | map | for_each`) with operator overloading

---

Feel free to contribute! See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.
