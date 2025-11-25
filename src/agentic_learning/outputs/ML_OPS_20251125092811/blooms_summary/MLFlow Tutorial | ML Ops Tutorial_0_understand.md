# MLflow, Experiment Tracking & Model Registry — Structured Knowledge

Below is a focused, structured extraction of the fundamental concepts and principles from the transcription. It includes **key terms with precise definitions**, **concise analogies** to clarify core ideas, a simplified **conceptual mind map** showing relationships, and **reflection questions** to deepen understanding and prompt practical thinking.

---

# 1. Key Terms and Definitions

- **MLOps**
  - *Definition:* Practices and tooling that bring software engineering discipline (CI/CD, monitoring, versioning, collaboration) to the lifecycle of machine learning systems.
- **MLflow**
  - *Definition:* An open-source platform that supports tracking experiments, packaging models, and managing model lifecycles (including a Model Registry). It provides APIs and a UI for logging, viewing, and deploying ML artifacts.
- **Experiment Tracking**
  - *Definition:* The process of recording runs/experiments with their hyperparameters, metrics, artifacts, and metadata so that experiments are discoverable, comparable, and reproducible.
- **Run**
  - *Definition:* A single execution of training/evaluation logged by MLflow. Each run has a unique **Run ID** and can contain parameters, metrics, and artifacts.
- **Run ID**
  - *Definition:* A unique identifier for a run (a long string) used to reference the run and its artifacts.
- **Tracking URI**
  - *Definition:* The endpoint (local or remote) to which MLflow clients send logged information (e.g., `http://localhost:5000` for local MLflow UI or a cloud-hosted MLflow endpoint).
- **Parameter (param)**
  - *Definition:* A recorded hyperparameter or configuration value used for a run (e.g., `C=0.1` for logistic regression).
- **Metric**
  - *Definition:* A numeric measured outcome of a run (e.g., accuracy, precision, recall, F1). Metrics can be compared across runs.
- **Artifact**
  - *Definition:* Files produced by runs—models (`.pkl`, `.xgb`), `requirements.txt`, `conda.yaml`, plots, data snapshots—stored and downloadable from MLflow.
- **Artifact Path / artifact_path**
  - *Definition:* A named location within a run where artifacts (like the saved model) are stored (e.g., `"logistic_regression"`).
- **Model Registry**
  - *Definition:* A centralized place in MLflow to register models, track versions, add descriptions/tags/aliases, and manage lifecycle stages (e.g., Staging, Production).
- **Model Version**
  - *Definition:* A numbered entry for a registered model. Each registration from a run becomes a new version (V1, V2, ...).
- **Aliases (Champion / Challenger)**
  - *Definition:* Human-friendly labels assigned to model versions. Typical pattern: `Champion` = production model, `Challenger` = candidate model under evaluation.
- **Model URI formats**
  - *Definition:* Ways to reference models:
    - `runs:/<run_id>/<artifact_path>` — refer to model artifact in a specific run.
    - `models:/<model_name>/<version>` — load by registered model name and version.
    - `models:/<model_name>@<alias>` — load by registered model alias (e.g., `@Challenger`).
- **mlflow.log_params / mlflow.log_metrics / mlflow.sklearn.log_model / mlflow.xgboost.log_model**
  - *Definition:* API calls to save parameters, metrics, and model artifacts to the tracking server.
- **MlflowClient (or MlflowClient API)**
  - *Definition:* Programmatic client to manage registry operations (copying versions, transitioning stages, updating descriptions).
- **DagsHub**
  - *Definition:* A cloud platform that integrates Git-like code versioning with dataset versioning and provides a hosted MLflow tracking server for centralized experiment collaboration.
- **SMOTETomek (or SMOTE)**
  - *Definition:* Techniques for handling class imbalance: SMOTE (Synthetic Minority Oversampling Technique) oversamples minority class; Tomek links are used to clean ambiguous samples—often combined.
