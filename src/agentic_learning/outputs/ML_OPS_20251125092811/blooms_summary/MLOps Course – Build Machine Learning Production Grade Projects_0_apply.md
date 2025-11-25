# Applied Exercises for MLOps (ZenML + MLflow + End-to-End Concepts)

Below are targeted applied exercises — wh-questions, multiple-choice questions (MCQs), and scenario-based tasks — designed to help learners apply and practice the MLOps concepts discussed in the transcription. Use these for self-study, group activities, assessments, or interview prep.

---

## Table of contents

- Wh-Questions (Why / Who / What / How / When / Where / Which)
- Multiple-Choice Questions (MCQs) — with answer key & brief explanations
- Scenario-based Practical Tasks — project-style exercises with deliverables and hints
- Suggested rubrics and model answers / evaluation guidance

---

# 1 — Wh-Questions (apply conceptual understanding)

Use these as short-answer exercises. For classroom use: require 1–3 sentence answers, or 1-paragraph justification for design decisions.

### 1.1 High-level / conceptual
- Why is MLOps considered an extension of DevOps rather than just a new tool?
- Why are ML models only ~20% of the effort in production ML systems?
- Who (which team members) should be responsible for (a) creating features, (b) productionizing data pipelines, (c) setting up model deployment and monitoring?
- What does "deployment" mean in an MLOps context? Give two different concrete examples.
- How does the continuous "collect → train → deploy" loop operate in production, and what events typically trigger reentry into the loop?
- When should a team prioritize a data-centric approach over a model-centric approach? Give two concrete signals.
- Where in the pipeline would you place fairness and explainability checks: before, during, after deployment — and why?
- Which artifacts should be stored in an artifact store for reproducibility (list at least five)?
- What are the responsibilities of an experiment tracker like MLflow in a ZenML stack?
- How does step-level caching in ZenML speed up iterative development? When might caching be dangerous?
- Which production non-functional constraints should be considered before selecting a model architecture (list and briefly justify)?
- Why is a model registry useful for gating deployments?
- What is a materializer in ZenML and why might you need a custom one?
- Who should own the decision to roll back a deployed model after monitoring flags an issue — the ML engineer or a product/business stakeholder? Explain the tradeoffs.
- How do you measure the ROI of an ML forecasting model (retail example) — name the key components of the calculation?
- When is ML NOT the right solution for a business problem? Provide two criteria.
- Which stack components (artifact store, orchestrator, experiment tracker, model deployer) are required to run a ZenML pipeline locally? Which differ in a production setup?
- What is a deployment trigger and how would you implement one (conceptually)?
- How is latency related to model size and serving infrastructure? Give two ways to reduce inference latency while preserving reasonable accuracy.
- Where do you log per-inference metadata (for auditability): application logs, artifact store, MLflow, or all? Explain your reasoning.

---

# 2 — Multiple-Choice Questions (MCQs)

Each MCQ tests applied conceptual knowledge. Correct answer is shown after the choices with a brief explanation.

1. In a production ML system, which of the following best explains “pipeline caching” in ZenML?
   - A) It stores pipeline source code for versioning.
   - B) It reuses step outputs if inputs and code didn't change.
   - C) It caches model predictions for user sessions.
   - D) It caches Docker images for faster start-up.
   - **Answer: B.** Caching reuses previous step outputs when inputs & code are unchanged.

2. Which of the following is a *data-centric* approach?
   - A) Changing model architecture to increase accuracy.
   - B) Collecting more representative labels and fixing label errors.
   - C) Increasing number of training epochs.
   - D) Trying deeper neural network layers.
   - **Answer: B.** Data-centric focuses on improving data quality and labels.

3. What is the main role of MLflow when integrated into ZenML pipelines?
   - A) Orchestrating pipeline step order
   - B) Storing raw data files
   - C) Experiment tracking and model artifact logging
   - D) Enforcing Docker versioning
   - **Answer: C.** MLflow logs metrics, parameters, and models.

4. Which of the following should be the first thing to clarify when starting an MLOps project?
   - A) Choice of model architecture
   - B) The cloud provider for deployment
   - C) The business problem and cost of wrong predictions
   - D) The container runtime
   - **Answer: C.** Start with the business problem and cost of errors.

5. Why might the training code be quick, but deployment takes a week?
   - A) Training models is inherently slow, deployment is trivial.
   - B) Model code has more bugs than deployment code.
   - C) Infrastructure, integration, monitoring, and compliance take heavy effort.
   - D) Developers prefer spending time on deployment.
   - **Answer: C.** Deployment includes integration, infra, monitoring, and governance.

