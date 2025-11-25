# MLflow & DagsHub — Applied Exercises (Wh-questions, MCQs, Scenarios)

Below are applied exercises to practice core concepts from the transcription: experiment tracking with MLflow, model registry/versioning, artifact management, deploying via aliases, and using DagsHub as a centralized MLflow server. Use them to test, practice, teach, or assess applied understanding.

---

## **How to use this file**
- Work through Wh-questions first to self-check conceptual recall.
- Attempt MCQs under timed quiz conditions; check answers in the answer key.
- Complete scenario-based tasks by implementing code and documenting results (deliverables listed per scenario).
- Use the scenarios as candidate test assignments or lab exercises.

---

# 1 — Wh-Questions (why / who / what / how / when / where / which)

Use these for reflection, discussion, or oral quizzes.

Why
- Why is MLflow useful in a team that uses many Jupyter notebooks?
- Why might the team prefer registering a model to the Model Registry instead of keeping artifacts locally?
- Why is recall for the minority class often prioritized in anomaly/fraud detection tasks?
- Why should you include environment files (e.g., `requirements.txt` or `conda.yaml`) as artifacts when logging a model?

Who
- Who on a data science team should be responsible for assigning model aliases like `Champion` or `Challenger`?
- Who should own the MLflow tracking server credentials and manage access when using a centralized server like DagsHub?
- Who benefits from logging `git` commit SHA and dataset version in each run?

What
- What is an MLflow Run ID and how is it used when registering a model?
- What are the three main things you typically log to MLflow in a training run?
- What does `mlflow.register_model(model_uri, name)` expect as `model_uri`?
- What artifacts does MLflow typically create when logging a scikit-learn model?

How
- How do you switch from a local MLflow server (`localhost:5000`) to a DagsHub-hosted MLflow URI in a notebook?
- How do you load a model from the Model Registry by alias rather than by explicit version?
- How can you log parameters and metrics for multiple experiments run inside a `for` loop?

When
- When should you register a model in the Model Registry: during the training run or after comparing several runs? Explain trade-offs.
- When is it appropriate to use SMOTE/SMOTETomek for a dataset?

Where
- Where do artifacts get stored when you run `mlflow ui` locally by default? (Hint: small demo vs production)
- Where should you store large datasets and link them to runs for reproducibility?

Which
- Which MLflow URI format would you use to reference a model artifact inside a specific run?
- Which alias (`Champion` or `Challenger`) should production inference code use to load the model in order to avoid changing version numbers?

---

# 2 — Multiple Choice Questions (MCQs)

Choose the single best answer. Answers provided in the Answer Key section.

1. After running `mlflow ui` locally, which URL is the MLflow UI typically available at by default?
   - A) `http://localhost:8080`
   - B) `http://127.0.0.1:5000`
   - C) `https://mlflow.local`
   - D) `http://0.0.0.0:6000`

2. Which function logs a scikit-learn model so MLflow stores model artifact and environment metadata?
   - A) `mlflow.log_artifact()`
   - B) `mlflow.log_model()`
   - C) `mlflow.sklearn.log_model()`
   - D) `mlflow.register_model()`

3. To register a model from a run with run ID `abc123` where the artifact path is `model`, what is a correct `model_uri`?
   - A) `models:/abc123/model`
   - B) `runs:/abc123/model`
   - C) `run:/abc123/model`
   - D) `models:abc123/model`

4. Which MLflow URI lets you load the model assigned the alias `Challenger` for model name `anomaly_xgb`?
   - A) `models:/anomaly_xgb/Challenger`
   - B) `models:/anomaly_xgb@Challenger`
   - C) `runs:/anomaly_xgb@Challenger`
   - D) `runs:/Challenger/anomaly_xgb`

