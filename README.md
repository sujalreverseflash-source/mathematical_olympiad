## AI Mathematical Olympiad – Modular Pipeline

This project organizes an **AI Mathematical Olympiad** solution around a clear, modular pipeline:

- **Constructor**: generate multiple candidate solutions for each problem.
- **Critic**: rank and filter those candidates based on quality signals.
- **Symbolic verifier**: check mathematical validity (symbolic math, formal reasoning, code execution).
- **Self-consistency / majority vote**: aggregate surviving candidates into a final answer.

### Directory structure

- **`src/constructor/`**: prompt templates, sampling strategies, and generation logic for producing \(N\) candidate solutions per problem.
- **`src/critic/`**: scoring models, heuristics, rerankers, and filters to choose top candidates from the constructor.
- **`src/verifier/`**: symbolic math and code-checking tools (e.g. `sympy`-based verifiers, Python execution sandboxes).
- **`src/self_consistency/`**: majority vote / self-consistency aggregation logic and tie-breaking strategies.
- **`src/models/`**: model loading, API wrappers, and fine-tuning utilities.
- **`src/utils/`**: shared utilities (logging, configuration loading, common data structures).
- **`src/evaluation/`**: offline evaluation scripts and metrics; glue to Kaggle’s AIMO evaluation (can wrap `kaggle_evaluation/`).
- **`config/`**: YAML/JSON configs for prompts, model settings, and pipeline hyperparameters.
- **`data/raw/`**: original competition data (problems, references, etc.).
- **`data/processed/`**: tokenized/cleaned/formatted data ready for training and evaluation.
- **`data/interim/`**: intermediate artifacts (generated candidates, critic scores, verifier traces).
- **`scripts/`**: CLI entrypoints (e.g. `run_constructor.py`, `run_full_pipeline.py`, `train_critic.py`).
- **`notebooks/`**: exploratory analysis and prototyping.
- **`tests/`**: unit/integration tests for each pipeline module.

You can now implement each stage independently while keeping the overall AIMO pipeline clean and extendable.