6. In a retail forecasting example, which step is LEAST suited to direct ML application?
   - A) Actual forecasting of demand
   - B) Data gathering (retrieving raw sales logs)
   - C) Market trend analysis via non-ML domain research
   - D) Feature engineering for forecasts
   - **Answer: B.** Data gathering is necessary but is not typically solved by ML itself; C and D can involve domain research and ML-assisted analysis. (B is the least ML-applied.)

7. What does a ZenML materializer do?
   - A) Compiles the pipeline into a binary
   - B) Serializes and deserializes step outputs to/from artifact storage
   - C) Encrypts artifact store data
   - D) Balances load across orchestrators
   - **Answer: B.**

8. Which of these is NOT a valid reason to retrain a deployed model?
   - A) New data distribution arrives (data drift)
   - B) Business objective changes
   - C) The model file grew in disk size
   - D) Model performance decays on production metrics
   - **Answer: C.** File size alone isn't a reason; A, B, D are.

9. Which metric would you prioritize to decide a deployment trigger for a regression forecasting model?
   - A) Accuracy
   - B) R² or business-aligned metric (e.g., forecasting MAPE)
   - C) F1 score
   - D) BLEU score
   - **Answer: B.** Use regression-appropriate and business-aligned metrics.

10. If a step returns `None` but the pipeline expects four outputs, you likely have:
    - A) Correct type annotations
    - B) A missing `return` in the step implementation
    - C) A caching issue only
    - D) A materializer bug only
    - **Answer: B.** Most often a missing return causes unpack error.

11. Which pattern was used in the course to make data cleaning extensible?
    - A) Singleton
    - B) Strategy
    - C) Observer
    - D) Adapter
    - **Answer: B.** Strategy pattern for multiple preprocessing behaviors.

12. For low-latency web predictions (≤ 100 ms), which approach is most appropriate?
    - A) Serve a 120B-parameter model on CPU without caching
    - B) Use a smaller distilled model, optimized runtime (ONNX), and batch where possible
    - C) Always use the most accurate model regardless of latency
    - D) Use client-side scripting to compute predictions
    - **Answer: B.** Distillation + optimized runtime reduces latency.

13. Where would you log per-prediction audit information for future debugging?
    - A) Not logged (privacy)
    - B) Application logs + secure centralized storage with redaction
    - C) Only in local files on the server
    - D) Only in the training dataset
    - **Answer: B.** Use application logs with security & privacy in mind.

14. Which tool from the course helps visualize pipeline runs and artifacts?
    - A) PyTorch
    - B) ZenML dashboard
    - C) pandas
    - D) scikit-learn
    - **Answer: B.** ZenML dashboard visualizes runs and artifacts.

15. Which is a valid defense against biased training data discovered post-deployment?
    - A) Ignore it if accuracy is still high
    - B) Retrain with sampled/augmented data and add fairness constraints, then re-evaluate
    - C) Delete the model and never use ML again
    - D) Increase model complexity to hide bias
    - **Answer: B.** Retrain with bias mitigation and reevaluate.

16. In the continuous deployment pipeline, the `deployment_trigger` should be implemented as:
    - A) A human-only approval step
    - B) A step checking metrics against thresholds (possibly combined with human approval)
    - C) Always `True` (always deploy)
    - D) Randomly decide to deploy
    - **Answer: B.** Use metric gating and optional human approval.

17. Which ZenML component is analogous to the "stack"?
    - A) A single `@step` function
    - B) A collection of infrastructure components (artifact store, orchestrator, tracker, deployer)
    - C) A scikit-learn pipeline object
    - D) A saved `.pkl` model
    - **Answer: B.**

18. Which of the following is a reason to prefer MLflow model format (or ONNX) over raw pickles?
    - A) Pickles are faster always
    - B) Standard formats improve portability, security, and cross-runtime serving
    - C) MLflow model format reduces disk usage only
    - D) ONNX is only for images
    - **Answer: B.**

19. If `zenml up` reports a version mismatch between client and server, recommended action is:
    - A) Ignore it — it never causes issues
    - B) Downgrade or upgrade to matching versions or re-init stack; fix warnings before continuing
    - C) Delete the repository
    - D) Remove ZenML
    - **Answer: B.** Resolve version mismatches proactively.