5. Which environment variables are commonly used to authenticate MLflow to a DagsHub tracking server?
   - A) `MLFLOW_TRACKING_URI`, `MLFLOW_TRACKING_USERNAME`, `MLFLOW_TRACKING_PASSWORD`
   - B) `DAGSHUB_URI`, `DAGSHUB_USER`, `DAGSHUB_TOKEN`
   - C) `MLFLOW_URI`, `MLFLOW_USER`, `MLFLOW_KEY`
   - D) `TRACKING_URI`, `TRACKING_USER`, `TRACKING_TOKEN`

6. When comparing models for an anomaly detection task where missing positives is very expensive, which metric is typically prioritized?
   - A) Precision for class 0
   - B) Recall for class 1
   - C) Accuracy
   - D) Log-loss

7. Which statement about registering models inside `mlflow.log_model()` vs post-hoc registration is TRUE?
   - A) Logging with `log_model` can never register a model automatically.
   - B) Registering during run avoids needing to choose later but may clutter registry with suboptimal models.
   - C) Post-hoc registration is impossible; only `log_model` registers models.
   - D) Registration is only done via the UI, not via code.

8. Which of the following is NOT normally produced as an artifact when MLflow records a model?
   - A) `model.pkl` or framework model file
   - B) `requirements.txt`
   - C) `conda.yaml`
   - D) `git_commit.patch` (automatic)

9. If you want multiple teammates to upload runs to one central MLflow server, the best first step is:
   - A) Each person runs `mlflow ui` on their laptop and shares screenshots.
   - B) Set up a central MLflow tracking server (e.g., DagsHub or hosted endpoint) and share credentials.
   - C) Use Excel to collect metrics and have someone upload models on request.
   - D) Use `mlflow.log_artifact` to send artifacts by email.

10. To promote a dev model named `xgb_sm` with alias `Challenger` into a production registry named `anomaly_prod` programmatically, which API/approach is appropriate?
    - A) Use `MlflowClient` to copy the model/version into `anomaly_prod`
    - B) Manually re-train the model and push it to the `anomaly_prod` repo
    - C) Use `mlflow.sklearn.log_model` to write to a new name
    - D) Edit the model file name and re-upload the artifact

---

# 3 — Scenario-based Exercises (practical tasks, deliverables, grading hints)

Work through each scenario. For coding tasks, implement in a notebook and commit to a Git repo. Deliverables: short report (one page) + code cell outputs demonstrating each result unless otherwise specified.

Scenario 1 — Basic local tracking
- Task:
  - Create a synthetic binary classification dataset with class imbalance (900 class 0, 100 class 1).
  - Train logistic regression with two hyperparameter settings (C=1 and C=0.1).
  - Log runs to a local MLflow server (`mlflow ui`).
  - Log: dataset version tag, hyperparameters, classification metrics (accuracy, recall per class, f1_macro), and the trained model artifact.
- Deliverable:
  - Jupyter notebook with MLflow logging code and a screenshot of the MLflow UI showing two runs.
  - One-paragraph conclusion: which run would you pick for production if recall_class_1 is primary?

Scenario 2 — Looping experiments and comparison
- Task:
  - Train 4 models across different algorithms: LogisticRegression, RandomForest, XGBClassifier, XGB + SMOTETomek.
  - Use a `for` loop and `enumerate` to run and log each experiment to MLflow. Set `run_name` to a descriptive name.
  - Use `mlflow.log_params` to log the hyperparameters dictionary for each model.
- Deliverable:
  - Notebook with looped experiments.
  - Use the MLflow UI Compare feature to select the best model when recall_class_1 is the primary metric. Attach a screenshot of the compare view and explain selection.

Scenario 3 — Registering and loading a model
- Task:
  - From the experiments in Scenario 2, pick the run with highest recall_class_1, register it to the Model Registry with name `anomaly_candidate`.
  - Add description and a tag `dataset_version: V1`.
  - Load the model locally from the Registry using both (a) explicit version number and (b) alias `Challenger` (assign the alias).
  - Run a small batch of predictions to verify identical outputs.
