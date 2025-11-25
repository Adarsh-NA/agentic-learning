# MLOps Applied Exercises — Wh-Questions, MCQs, and Scenario-Based Tasks

This set of exercises helps learners apply concepts from the MLOps + ZenML + MLflow lecture. Use these to study, teach, or assess practical understanding. Work through WH (why/who/what/how/when/where/which) prompts, multiple-choice checks, and scenario-based applied tasks. Suggested time per scenario: 60–180 minutes depending on complexity.

---

# 1. WH-Questions (why / who / what / how / when / where / which)

- Why is MLOps described as a "set of practices" rather than a single tool?
- Why is focusing on business problem & ROI critical before choosing an ML model?
- Why does the instructor say ML code is ~20% of a production ML project?
- Why is caching useful in ZenML pipelines? When can caching be harmful?
- Who are the typical stakeholders in an ML product team and what are their core responsibilities?
- Who should decide the model deployment threshold (metric) and what inputs should they use?
- What is a ZenML "step"? What does it produce and consume?
- What is a ZenML "pipeline"? How is it different from a single script?
- What is MLflow used for in the pipeline illustrated in the lecture?
- What does “productionize the data pipeline” mean? Give three concrete activities.
- How does an inference pipeline differ from a training pipeline?
- How do you design a deployment trigger step (what inputs, what outputs)?
- When should you retrain a deployed model? List at least three triggers.
- When would you prefer a data-centric approach over a model-centric approach?
- Where are artifacts stored and why is an artifact store important?
- Where in the pipeline should legal/compliance checks be performed?
- Which metrics would you track for: (a) latency, (b) model performance, (c) fairness?
- Which ZenML stack components map to the following roles: orchestrator, artifact store, tracker, deployer?
- Which parts of an ML project are most likely to cause production failures (rank top 3 and explain)?
- How would you explain the “city vs building” analogy to a non-technical product manager?

---

# 2. Multiple-Choice Questions (MCQs)

Choose the best answer. Answers are shown after each question.

1. Which one best summarizes MLOps?
   - A. A specialized ML library for training models
   - B. A set of practices to deploy and maintain ML in production
   - C. A replacement for DevOps
   - D. An automated model-building tool  
   **Answer: B**

2. In a typical ML production lifecycle, which step most often consumes the most engineering time?
   - A. Hyperparameter tuning
   - B. Writing model inference code
   - C. Data pipelines, deployment, monitoring and integration
   - D. Feature selection in notebook  
   **Answer: C**

3. ZenML "steps" are primarily used to:
   - A. Run shell commands only
   - B. Represent independent units of a pipeline with typed inputs/outputs
   - C. Replace Python functions
   - D. Store data in a database  
   **Answer: B**

4. Why use MLflow autolog in a training step?
   - A. To make training faster
   - B. To automatically log parameters, metrics, and artifacts
   - C. To deploy models to production automatically
   - D. To optimize hyperparameters automatically  
   **Answer: B**

5. Step caching in ZenML will reuse a previous step output when:
   - A. Only when the step code changed
   - B. When inputs and step code/configuration are unchanged
   - C. Always, regardless of changes
   - D. Only when the pipeline is run locally  
   **Answer: B**

6. Which of the following is a correct reason to retrain a model?
   - A. The model's R² has increased
   - B. Production input distribution has drifted significantly
   - C. The pipeline cache is enabled
   - D. The dataset is perfectly balanced  
   **Answer: B**

7. Which ZenML stack component stores artifacts (datasets, model files)?
   - A. Orchestrator
   - B. Artifact store
   - C. Experiment tracker
   - D. Model deployer  
   **Answer: B**

8. Which of the following best describes a "deployment trigger"?
   - A. A command-line flag to run a pipeline
   - B. A boolean decision based on model metric thresholds
   - C. An environment variable that sets memory limits
   - D. A ZenML decorator  
   **Answer: B**