- **Precision / Recall / F1 / Accuracy**
  - *Definition:* Standard classification metrics:
    - *Precision:* TP / (TP + FP) — correctness of positive predictions.
    - *Recall:* TP / (TP + FN) — how many positive cases were found (critical for anomaly/fraud detection).
    - *F1:* Harmonic mean of precision and recall.
    - *Accuracy:* (TP + TN) / total.
- **CI/CD (Jenkins, pipelines)**
  - *Definition:* Continuous Integration / Continuous Deployment tools used to automate testing, packaging, and deployment of models and ML workflows.
- **Conda.yaml / requirements.txt**
  - *Definition:* Environment specification files saved with model artifacts to enable reproducible runtime for deployment.

---

# 2. Core Ideas Explained with Analogies

- **MLflow is like a lab notebook + specimen cabinet for ML experiments**
  - Lab notebook = experiment tracking (parameters, metrics, notes).
  - Specimen cabinet = artifact storage (models, environment files), where each specimen is labeled by run ID and version.
- **Runs are experiments on a lab bench**
  - Each run = one experiment trial with a recipe (params) and measured outcomes (metrics) and stored samples (artifacts).
- **Excel/Google Sheets approach is like keeping post-it notes instead of lab notebooks**
  - Fragile, error-prone, no direct link to the specimen (model artifact), no reproducible way to fetch the exact sample.
- **Model Registry is a museum archive for finalized artifacts**
  - Each model version is a cataloged exhibit; aliases (Champion/Challenger) are temporary exhibition labels indicating current production vs candidate.
- **DagsHub is like a centralized research institute**
  - It hosts the lab notebooks (code), the data vault (dataset versions), and a public catalog (MLflow server) so multiple researchers can collaborate and access the same experiments and artifacts.
- **Champion vs Challenger is A/B testing for models**
  - Champion = current live model; Challenger = new model being tested — like a challenger athlete trying to beat the champion in a match.

---

# 3. Conceptual Mind Map (Simplified)

Use this hierarchical map to visualize relationships. The top-level is MLflow; branches show capabilities and integrations.

- MLflow
  - Experiment Tracking
    - Runs
      - Run ID
      - Parameters (mlflow.log_params)
      - Metrics (mlflow.log_metrics)
      - Artifacts (mlflow.log_model → artifact_path)
    - UI
      - List experiments
      - Compare runs
      - Charts & Tables
    - Local vs Remote
      - Local: `mlflow ui` → `http://localhost:5000`
      - Remote: Tracking URI (DagsHub, Databricks, AWS)
  - Model Registry
    - Register model (mlflow.register_model)
      - model_uri: `runs:/<run_id>/<artifact_path>`
      - name: `<model_name>`
    - Versions (V1, V2, ...)
    - Aliases / Stages (Challenger, Champion, Staging, Production)
    - Load model
      - `models:/<model_name>/<version>` or `models:/<model_name>@<alias>`
    - MlflowClient
      - copy / transition / set alias
  - Artifacts & Reproducibility
    - `requirements.txt`, `conda.yaml`
    - Download model artifacts for Docker packaging / deployment
  - Integration & Automation
    - CI/CD (Jenkins pipelines)
    - Cloud providers (Databricks, AWS, etc.)
    - DagsHub for centralization
- DagsHub
  - Git + data versioning + hosted MLflow
  - Repo integration (connect GitHub)
  - Centralized tracking URI, credentials (username/token)
  - Team collaboration: shared experiments and artifacts
- Model Development Workflow (practical flow)
  - Data v1 / v2 → Feature engineering → Train models (LR, RF, XGB, XGB+SMOTE) → Log runs → Compare metrics (focus metric e.g., recall for minority class) → Register best run → Assign alias → Promote to production via MlflowClient → Deploy (Docker/Cloud) → Monitor & retrain

(Short code examples — model URIs)

```python
# Examples of URIs referenced in MLflow
# Register model from a run artifact:
model_uri = "runs:/<run_id>/model"  # artifact path 'model' inside the run

# Load by registered name + version:
loaded = mlflow.xgboost.load_model("models:/xgb_sm/1")

# Load by alias:
loaded = mlflow.xgboost.load_model("models:/xgb_sm@Challenger")
```