20. Which of these is the best place to handle human labeling and labeling cost estimation in the ML canvas?
    - A) Data Sources section
    - B) Offline evaluation only
    - C) Data collection and retraining planning
    - D) Model packaging
    - **Answer: C.** Labeling planning belongs in data collection & retraining planning.

---

# 3 — Scenario-Based Practical Tasks (project-style applied exercises)

Each scenario is realistic and asks for practical deliverables, design decisions, or code-level tasks. These are intended for hands-on application; some include suggested evaluation rubrics and hints.

---

### Scenario 1 — Pipeline blueprint and business case (Retail Forecasting)
Context: You work for a chain of grocery stores. The business problem: reduce overstock and understock for fresh produce. You have historical sales, promotions, calendar, and weather data.

Tasks:
- A1: Write a short value-proposition (1–2 sentences) that explains the benefit of the forecasting ML system and who the end user is.
- A2: Break the solution into pipeline components (list at least 6 steps including non-ML tasks).
- A3: Choose a business metric to evaluate success (e.g., net savings per week) and define how you will compute it (inputs and formula).
- A4: Decide whether to prioritize a model-centric or data-centric approach first. Justify with 2 reasons.

Deliverables:
- Value proposition sentence.
- Ordered list of pipeline steps (ingest, validation, enrichment, feature store, train, evaluate, etc.).
- Metric formula (e.g., savings = reduced overstock cost + avoided lost sales - cost of solution).
- Short rationale (3–4 sentences).

Hints:
- Quantify costs per unit for overstock (waste) and understock (lost margin).
- Include domain-specific data (e.g., perishable TTL, forecast horizon).

Rubric (10 pts):
- Value proposition clarity: 2 pts
- Pipeline completeness & ordering: 3 pts
- Metric & calculation plausibility: 3 pts
- Rationale: 2 pts

---

### Scenario 2 — Designing a ZenML stack for local dev vs production
Context: Your team wants a development environment on laptops and a production environment on Kubernetes. You will use ZenML and MLflow.

Tasks:
- B1: List the stack components for local dev (artifact store, orchestrator, tracker, deployer) and the concrete choices you would make (e.g., local filesystem, local orchestrator).
- B2: List production stack components and choices (e.g., GCS, Argo/Beam/K8s, MLflow server, Seldon).
- B3: Explain three configuration differences you must ensure (authentication, endpoints, resource limits).

Deliverables:
- Two small tables (dev vs prod) with component and selection.
- 3 configuration differences with rationale.

Hints:
- Think about credentials, artifact size, scaling, model serving SLA.

Rubric (8 pts):
- Correct components for both environments: 4 pts
- Clear configuration differences and rationale: 4 pts

---

### Scenario 3 — Implement a deployment trigger (code-level design)
Context: You will implement a `deployment_trigger` step that receives metrics `(r2: float, rmse: float)` and a `DeploymentTriggerConfig` with `min_r2: float` and `max_rmse: float`. The trigger should return `True` only if `r2 >= min_r2` AND `rmse <= max_rmse`. Also include a rule that prevents deployment if `r2` is unusually high but sample size is tiny (e.g., `n_test < 50`).

Tasks:
- C1: Write pseudocode (or Python code) for the step decorated with `@step` (ZenML style). Use types for inputs and outputs.
- C2: Explain why you included the sample size check.

Deliverables:
- Small code block with step function.
- Short justification (2–3 sentences).

Model answer (example code):
```python
from zenml import step
from zenml.steps import BaseParameters

class DeploymentTriggerConfig(BaseParameters):
    min_r2: float = 0.5
    max_rmse: float = 10.0
    min_test_samples: int = 50

@step
def deployment_trigger(r2: float, rmse: float, n_test: int, config: DeploymentTriggerConfig) -> bool:
    if n_test < config.min_test_samples:
        # avoid spurious high metrics on tiny sample
        return False
    return (r2 >= config.min_r2) and (rmse <= config.max_rmse)
```

Rubric (5 pts):
- Correct condition logic: 3 pts
- Sample size guard present & explanation: 2 pts

---

### Scenario 4 — Debugging a failing pipeline (practical troubleshooting)
Context: You run your ZenML training pipeline and get the error: `TypeError: cannot unpack non-iterable StepArtifact`. The `clean_df` step is supposed to return `(X_train, X_test, y_train, y_test)`.

Tasks:
- D1: List five concrete steps you would take to debug this issue (commands you would run or code changes to inspect).
- D2: Explain the most likely root cause and how to fix it.