9. Which is the most direct negative consequence of high prediction latency?
   - A. Improved fairness
   - B. Increased user abandonment
   - C. More accurate predictions
   - D. Better experiment tracking  
   **Answer: B**

10. In the lecture’s project, the data was simplified by dropping text columns. The primary reason given was:
    - A. Text data is never useful
    - B. To focus the course on MLOps concepts rather than advanced feature engineering
    - C. Text processing is prohibited by ZenML
    - D. Text features degrade accuracy  
    **Answer: B**

11. Which tool was used for experiment tracking and local model serving in the course?
    - A. Kubeflow
    - B. MLflow
    - C. Airflow
    - D. Seldon  
    **Answer: B**

12. The Strategy Pattern was used in the data cleaning module to:
    - A. Automatically tune hyperparameters
    - B. Provide interchangeable preprocessing/splitting strategies
    - C. Encrypt data at rest
    - D. Validate model metrics  
    **Answer: B**

13. What does “materializer not found” usually imply in ZenML?
    - A. The pipeline is missing a documented step
    - B. The type of an artifact has no registered serializer/deserializer
    - C. The server is out of disk space
    - D. There is a syntax error in a step  
    **Answer: B**

14. If a deployed model begins supporting harmful behaviors (e.g., a toxic chatbot), the most immediate action is to:
    - A. Increase the model complexity
    - B. Retrain immediately with the same data
    - C. Take the model offline and investigate
    - D. Ignore and watch logs  
    **Answer: C**

15. Data-centric AI implies:
    - A. Always use a complex model architecture
    - B. Improving data quality and labels while keeping the model fixed
    - C. Never tuning model hyperparameters
    - D. Reducing dataset size to speed up training  
    **Answer: B**

16. Which metric is most appropriate to detect *data drift*?
    - A. Model loss on training set
    - B. Distribution distance (e.g., KL divergence) between production and training inputs
    - C. R² on training set
    - D. Latency  
    **Answer: B**

17. Which pipeline setting should you toggle if you want to force re-execution of all steps ignoring cache?
    - A. enable_cache=False
    - B. enable_cache=True
    - C. enable_recompute=True
    - D. cache_override=None  
    **Answer: A**

18. When integrating legal constraints in the pipeline, where is the best place to check data permissions?
    - A. In the training step only
    - B. During data ingestion/validation step and before deployment
    - C. After deployment
    - D. In the UI only  
    **Answer: B**

19. Using MLflow with ZenML requires:
    - A. Registering an MLflow experiment tracker in the stack
    - B. Replacing ZenML steps with MLflow steps
    - C. Running MLflow on a separate server only
    - D. Creating a docker image for model training  
    **Answer: A**

20. Which approach helps the most when models degrade because attackers change behavior (adversarial drift)?
    - A. Static model: deploy once and never retrain
    - B. Implement continuous monitoring + fast retraining loop + robust features
    - C. Remove monitoring — it will reduce false positives
    - D. Use larger batch sizes in training  
    **Answer: B**

---

# 3. Scenario-Based Exercises (applied, graded)

Each scenario includes tasks, deliverables, hints, and evaluation criteria.

---

## Scenario A — Design a Business-First ML Canvas (Time: 45–90 min)

Situation: You're asked to build an ML system to reduce overstock/understock at a retail company.

Tasks:
- Define the Value Proposition: write a 1-paragraph positioning statement: who, need, product, benefit.
- List 4 potential data sources (internal / external) and hidden costs associated with each.
- Select the ML prediction task (classification/regression/anomaly) and justify.
- Propose 3 evaluation metrics and explain how each maps to business cost.
Deliverables:
- 1-paragraph value prop
- 1-page ML canvas (bulleted list)
Hints:
- For overstock/understock, forecasting (regression) on sales quantities is typical.
Evaluation:
- Clarity of value prop (20%)
- Suitability of data sources & costs (30%)
- Correct task identification & justification (30%)
- Metric-business mapping (20%)

---

## Scenario B — Build a ZenML Pipeline Skeleton (Time: 90–180 min)