- Deliverable:
  - Notebook cells showing `mlflow.register_model(...)`, `mlflow.xgboost.load_model(...)` (or framework appropriate), prediction outputs, and a short verification statement proving equality of predictions.

Scenario 4 — Alias promotion (Dev → Prod)
- Task:
  - Using `MlflowClient`, copy or promote the `anomaly_candidate@Challenger` model into another registry name `anomaly_prod`. Set that new prod version alias to `Champion`.
  - Demonstrate loading the production model via `models:/anomaly_prod@Champion` and run predictions.
- Deliverable:
  - Notebook code showing `MlflowClient` operations and the successful load/prediction. Describe the promotion steps in 3 bullet points.

Scenario 5 — Debugging a run ID / registration error
- Task:
  - Intentionally attempt to register a model using an invalid run URI (e.g., wrong run ID) and capture the error.
  - Then explain how you would find the correct Run ID from the UI and re-run registration successfully.
- Deliverable:
  - Notebook cell with failed registration (error message), then corrected registration. Short explanation listing steps to recover from the error.

Scenario 6 — DagsHub centralized tracking
- Task:
  - Create a GitHub repo, push a notebook (or use provided one), create a free DagsHub account, and connect the repo to DagsHub.
  - Install `dagshub` Python package and initialize tracking in the notebook with `dagshub.init(..., mlflow=True)` or set environment variables `MLFLOW_TRACKING_URI`, `MLFLOW_TRACKING_USERNAME`, `MLFLOW_TRACKING_PASSWORD` (token).
  - Log a single run from your notebook to DagsHub’s MLflow and verify the run appears on the DagsHub MLflow UI.
- Deliverable:
  - Short write-up of the steps and a screenshot of the run on DagsHub MLflow UI. Note: if you cannot create a DagsHub account, explain alternative hosted endpoints you would use.

Scenario 7 — Business stakeholder selection & communication
- Task:
  - You are the data scientist. The team lead prioritizes recall_class_1, but business stakeholders are worried about too many false positives. Using the runs from Scenario 2:
    - Prepare a 1-page summary to present to a non-technical stakeholder:
      - Show top 3 models, recall_class_1, precision_class_1, F1_macro.
      - Show a recommendation and clearly state expected business trade-offs (e.g., more alerts vs more caught frauds).
- Deliverable:
  - PDF or Markdown one-page summary. Include a recommended model and one-sentence rollback plan.

Scenario 8 — CI/CD promotion sketch
- Task:
  - Draft a short CI/CD pipeline (Jenkinsfile or GitHub Actions steps, pseudo-code acceptable) that:
    - Trains/validates models upon push
    - Evaluates primary metric threshold (e.g., recall_class_1 >= 0.80)
    - On pass: registers the run, assigns alias `Challenger`, runs automated tests, then promotes to `Champion` if staging tests pass.
- Deliverable:
  - Text or code snippet of the pipeline and explanation of checks at each stage.

Scenario 9 — Dataset version tie-in and reproducibility
- Task:
  - Demonstrate how to log dataset version into MLflow run params (e.g., `dataset_version: V2` or a dataset hash).
  - Describe a method to store the dataset (e.g., cloud storage path or DagsHub dataset) and ensure runs reference the same dataset.
- Deliverable:
  - Notebook snippet logging `mlflow.log_param("dataset_version", "V2")` and a short checklist describing how to reproduce a run end-to-end (code commit, dataset location, environment file).

Scenario 10 — Evaluate cost of oversampling
- Task:
  - Compare model inference speed and memory consumption for XGBoost trained on original data vs XGBoost trained on SMOTETomek-augmented data. Measure training and inference times for a fixed test batch.
  - Discuss trade-offs between improved recall and increased inference cost, and provide a recommendation.
- Deliverable:
  - Short table with timings and memory, plus one-paragraph recommendation.

---

# 4 — Mini Project Assignments (graded rubrics)