Deliverables:
- Ordered debug checklist (5 items).
- Root cause & fix (brief).

Suggested debug steps:
1. Inspect `clean_df` step implementation: ensure it ends with `return X_train, X_test, y_train, y_test`.
2. Run `clean_df` independently (unit test) to see its return values.
3. Check step decorator signature to ensure return annotation matches number of outputs.
4. Look at ZenML dashboard for `clean_df` run to inspect artifact stored and its URI.
5. Ensure caching didn't return a previous artifact type; run pipeline with `enable_cache=False`.

Likely root cause:
- The step did not `return` the expected tuple (e.g., missing return or returned `None`), or the step returned a single StepArtifact because it returned an unsupported type. Fix by adding proper `return` and correct typed outputs.

Rubric (6 pts):
- Useful, ordered debug steps: 4 pts
- Root cause & fix correctness: 2 pts

---

### Scenario 5 — Materializer design (advanced)
Context: Your predictor step returns a `numpy.ndarray` predictions, but ZenML emits a warning: "Built-in materializer cannot handle numpy.ndarray; using default pickle materializer." You need a production-ready approach for storing per-run predictions in a standardized format.

Tasks:
- E1: Propose a production-safe serialization format and justify it.
- E2: Sketch a custom materializer (high-level pseudocode or explanation) to serialize numpy arrays and include metadata (model version, run_id, timestamp).

Deliverables:
- One-paragraph justification of chosen format (e.g., Parquet, Arrow, or MLflow model format).
- Materializer sketch describing `save` and `load` behaviors and metadata storage.

Hints:
- Consider interoperability, columnar storage, and schema evolution.

Rubric (8 pts):
- Rational choice of serialization: 4 pts
- Clear materializer behavior & metadata: 4 pts

Model answer summary:
- Use Arrow/Parquet for tabular predictions (fast, columnar, schema). Save metadata as JSON sidecar (run_id, model_version) and register artifact URI to ZenML. Provide `save` method to write `np.ndarray` as Parquet via `pandas.DataFrame` and `load` to read back.

---

### Scenario 6 — Deployment strategy & rollout plan
Context: Your model trainer achieves improved R² in staging. You must propose a rollout plan to production that minimizes risk. Requirements: allow rollback, monitor real-time metrics, and gradually ramp traffic.

Tasks:
- F1: Propose a 5-step rollout strategy (e.g., staging validation → canary → 10% traffic → 50% → 100%) and specify what metrics to monitor at each stage.
- F2: For the canary stage, specify two automated stop conditions that will trigger a rollback.

Deliverables:
- Ordered rollout steps with monitored metrics.
- Two stop conditions with thresholds.

Rubric (7 pts):
- Clear progressive rollout: 4 pts
- Reasonable stop conditions: 3 pts

Example solution:
- Steps: staging validation (unit tests & offline metrics) → deploy canary (1–5% traffic) → 10% if canary OK → 50% → 100%. Monitor latency p95, error rate, business KPI (conversion or revenue), and R² on sampled labeled traffic. Stop conditions: (1) p95 latency increases by >50% vs baseline for 10 mins; (2) business KPI drops by >3% or error rate >1%.

---

### Scenario 7 — Inference endpoint design & latency budget
Context: Target SLA: 95th percentile latency ≤ 150ms for online inference. You have two model options:
- Model A: 500MB, 92% accuracy, inference on CPU takes 400ms.
- Model B: 50MB, 88% accuracy, inference on CPU takes 50ms; can be optimized further on GPU/ONNX.

Tasks:
- G1: Select which model to serve for the production web app and justify (2–3 sentences).
- G2: If selecting Model B, list two optimization steps to reduce accuracy loss and maximize business value.

Deliverables:
- Choice and justification.
- Two optimization steps.

Rubric (5 pts):
- Sensible choice with business-awareness: 3 pts
- Useful optimizations: 2 pts

Model answer hints:
- Prefer Model B because it meets latency budget; combine with ensemble or calibrate probabilities, and improve data features (feature engineering) to regain accuracy.

---

### Scenario 8 — Monitoring plan for drift & performance
Context: You're required to design a monitoring plan that detects input data drift and performance degradation for an online model.

Tasks:
- H1: List at least five monitors/metrics you would implement and their purpose.
- H2: For each monitor, specify a simple threshold or alarm rule.

Deliverables:
- Table of monitors + purpose + threshold.