Situation: You will implement a skeleton ZenML pipeline for the retail forecasting project.

Tasks:
- Create 4 steps: `ingest_df`, `clean_df`, `train_model`, `evaluate_model`.
- Define typed inputs/outputs for each step (use `Annotated` where applicable).
- Implement `run_pipeline.py` that wires steps and runs pipeline with `enable_cache=True`.
Deliverables:
- Repository with `steps/` and `pipelines/` plus `run_pipeline.py`.
Hints:
- Use small sample CSV to test pipeline.
- Ensure steps return proper types (e.g., train returns model, clean returns train/test sets).
Evaluation:
- Steps present and typed (30%)
- Pipeline runs and shows steps in ZenML UI (40%)
- Correct wiring and caching behavior (30%)

---

## Scenario C — Implement a Deployment Trigger (Time: 60–120 min)

Situation: You want to ensure only sufficiently-good models are deployed.

Tasks:
- Implement a `deployment_trigger` step that takes a metric (R²) and a config (threshold) and returns boolean.
- Integrate into a deployment pipeline that conditionally calls `mlflow_model_deployer_step` when True.
- Run pipeline with a deliberately low threshold to see deployment; then high threshold to skip.
Deliverables:
- `deployment_pipeline.py`, `run_deployment.py`, and sample runs showing both paths.
Hints:
- Simulate R² values if needed; confirm logs show "Skipping deployment" when false.
Evaluation:
- Trigger correctness (40%)
- Conditional deploy path works (40%)
- Clear logs and reproducibility (20%)

---

## Scenario D — MLflow Autolog & Metrics Recording (Time: 45–90 min)

Situation: You must ensure all training runs are tracked.

Tasks:
- Modify training step to call `mlflow.sklearn.autolog()` or equivalent at step start.
- In evaluation step, log metrics explicitly: `mlflow.log_metric("r2", value)`, etc.
- Show how to extract MLflow tracking URI via ZenML client and start `mlflow ui` to visualize runs and metrics.
Deliverables:
- Training/eval step code and screenshot of MLflow UI showing metrics/artifact.
Hints:
- Register MLflow tracker in ZenML stack before running.
Evaluation:
- Autolog works and model artifact appears (50%)
- Logged metrics visible in UI (30%)
- Demonstrated ability to obtain tracking URI (20%)

---

## Scenario E — Caching Troubleshoot (Time: 60–120 min)

Situation: You re-run pipeline and expect cached steps, but an upstream step re-executes. Diagnose.

Tasks:
- List 5 reasons ZenML might not reuse a cached step (hint: code change, input change, env differences, materializer, step decorator difference).
- Reproduce one reason (e.g., change step signature, or modify an input file timestamp) and show logs proving cache invalidation.
Deliverables:
- Short report (max 1 page) listing reasons and evidence of reproduction.
Hints:
- Inspect ZenML logs; `using cached version of ...` appears when cache used.
Evaluation:
- Correct reasons (60%)
- Reproduction evidence & logs (40%)

---

## Scenario F — Latency vs Model Size Tradeoff (Time: 60–90 min)

Situation: Business requires response < 500 ms. You have a large model and a small model.

Tasks:
- Propose 3 engineering strategies to meet latency requirement while keeping accuracy acceptable.
- For each strategy, list pros/cons, complexity to implement, and monitoring changes required.
Deliverables:
- 1-page decision memo recommending a strategy and a fallback plan.
Hints:
- Consider model distillation, batching, asynchronous inference, caching frequent queries, or deploying smaller model for online and large for batch.
Evaluation:
- Practicality of proposals (50%)
- Consideration of operational cost & monitoring (30%)
- Clear fallback plan (20%)

---

## Scenario G — Detecting & Handling Data Drift (Time: 120–180 min)

Situation: The deployed model starts to misbehave. Design a drift detection & reaction pipeline.

