# ML Ops — Structured Knowledge (from the transcription)

Below is a structured, student-ready extraction of the lecture: key terms and precise definitions, useful analogies, a conceptual mind‑map showing relationships, and reflection questions to deepen understanding.

---

# Key Terms & Definitions

- **MLOps**  
  *A set of practices (not a single tool)* that aims to deploy, operate, and maintain machine learning models in production reliably and efficiently. It extends DevOps to include machine learning and data-science artifacts as first-class citizens.

- **DevOps**  
  Practices and tooling to automate and integrate development and operations; MLOps is an extension of DevOps that accounts for models, datasets, and experiment artifacts.

- **Pipeline (ML pipeline)**  
  A high-level, ordered workflow of steps that transforms raw inputs into a final ML product (e.g., data ingestion → preprocessing → feature engineering → training → evaluation → deployment).

- **Step**  
  A single unit/task in a pipeline (e.g., a function decorated with `@step` in ZenML) that consumes inputs and produces artifacts.

- **ZenML**  
  An open-source MLOps framework used to build and orchestrate pipelines and steps, with features like caching, artifact management, and integrations (e.g., MLflow).

- **MLflow**  
  An experiment tracking and model management system used to log experiments (parameters, metrics, artifacts) and deploy models.

- **Artifact**  
  Any output produced by a step (datasets, trained models, metrics, logs). Artifacts are stored for traceability and reproducibility.

- **Orchestrator**  
  Component that executes pipeline steps in the desired environment/scheduling system (e.g., local, Kubernetes).

- **Artifact store**  
  Storage (local or remote) holding artifacts produced by steps (e.g., models, data snapshots, metrics).

- **Stack (ZenML stack)**  
  A configured set of components (orchestrator, artifact store, experiment tracker, model deployer) used by ZenML pipelines.

- **Experiment tracking**  
  The practice of recording run metadata — parameters, metrics, artifacts — to compare and reproduce experiments (MLflow is an example).

- **Model deployer**  
  Component or service that exposes a trained model for inference (e.g., MLflow Model Deployer, Seldon Core, etc.).

- **Materializer**  
  In ZenML context, a converter that knows how to serialize/deserialize a type (e.g., pandas DataFrame, sklearn model) to/from the artifact store.

- **Caching (step caching)**  
  Re-using a previously computed step output when the step code and inputs haven’t changed. Speeds up runs by avoiding recomputation.

- **Continuous Deployment (CD) pipeline**  
  A pipeline that can automatically deploy a model when a deployment criterion (e.g., metric threshold) is met.

- **Inference pipeline**  
  Pipeline focused on loading a deployed model/service and sending data to it to obtain predictions.

- **Model drift / Performance decay**  
  Degradation of model performance over time due to changes in data distribution or environment (data‑drift, concept‑drift).

- **Data drift**  
  Changes in input data distribution over time causing the model’s assumptions to break.

- **Latency**  
  Time taken for the model/service to respond to a prediction request. High latency negatively impacts user experience.

- **Fairness / Bias**  
  The property that model outputs don’t systematically disadvantage certain groups. Fairness issues must be monitored and mitigated.

- **Explainability / Auditability**  
  Ability to understand why a model made a decision and to produce logs/records for audits and compliance.

- **Model-centric approach**  
  Focus on improving model algorithms/architecture and hyperparameters while keeping data fixed.

- **Data-centric approach**  
  Focus on improving data quality, labels, coverage, and preprocessing while keeping the model fixed. Recommended by the instructor.

- **Feature engineering**  
  The process of creating, transforming, and selecting input features that improve model performance.

- **Business value & ROI**  
  Before building a model, quantify the expected business benefit versus development and maintenance costs.

- **CI/CD for ML (MLOps CI/CD)**  
  Automate retraining, validation, and redeployment of models via pipelines and integration with orchestration/stack components.

---

# Helpful Analogies (to solidify intuition)