Example monitors:
- Input feature distribution PSI > 0.2 → alert.
- Mean prediction value change > 3σ of historical mean → alert.
- Model latency p95 > 2x baseline → alert.
- Error rate or 5xx > 0.5% → alert.
- Business KPI drop (e.g., conversions) > 5% in rolling 1 day → alert.

Rubric (6 pts):
- Good coverage & plausible thresholds: 6 pts

---

### Scenario 9 — Explainability audit
Context: A deployed model flagged for possible bias. You must run a post-deployment explainability audit on a recent batch of predictions.

Tasks:
- I1: Describe a 4-step audit procedure that includes data selection, explainability method(s), metrics, and remediation options.
- I2: Name two explainability tools or techniques you would use and why.

Deliverables:
- 4-step procedure and choice of tools (e.g., SHAP, LIME).

Rubric (6 pts):
- Audit completeness & practical remediation suggestions: 4 pts
- Tool choices & justification: 2 pts

Example steps:
1. Select representative recent batch (stratify by sensitive attributes).
2. Compute SHAP summary and per-group feature importance.
3. Compute fairness metrics (e.g., disparate impact ratio, equalized odds).
4. Recommend remediation: reweighting, additional training data for underrepresented groups, or human-in-loop for flagged cases.

---

### Scenario 10 — From CSV to SQL (realistic data ingestion)
Context: The course uses CSVs. You need to upgrade ingestion to use PostgreSQL. Design and implement the change.

Tasks:
- J1: Outline the changes to the `ingest_df` step to read from Postgres instead of `pd.read_csv`.
- J2: Provide a small code example of a ZenML `@step` that connects, executes a parameterized SQL query, and returns a `pd.DataFrame`.
- J3: List three advantages of ingestion from a DB vs CSV, and one potential complication.

Deliverables:
- Short outline and code snippet.
- Advantages & complication.

Model snippet:
```python
from zenml import step
import pandas as pd
import sqlalchemy

@step
def ingest_from_postgres(conn_string: str, query: str) -> pd.DataFrame:
    engine = sqlalchemy.create_engine(conn_string)
    with engine.connect() as conn:
        df = pd.read_sql_query(query, conn)
    return df
```

Advantages: incremental/partial reads, access control, easier updates/joins. Complication: credentials & network security + connection pooling.

Rubric (6 pts):
- Correct step changes, working snippet, realistic pros/cons.

---

# 4 — Suggested Answer Key & Rubrics (short)

- MCQs: correct answers as listed inline.
- Scenarios: use rubric provided to grade. Provide expected model answers as hints in each scenario.

---

# 5 — Additional quick practice items (short tasks)

- Convert the high-level movie production analogy into a ZenML pipeline diagram: list steps, input/output types, which steps should be cached.
- Given a dataset with categorical columns, sketch a `DataPreprocessStrategy` that includes categorical encoding and textual tokenization for `review_comment_message`.
- Create a simple test plan: 5 unit tests & 3 integration tests to validate `clean_df` and `train_model` steps.
- Write a short README section explaining how to run your pipeline locally and how to view MLflow metrics.

---

# 6 — Useful answer examples / reference patterns

- Example `deployment_trigger` step: see Scenario 3 model answer.
- Example prediction materializer idea: store predictions as Parquet and JSON sidecar metadata.
- Example rollout plan: staging → canary (1–5%) → ramp 10% → 50% → 100% with p95 latency and business KPI checks.

---

# 7 — How instructors / teams can use these exercises

- Bootcamp: Use scenarios 1–4 as day-1 assignments and scenarios 5–10 as subsequent projects.
- Interview prep: MCQs + debugging scenario simulate common live-coding / system design questions.
- Team retrospective: Use monitoring & audit scenarios to test production readiness.
- Grading: Use rubrics per scenario; allow partial credit for reasonable tradeoffs and justifications.

---

# 8 — References & further practice suggestions

- Re-implement the course example but replace:
  - CSV ingestion with PostgreSQL (Scenario 10).
  - Linear Regression model with RandomForest or LightGBM (measure compute/time tradeoffs).
  - Use MLflow model registry and implement a model promotion policy.
- Add a feature store (Feast) and modify `clean_df` to fetch features from the store.
- Implement a small Streamlit app (as in the course) but add an explainability panel using SHAP.

---

If you want, I can:
- Produce printable assessment sheets for instructors (with point allocation and sample model answers).
- Generate a set of automated tests (pytest) for pipeline step contracts.
- Provide small starter code templates for each scenario (ZenML step scaffolds).

Which would you like next?