Tasks:
- Choose a drift metric (e.g., population stability index, KL divergence) and justify.
- Design a ZenML monitoring step that computes drift daily and triggers alert when threshold exceeded.
- Define automated reactions: (a) send alert, (b) flag data for labeling, (c) trigger retrain pipeline automatically or schedule manual review.
Deliverables:
- Design doc + pseudocode of monitoring step + simple simulation (script computing drift between two datasets).
Hints:
- Use `evidently`, `scipy.stats`, or simple histogram distance.
Evaluation:
- Appropriateness of drift metric (40%)
- Feasibility of automation & reactions (40%)
- Simulation & reproducibility (20%)

---

## Scenario H — Fairness Gate Before Deployment (Time: 90–180 min)

Situation: You must prevent biased models from being deployed.

Tasks:
- Define a fairness metric for your target (e.g., demographic parity difference, equal opportunity).
- Implement a pre-deploy step that computes fairness metrics on validation set and blocks deployment if threshold violated.
- Design documentation required for auditing (what to store and where).
Deliverables:
- Code for fairness gate step + a short compliance checklist (data lineage, datasets used, thresholds, responsible person).
Hints:
- Use `aif360`, `fairlearn`, or compute simple group-wise metrics.
Evaluation:
- Correctness of fairness metric & gate logic (50%)
- Auditability & documentation (30%)
- Clear responsible-owner mapping (20%)

---

## Scenario I — Build a Minimal Streamlit App for Single Predictions (Time: 60–120 min)

Situation: Expose single-record predictions using the deployed MLflow service.

Tasks:
- Create `streamlit_app.py` with UI controls for features used by the model.
- On Predict button:
  - Call `prediction_service_loader` or directly call the MLflow serving endpoint to get a prediction.
- Display predicted value and basic explanation (e.g., top 3 features) if available.
Deliverables:
- Working Streamlit app and run instructions.
Hints:
- Ensure the deployed service is reachable (service.url) and CORS if necessary.
Evaluation:
- UI usability & correctness of calls (50%)
- Inclusion of simple explainability (20%)
- Robustness: error handling when service unavailable (30%)

---

## Scenario J — CI/CD for Pipeline Tests (Time: 120–240 min)

Situation: Create a minimal CI pipeline to test steps on PRs.

Tasks:
- Create GitHub Actions workflow that:
  - Sets up Python environment.
  - Installs deps.
  - Runs unit tests for `ingest_df` and `clean_df` with small sample data.
  - Runs a smoke test that triggers pipeline in local mode and ensures steps succeed (or mock artifact store).
Deliverables:
- `.github/workflows/ci.yml` and sample tests under `tests/`.
Hints:
- Keep jobs short by using tiny sample CSV and `zenml` local stack or mocking steps.
Evaluation:
- CI runs on push (40%)
- Tests cover step logic & smoke pipeline (40%)
- Ease of reproduction documented (20%)

---

# 4. Mini-Project Ideas (short; 2–6 hours each)

- Mini-Project 1: Implement a Data Drift Dashboard using a small dataset and a notebook that computes JS divergence for each numeric feature. Visualize changes over time.
- Mini-Project 2: Add a custom ZenML materializer for a custom object (e.g., a scikit-learn pipeline + preprocessor) and ensure proper serialization across steps.
- Mini-Project 3: Create a ZenML stack that uses a remote artifact store (S3 or GCS) and demonstrate a run saving artifacts remotely.
- Mini-Project 4: Implement a canary deployment simulation: deploy two model versions, route a percentage of test traffic, and compare metrics.

---

# 5. MCQ Answer Key (for instructors)

1 B, 2 C, 3 B, 4 B, 5 B, 6 B, 7 B, 8 B, 9 B, 10 B, 11 B, 12 B, 13 B, 14 C, 15 B, 16 B, 17 A, 18 B, 19 A, 20 B

---

# 6. Sample Solution Hints & Model Answers (short)