- **City vs. Building (MLOps analogy)**  
  - The ML *model* is like a *single building*.  
  - MLOps is the *entire city infrastructure* (power, roads, maintenance, governance, security).  
  - Companies want full *cities* (end-to-end production systems), not standalone buildings (models).

- **Movie Production (Pipeline analogy)**  
  - Script → Casting → Filming → Editing → Distribution.  
  - Each task depends on the previous. Similarly, ML pipelines are ordered steps (data prep → feature engineering → training → evaluation → deployment).

- **Loop / Thermostat (Production loop)**  
  - Production ML is a continuous loop: collect → train → deploy → monitor → collect.  
  - Like a thermostat constantly reading temperature and adjusting HVAC; production pipelines must continuously respond to changing inputs and behavior.

- **Caching as Using Previously Edited Footage**  
  - Caching a pipeline step is like reusing previously edited footage when nothing affecting that footage changed—no need to redo the edit.

---

# Conceptual Mind Map (simplified, hierarchical)

```
Business Problem
├─ Value Proposition (who benefits, ROI)
├─ Costs & Constraints (wrong-prediction cost, storage, labeling)
└─ Solution Design (ML or not?)
    ├─ ML Canvas
    │   ├─ Data Sources (DBs, APIs, open datasets)
    │   ├─ Prediction Task (classification/regression/...)
    │   ├─ Feature Engineering (domain experts)
    │   ├─ Offline Evaluation (metrics, test sets)
    │   ├─ Pre-deployment checks (errors, UX)
    │   ├─ Monitoring & Retraining (frequency + cost)
    │   └─ Deployment Strategy (batch/online/service)
    └─ MLOps Implementation
        ├─ Artifacts
        │   ├─ Data
        │   ├─ Model
        │   └─ Code
        ├─ Phases
        │   ├─ Data Engineering (ingest, validate, split)
        │   ├─ Model Engineering (train, eval, package)
        │   └─ Code Engineering (deploy, serve, monitor)
        ├─ Pipelines & Steps (ZenML)
        │   ├─ Ingest Step
        │   ├─ Clean Step
        │   ├─ Train Step (autolog with MLflow)
        │   ├─ Evaluate Step (metrics)
        │   └─ Deploy Step (MLflow deployer)
        ├─ Tooling
        │   ├─ ZenML (pipelines, caching, stacks)
        │   ├─ MLflow (tracking + deploy)
        │   ├─ Orchestrator (execution)
        │   └─ Artifact Store
        └─ Operational Concerns
            ├─ Caching & reproducibility
            ├─ Experiment tracking (MLflow)
            ├─ Deployment decisions (metric thresholds)
            ├─ Monitoring (latency, drift, fairness)
            └─ Governance (legal, explainability, audit logs)
```

---

# Core Principles (compact)

- Start with the *business problem* and ROI, not the model.
- Treat *data*, *model*, and *code* as first-class production artifacts.
- Use *pipelines* to structure reproducible workflows; use *steps* to modularize tasks.
- *Experiment track* everything (parameters, metrics, artifacts) to compare runs.
- Make *deployment decisions* explicit (e.g., threshold on R²) and automate deploys only when criteria are met.
- Continuously *monitor* models in production for drift, latency, fairness, and explainability.
- Favor *data-centric* improvements over endless model tweaks (unless needed).
- Use *caching* to save time, but re-run steps when inputs/code change.
- Plan for *maintenance cost*: retraining frequency, data labeling, storage, compute, human oversight.

---

# Practical Patterns & Implementation Notes (from code walkthrough)

- Implement step functions with clear inputs/outputs and use type hints (e.g., `Annotated[np.ndarray, ...]`) for clarity and ZenML artifact typing.
- Use Strategy Pattern for data processing: define an abstract `DataStrategy` then `DataPreprocessStrategy` and `DataDivideStrategy`.
- Keep models modular: abstract `Model` class with concrete implementations (e.g., `LinearRegressionModel`).
- Log experiments and model artifacts using MLflow (e.g., `mlflow.sklearn.autolog()` in training step).
- Use `DeploymentTrigger` step (a simple boolean) to decide whether to deploy (based on metric thresholds).
- For deployment: MLflow local deployer can start a local service; have a `prediction_service_loader` that finds and starts the service.
- For inference: implement a `dynamic_importer` to fetch test data and a `predictor` step to call the model service and log predictions.
- Expose a simple UI (Streamlit) that uses the deployed service for single-record predictions (no local joblib loading).