---

# 4. Reflection Questions (to deepen understanding and practice)

Practical / design questions:
1. Why is *recall for the minority class* often prioritized in anomaly/fraud detection? What are the consequences of optimizing for recall only (what happens to precision)?
2. What information should you always log for a run so another teammate can reproduce the model exactly?
3. How would you design a naming convention for experiments and runs to make search/discovery easier in a team of 10 data scientists?
4. When registering a model to the Model Registry, what metadata and tags would you add to make the model discoverable and understandable later?
5. How do `requirements.txt` and `conda.yaml` files help with reproducibility? When would each be more appropriate?

Operational / architecture questions:
6. Compare running MLflow locally vs using a hosted MLflow endpoint (DagsHub). What are the advantages and limitations of each?
7. How would you integrate MLflow model registration and promotion into a CI/CD pipeline (Jenkins/GitHub Actions)? Outline a simple pipeline that promotes a model from Dev → Staging → Production.
8. What access controls (authentication/authorization) should be in place on a shared MLflow server used by multiple teams?
9. How can you automate the selection of a "Champion" model using metrics thresholds? What risks exist with automated promotion?
10. How would you version datasets and tie a specific dataset version to a logged run? What are the pitfalls of not versioning datasets?

Modeling / metrics questions:
11. When comparing models in MLflow, why might you want to look beyond a single scalar metric (e.g., recall) and inspect other metrics or runtime/system metrics?
12. What trade-offs are commonly observed when using oversampling (SMOTE) vs algorithmic or loss-level approaches for class imbalance?
13. How would you validate that a model loaded from the Model Registry behaves identically to the original run output?
14. If two models have similar recall but different inference latency, how would you decide which to deploy?

Team & process questions:
15. If multiple data scientists push runs to the same centralized MLflow server, how would you avoid name collisions and ensure consistent metadata?
16. What workflows or checks would you build to guarantee that the person who registers or promotes a model understands business requirements (not just raw metric improvements)?
17. How could you demonstrate to a non-technical stakeholder (e.g., team lead) why the chosen model is preferable? What visualizations or comparisons would be most persuasive?

Exploratory / research questions:
18. Which MLflow features would you use to track experiments that include data labeling steps or data augmentation artifacts?
19. How would you extend MLflow usage to support online learning or streaming models where regular periodic evaluation is required?
20. What are the limits of MLflow for large-scale model management (e.g., thousands of models), and what additional systems/controls might you need?

---

# 5. Quick Practical Tips (extracted from the transcription)

- Install MLflow: `pip install mlflow`
- Launch local UI: `mlflow ui` → visit `http://localhost:5000`
- Set tracking URI in notebooks to point to the server: `mlflow.set_tracking_uri("http://127.0.0.1:5000")` or to DagsHub URI for central tracking.
- Use `classification_report(..., output_dict=True)` to get metrics as a dict, then `mlflow.log_metrics(...)`.
- Log entire hyperparameter dictionaries with `mlflow.log_params(params_dict)` to keep param metadata consistent.
- Use `mlflow.sklearn.log_model` or `mlflow.xgboost.log_model` to log model artifacts and environment files.
- Use `mlflow.register_model(model_uri, name)` to register chosen run artifact into Model Registry.
- Load registered models by `models:/<name>/<version>` or `models:/<name>@<alias>` for reproducible inference.
- For team centralization, use DagsHub (or Databricks/AWS) and set environment variables for username/token and tracking URI.
- Use aliases (`Champion`/`Challenger`) and versions for safe model promotion workflows.
- Package the model plus `requirements.txt` or `conda.yaml` for Dockerized deployment.

---

If you want, I can:
- Generate a short checklist to adopt MLflow + DagsHub in a small team (practical steps).
- Produce a template for experiment naming, param logging, and model description to standardize team practices.
- Provide a minimal reproducible example notebook snippet showing training, logging, and registering a model.

Which of those would help you next?