A. Mini-project: "From Notebook to Prod Model"
- Tasks (full pipeline):
  1. Build dataset + 3 candidate models.
  2. Log all runs and artifacts to central MLflow (DagsHub or local if solo).
  3. Use MLflow UI to pick the best model (primary metric defined).
  4. Register chosen model to Model Registry with description + tags.
  5. Promote to production alias via `MlflowClient`.
  6. Package model into a Docker image using the recorded `requirements.txt`.
- Deliverables:
  - Git repo link with notebook(s), Dockerfile, and a one-page README documenting steps and commands to reproduce.
- Grading rubric (suggested):
  - 20% — Correct logging of params/metrics/artifacts
  - 20% — Clear run naming & dataset versioning
  - 20% — Model registry usage and versioning
  - 20% — Demonstrated production load from alias and Docker packaging
  - 20% — Documentation quality & reproducibility

B. Mini-assignment: "Compare & Justify"
- Tasks:
  - Given runs for models A/B/C in MLflow, write a 500-word justification for choosing one model for production, including business impact, metrics trade-offs, and monitoring plan.
- Grading:
  - 50% technical justification, 30% business-communication clarity, 20% monitoring & rollback plan.

---

# 5 — MCQ Answer Key

1. B  
2. C  
3. B  
4. B  
5. A  
6. B  
7. B  
8. D  
9. B  
10. A

---

# 6 — Quick Reference Snippets (for exercises)

- Start MLflow UI locally:
```bash
pip install mlflow
mlflow ui
# Visit: http://127.0.0.1:5000
```

- Basic logger pattern in a notebook:
```python
import mlflow
from sklearn.metrics import classification_report

mlflow.set_experiment("anomal_detection")
mlflow.set_tracking_uri("http://127.0.0.1:5000")

with mlflow.start_run(run_name="xgb_smote_v1"):
    # train model -> model
    report = classification_report(y_true, y_pred, output_dict=True)
    mlflow.log_params({"model": "xgboost", "use_smote": True})
    mlflow.log_metrics({
        "accuracy": report["accuracy"],
        "recall_class_1": report["1"]["recall"],
        "f1_macro": report["macro avg"]["f1-score"]
    })
    mlflow.xgboost.log_model(model, artifact_path="model")
```

- Register model from run:
```python
run_id = "<paste_run_id_here>"
model_uri = f"runs:/{run_id}/model"
mlflow.register_model(model_uri, name="anomaly_candidate")
```

- Load registered model by alias:
```python
loaded = mlflow.xgboost.load_model("models:/anomaly_candidate@Challenger")
y_pred = loaded.predict(X_test)
```

- Use `dagshub` to init tracking (example):
```python
# pip install dagshub
import dagshub
dagshub.init(repo_owner="your_user", repo_name="your_repo", mlflow=True)
# Or set env vars:
# import os
# os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/your_user/your_repo.mlflow"
# os.environ["MLFLOW_TRACKING_USERNAME"]="your_user"
# os.environ["MLFLOW_TRACKING_PASSWORD"]="your_token"
```

---

# 7 — Instructor / Assessment Notes (for trainers)

- Suggested time allotment per scenario:
  - Basic local tracking: 45–60 minutes
  - Loop experiments + compare: 60–90 minutes
  - Register + alias promotion: 30–45 minutes
  - DagsHub integration: 60–120 minutes (account setup may add time)
- Suggested automated checks a grader can add:
  - Verify MLflow experiment exists with expected runs via MLflow REST API.
  - Check registered model names and versions via `MlflowClient.list_registered_models()`.
  - Run `mlflow.models.load_model(uri)` and confirm `predict` returns expected shape.

---

If you want, I can:
- Produce ready-to-run minimal notebooks for each scenario (with placeholders for tokens).
- Create a graded Jupyter assignment with automated validation (nbgrader-style).
- Generate slides or a one-page checklist for teams to adopt MLflow + DagsHub.

Which would you like next?