---

# Reflection Questions (to deepen understanding)

1. Why should an ML project start by defining the business problem and ROI rather than selecting a model first?
2. The instructor said the ML code is ~20% of an ML project. Which parts make up the remaining 80% and why are they critical?
3. Compare and contrast model-centric and data-centric approaches. In what scenarios would you pick one over the other?
4. What are the trade-offs between deploying a very large model (e.g., 120B parameters) and user latency requirements? How would you mitigate latency?
5. Describe a realistic sequence of events that would cause a deployed fraud-detection model to degrade. How would you design an MLOps pipeline to respond automatically?
6. What does step caching buy you in practice? When might caching be dangerous or misleading?
7. How does experiment tracking (e.g., MLflow) improve reproducibility and team collaboration? Give an example workflow that highlights these benefits.
8. What are the minimal set of artifacts and metadata you would store to be able to reproduce any past pipeline run?
9. How do you decide the metric threshold for automatic deployment (deployment trigger)? What could go wrong if you set it too low or too high?
10. What legal and ethical checks (e.g., data usage permissions, fairness tests) should be part of a production pipeline before deploy? How would you automate them?
11. Why is monitoring for fairness and explainability important after deployment? Give an example of a fairness failure and the immediate mitigation steps.
12. How would you handle a model that performs well offline (test dataset) but poorly in production? Outline diagnosis steps.
13. When integrating a model service into a user-facing product, what operational metrics (beyond accuracy) would you monitor?
14. Describe an end-to-end checklist you would follow before marking a model as “production-ready”.
15. If you are building your MLOps skills to get job offers abroad while working remotely, which parts of the stack should you prioritize learning and why?

---

# Quick Reference Commands & Snippets (contextual)

- Initialize ZenML repository:
```bash
zenml init
```

- Start ZenML server:
```bash
zenml up
# open the provided URL, login default/default
```

- Install MLflow integration for ZenML:
```bash
zenml integration install mlflow
```

- Example pipeline run (Python):
```python
from pipelines.training_pipeline import training_pipeline
training_pipeline(data_path="data/customer_data.csv")
```

- Get MLflow tracking URI from active stack (Python snippet):
```python
from zenml.client import Client
client = Client()
print(client.active_stack.experiment_tracker.get_tracking_uri())
```

- Start MLflow UI locally pointing to a URI:
```bash
mlflow ui --backend-store-uri <TRACKING_URI>
```

- Run a CLI script to deploy or predict:
```bash
python run_deployment.py --config deploy --min-accuracy 0.9
python run_deployment.py --config predict
```

---

# Short Checklist for an MLOps Project MVP

- [ ] Define business problem and ROI estimate.
- [ ] Collect and document data sources and costs.
- [ ] Build a pipeline skeleton (ingest → clean → train → evaluate → deploy).
- [ ] Implement step-level unit tests or sanity checks.
- [ ] Add experiment tracking (auto-logging for training).
- [ ] Add a deployment decision (metric threshold).
- [ ] Deploy to a reproducible stack (artifact store + deployer).
- [ ] Add monitoring for drift, latency, and errors.
- [ ] Add basic governance checks (data privacy, usage consent).
- [ ] Document the run and reproducibility steps.

---

If you want, I can:
- Produce a one-page checklist you can print and follow during your project.
- Convert the mind map into a visual (SVG/PNG) you can include in project docs.
- Create example ZenML/MLflow minimal code templates (ingest → train → eval) you can copy-into your repo.

Which of these would be most helpful next?