- Scenario A (ML Canvas):
  - Value prop example: "For retail inventory managers, our forecasting service predicts weekly SKU-level demand so managers reduce overstock and stockouts, improving revenue and reducing waste."
  - Prediction task: Regression (forecast units sold).
  - Metrics: RMSE (accuracy), Service-level fill rate % (business impact), Cost-savings estimate (monetary ROI).

- Scenario B (ZenML pipeline skeleton):
  - Use `@step` decorators returning `pd.DataFrame` and a training step returning `RegressorMixin`.
  - Use `@pipeline(enable_cache=True)` to combine.

- Scenario C (deployment trigger):
  - Implement `@step def deployment_trigger(r2: float, config: DeploymentTriggerConfig) -> bool: return r2 >= config.minimum_accuracy`.

- Scenario D (MLflow autolog):
  - In training step: `mlflow.sklearn.autolog()` then proceed to fit. Check MLflow UI for saved model in artifacts.

- Scenario E (caching issues):
  - Common reasons: step code changed, input file checksum changed, different environment variables, step decorator param changed, materializer change.

- Scenario F (latency tradeoffs):
  - Tradeoffs: model distillation (reduce size), serving optimization (GPU or CPU tuning), caching repeated predictions, asynchronous/batched inference. Monitor P50/P95 latencies.

- Scenario G (drift):
  - Metric: KL-divergence or PSI per feature with threshold. Reaction: alert -> collect labeled samples -> retrain pipeline with tests.

- Scenario H (fairness gate):
  - Compute group-wise recall/precision; compare differences. Store dataset hashes, model version in artifact store and document thresholds.

- Scenario I (Streamlit):
  - Convert inputs into JSON/numpy, call `service.predict()` or HTTP endpoint, handle exceptions.

- Scenario J (CI/CD):
  - Use GitHub Actions; use sample data for tests. Keep pipeline short to run on each PR.

---

# 7. Assessment Rubric (suggested, scalable)

For scenario tasks, use a 100-point rubric:
- Correctness (50%): Does the solution work and meet the scenario requirements?
- Reproducibility & Documentation (20%): Clear README, run instructions, environment setup.
- Robustness & Error Handling (15%): Handles missing inputs, step failures, service unavailability.
- Code Quality & Design (10%): Modularity, naming, patterns (Strategy, typed outputs).
- Observability & Logging (5%): Logs & metrics shown (ZenML UI, MLflow, or simple logs).

---

# 8. Quick Reference Commands (cheat sheet)

```bash
# Initialize ZenML project
zenml init

# Start ZenML server (dashboard)
zenml up

# Register MLflow integration
zenml integration install mlflow

# Show stacks
zenml stack list

# Run a pipeline Python entry
python run_pipeline.py

# Start MLflow UI using tracking URI (example)
mlflow ui --backend-store-uri <TRACKING_URI>

# Run Streamlit app
streamlit run streamlit_app.py
```

---

# 9. Tips for Grading / Teaching

- Encourage learners to submit:
  - code repo URL (with clear README)
  - ZenML pipeline run screenshots (dashboard)
  - MLflow UI metrics screenshot
  - short demo video if possible (2–5 min)
- Use the rubric above for consistent grading.
- For peer review: have students swap projects and run each other's pipelines to validate reproducibility.

---

# 10. Final Advice for Learners Applying These Exercises

- Start with the business problem — document it before coding.
- Implement pipelines incrementally; get ingestion → cleaning → train → eval working on tiny samples first.
- Register MLflow early and autolog; you’ll thank yourself when comparing runs.
- Use caching to speed iterating; intentionally exercise cache invalidation to learn its behavior.
- Treat deployments conservatively: create deployment triggers and fairness gates before automatic deployment.
- Practice debugging infra problems (version mismatches, materializer errors, service daemons); they are common and important skills for MLOps roles.

---

If you'd like, I can:
- Produce a printable worksheet for Scenario G (drift detection template).
- Generate ready-to-copy ZenML step + pipeline starter files for Scenario B.
- Create a GitHub Actions CI template tailored to the pipeline structure above.

Which would you like next?