# MLflow & DagsHub – Memory Aids for Subject Properties

Below are **mnemonics, flashcards, vivid stories, and acronyms** to help you remember the **key concepts and properties** of MLflow, Experiment Tracking, Model Registry, and DagsHub.

---

## 1. Core Mnemonics

### 1.1 What MLflow DOES – **"MLFLOW TRACKS"**

Remember MLflow’s core functions with:

**MLFLOW TRACKS**

- **M** – **Manage** experiments (group runs into experiments)
- **L** – **Log**  
  - **P**arameters (`log_params`)  
  - **M**etrics (`log_metrics`)  
  - **A**rtifacts (`log_model`, files)
- **F** – **Find** best models via comparison UI
- **L** – **Link** runs to datasets, code, and environment
- **O** – **Organize** models into a Model Registry
- **W** – **Workflow** from Dev → Staging → Prod

**TRACKS** (what it “tracks”):  
- **T** – **Tracking URI** (where logs go: local or remote)  
- **R** – **Run IDs** (unique identifiers for experiments)  
- **A** – **Artifacts** (model files, `requirements.txt`, `conda.yaml`)  
- **C** – **Compare** runs (tables, charts, scatter plots)  
- **K** – **Key metrics** (accuracy, precision, recall, F1, etc.)  
- **S** – **Stages** / aliases (Champion, Challenger) in Model Registry  

---

### 1.2 Elements of a Run – **"P-M-A-R"**

Each MLflow run has:

**P-M-A-R = Parameters – Metrics – Artifacts – Run ID**

- **P** – *Parameters* = hyperparameters/configs (`C`, `n_estimators`)
- **M** – *Metrics* = outputs (accuracy, recall, F1, etc.)
- **A** – *Artifacts* = physical files (models, env files, plots)
- **R** – *Run ID* = unique handle to this run

You can say:  
> “**Every run is PMAR** — Parameters, Metrics, Artifacts, Run ID.”

---

### 1.3 Model Registry Lifecycle – **"D-E-V to P-R-O-D"**

For model life cycle:

**DEV → PROD**

- **D** – **Decide** best run (e.g., highest recall for class 1)
- **E** – **Enroll** in registry (`register_model`)
- **V** – **Version** it (V1, V2, ...)

Then:

- **P** – **Promote** best version to production name
- **R** – **Rename / alias**: `Champion`, `Challenger`
- **O** – **Observe** metrics & behavior
- **D** – **Deploy** via Docker/Cloud using saved artifacts

---

### 1.4 MLflow Model URIs – **"R-M-A" formats**

Three common URI formats:

**R-M-A = Runs, Models by version, Alias**

- **R** – `runs:/<run_id>/<artifact_path>`  
  *Use to register models from a run.*

- **M** – `models:/<model_name>/<version>`  
  *Use to load a specific version.*

- **A** – `models:/<model_name>@<alias>`  
  *Use to load by alias (`@Champion`, `@Challenger`).*

---

### 1.5 DagsHub Purpose – **"DAGSHUB"**

Remember DagsHub’s core properties with:

**DAGSHUB**

- **D** – **Data** & **code** versioning (like Git for ML projects)
- **A** – **Annotate** and manage datasets
- **G** – **Git-like** repos (mirrors GitHub)
- **S** – **Shared** MLflow server (central tracking URI)
- **H** – **Hosted** in the cloud (no local server to maintain)
- **U** – **Unified** view: code + data + experiments
- **B** – **Better collaboration** (team-wide experiment tracking)

---

### 1.6 Choosing Metrics in Anomaly Detection – **"R1 FIRST"**

For anomaly detection/fraud detection, recall for class 1 is vital:

**R1 FIRST**

- **R1** – **Recall for Class 1** (minority/anomaly/fraud)
- **F** – It’s the **First** priority
- **I** – Even if **Imbalance** exists
- **R** – Be willing to **Reduce precision**
- **S** – Use **SMOTE / SMOTETomek** to boost recall
- **T** – **Tune** trade-offs with F1 & precision

---

## 2. Flashcards (Q–A Style)

### 2.1 MLflow Basics

**Q:** What problem does MLflow mainly solve in a data science team?  
**A:** It solves chaotic experiment tracking by centrally logging parameters, metrics, and artifacts, making experiments searchable, comparable, and reproducible, and supporting deployment via a Model Registry.

---

**Q:** What are the four key components logged in an MLflow run?  
**A:** **P-M-A-R** – Parameters, Metrics, Artifacts, and Run ID.

---

**Q:** What command launches a local MLflow UI?  
**A:**
```bash
mlflow ui
```
It runs typically on `http://localhost:5000`.

---

**Q:** What is a Tracking URI in MLflow?  
**A:** The endpoint where all logged runs go (e.g., `http://127.0.0.1:5000` locally, or a DagsHub/Databricks/AWS MLflow URL in the cloud).

---

### 2.2 Parameters, Metrics, and Artifacts

**Q:** Which MLflow functions log hyperparameters and metrics?  
**A:** `mlflow.log_params()` for multiple hyperparameters, `mlflow.log_param()` for single; `mlflow.log_metrics()` and `mlflow.log_metric()` for performance metrics.

---

**Q:** What is an MLflow artifact?  
**A:** Any file saved with the run (e.g., trained model binary, `requirements.txt`, `conda.yaml`, plots, data snapshots).

---

**Q:** Why are `requirements.txt` and `conda.yaml` artifacts important?  
**A:** They capture the environment (library versions) to **reproduce** and **deploy** the model reliably, e.g., in Docker or cloud.

---

### 2.3 Model Registry

**Q:** What is the MLflow Model Registry used for?  
**A:** To **register**, **version**, **describe**, and **stage** models (e.g., Dev/Prod) so teams can manage lifecycles and deployments.

---

**Q:** How do you reference a registered model by version?  
**A:** Via `models:/<model_name>/<version>`, e.g., `models:/xgb_sm/1`.

---

**Q:** How do you reference a registered model by alias?  
**A:** Via `models:/<model_name>@<alias>`, e.g., `models:/xgb_sm@Challenger`.

---

**Q:** What’s the typical meaning of `Champion` and `Challenger` aliases?  
**A:** `Champion` = current production model; `Challenger` = candidate model trying to replace Champion.

---

### 2.4 Anomaly Detection Focus

**Q:** In anomaly/fraud detection, which metric is usually most critical?  
**A:** **Recall for the minority class (class 1)** because missing anomalies (false negatives) is more costly than raising some false alarms.

---

**Q:** What is SMOTETomek used for in this context?  
**A:** For handling class imbalance by oversampling the minority class (SMOTE) and cleaning via Tomek links, often increasing recall for class 1.

---

### 2.5 DagsHub Integration

**Q:** How does DagsHub extend MLflow usage?  
**A:** DagsHub hosts a **central MLflow tracking server** plus code and data repositories, allowing team-wide, cloud-based experiment tracking.

---

**Q:** What environment variables are commonly set for using MLflow with DagsHub?  
**A:** `MLFLOW_TRACKING_USERNAME`, `MLFLOW_TRACKING_PASSWORD` (token), and `MLFLOW_TRACKING_URI`.

---

**Q:** How do you initialize MLflow tracking to DagsHub in a notebook?  
**A (example):**
```python
import dagshub
dagshub.init(repo_owner="user", repo_name="repo", mlflow=True)
```
This sets up MLflow tracking URI to DagsHub.

---

### 2.6 Comparison & Selection

**Q:** How do you compare multiple runs in MLflow UI?  
**A:** Select them with checkboxes in an experiment → click **Compare** → inspect charts, tables, scatter plots of metrics.

---

**Q:** How can you visually choose the best model when plotting F1 vs recall for class 1?  
**A:** Look for models in the **top-right quadrant** (high F1 and high recall for class 1).

---

**Q:** Why do we prefer model registration after evaluating all experiments rather than during each run?  
**A:** It allows you to **compare all models first** (e.g., focusing on recall for class 1) and register only the best-performing candidate into the registry.

---

## 3. Vivid Story for Long-Term Memory

### Story: "The Lab of Lost Models"

Imagine a **data science lab** working on **anomaly detection** for a big bank.  

- **Kathy** and **Wut** are two scientists.  
  - Kathy uses **Logistic Regression** with dataset **V1**, then **V2** when a new feature **F10** is added.  
  - Wut works on dataset **V10** with severe class imbalance, trying **Random Forest** and **XGBoost** while applying **SMOTETomek** for oversampling.

Their desks are buried under **27 notebooks**, each with slightly different parameters and datasets.  
When **Tony**, their team lead, asks:

> “Show me your best model for detecting fraud, especially catching as many frauds (class 1) as possible!”

They:

- Scroll painfully through large notebooks.
- Squint at **precision**, **recall**, and **F1** numbers.
- Try to remember which notebook used which dataset version.
- Write final metrics into a **shared Excel sheet**.

Tony is frustrated:

> “Every time I visit, it’s like opening a messy shop. You tell me recall is 0.83 for model ‘S’, but there’s no button to get the actual model! You have to go back, dig up the notebook, export `.pkl`, and email it!”

The **Excel** method is like writing results on sticky notes—easy to lose, impossible to tie back to a specific *model file* and *environment*.

Then they discover **MLflow**.

Suddenly, there’s a **digital lab notebook and cabinet**:

- Every training **Run** has:
  - **Parameters** (hyperparameters),
  - **Metrics** (accuracy, recall_class_1, F1_macro),
  - **Artifacts**: the model, environment files,
  - and a **Run ID** on the label.

Now, Tony opens the MLflow **UI**:

- He sees **experiments** like “anomal_detection”.
- Each model run is clearly labeled: `Logistic Regression`, `Random Forest`, `XGB`, `XGB + SMOTETomek`.
- He clicks **Compare** and sees:
  - For class 1 recall:
    - Logistic Regression ~0.5
    - Random Forest is better
    - XGB is better still
    - **XGB + SMOTETomek** gives recall ~0.83 (best).

Tony says:

> “We need the model that catches the most frauds — XGB with SMOTETomek!”

No more hunting. They **register** this best run as a model:

- Add it to **Model Registry** as `xgb_sm`.
- Version 1 is created with alias **Challenger**.

Later, after additional testing, they promote it:

- Using the MLflow **client**, they **copy** it as a **production model** name.
- Assign alias **Champion** to the production version.
- Deployment engineers just load `"models:/prod_model@Champion"` and pack it into a Docker image using the included `requirements.txt` and `conda.yaml`.

Now, **another team** joins the lab, working remotely. Instead of running MLflow locally, they use **DagsHub**:

- The **GitHub repository** is mirrored to DagsHub.
- Datasets and experiments are centrally logged.
- All data scientists share the same **MLflow Tracking URI** hosted by DagsHub.
- Everyone can see Kathy’s and Wut’s experiments in one place.

The lab is no longer “The Lab of Lost Models” — it’s now a **disciplined ML Factory**.

Whenever Tony asks:

> “Which model is our Champion today, and what’s its recall on class 1?”

The answer is one click away in the MLflow UI.

---

## 4. Targeted Acronyms for Properties and Concepts

### 4.1 Experiment Properties – **"CLEAR"**

An ML experiment in MLflow should be **CLEAR**:

- **C** – **Config**: log **parameters** (hyperparameters, seeds)
- **L** – **Logs**: log **metrics** (accuracy, recall, F1, etc.)
- **E** – **Environment**: capture dependencies (`requirements.txt`, `conda.yaml`)
- **A** – **Artifacts**: store models, plots, important files
- **R** – **Run ID**: unique, reproducible identifier

---

### 4.2 Good Model Registry Practices – **"VITAL"**

A healthy Model Registry is **VITAL**:

- **V** – **Versions**: use V1, V2... for tracked improvement
- **I** – **Information**: descriptions & tags for context
- **T** – **Tags**: encode business area, dataset version, owner
- **A** – **Aliases**: Champion, Challenger, Staging, Prod
- **L** – **Loading**: easy loading for inference (`models:/name@alias`)

---

### 4.3 DagsHub–MLflow Team Setup – **"TEAM"**

For team-based tracking on DagsHub, remember **TEAM**:

- **T** – **Tracking URI** shared across team
- **E** – **Experiment visibility** (central MLflow UI)
- **A** – **Auth** with username + token env vars
- **M** – **Mirror** code and data from GitHub → DagsHub

---

### 4.4 Comparing Models – **"R-U-N-S BEST"**

How to pick the best model among runs:

**RUNS BEST**

- **R** – **Recall** for key class (e.g., class 1 in anomalies)
- **U** – **Understand** precision–recall trade-offs
- **N** – **Name** metrics clearly in MLflow logs
- **S** – **Scatter plots** F1 vs recall to spot top-right candidates

**BEST**

- **B** – **Benchmark** all models via MLflow Compare UI
- **E** – **Examine** runtime and system metrics
- **S** – **Select** candidate(s) for registration
- **T** – **Tag** them with clear descriptions and stage/alias

---

## 5. Mini Scenario Mnemonics (Very Short Stories)

### 5.1 Kathy’s Chaos vs MLflow Order

- Before MLflow:  
  “**Kathy’s 27 notebooks**” — each with tweaks, versions, random metrics.
- After MLflow:
  - Each trial is a **RUN**:
    - **R** – Run ID  
    - **U** – Unified info (params, metrics, artifacts)  
    - **N** – Named clearly  

> “Don’t keep **27 notebooks**. Keep **27 runs** in MLflow.”

---

### 5.2 Champion/Challenger Arena

Think of a **boxing ring**:

- **Champion** = current production model.
- **Challenger** = new model from the experiments.
- Promoting the Challenger:

  - Logging: `runs:/<run_id>/model`  
  - Registration: `xgb_sm`  
  - Alias update: switch `Champion` to new version.

> “The ring is the Registry; the belts are the Aliases.”

---

### 5.3 Excel Trap

Imagine an Excel sheet labeled “World’s Best Models”:

- Columns: owner, dataset version, model, parameters, recall.
- No model files. No run IDs. No environment.
- Tony chooses the best row, but **nobody can press a button to download it**.

Mnemonic:  
> “**Excel EXposes but can’t EXecute. MLflow LOGs and LOADs.**”

---

## 6. Quick Drill Cards (Rapid Recall)

Use these as 10-second mental checks.

1. **Card:** “P-M-A-R?”  
   **Answer:** Parameters, Metrics, Artifacts, Run ID.

2. **Card:** “three model URI types?”  
   **Answer:**  
   - `runs:/<run_id>/<artifact_path>`  
   - `models:/<name>/<version>`  
   - `models:/<name>@<alias>`

3. **Card:** “metric that matters most in anomaly detection?”  
   **Answer:** Recall for class 1 (minority class).

4. **Card:** “DAGSHUB stands for?”  
   **Answer:** Data & code, Annotate data, Git-like, Shared MLflow, Hosted, Unified, Better collaboration.

5. **Card:** “what’s Champion vs Challenger?”  
   **Answer:** Champion = production model; Challenger = candidate model under testing in the registry.

6. **Card:** “what files give reproducible environment in artifacts?”  
   **Answer:** `requirements.txt`, `conda.yaml` (and sometimes `python_env` files).

7. **Card:** “where do you see and compare experiments?”  
   **Answer:** In the MLflow **UI** under an **experiment** → **Compare**.

8. **Card:** “What is the ONE button Excel can’t give that MLflow does?”  
   **Answer:** Direct **download** of the actual model artifact linked to a set of metrics.

---

If you’d like, I can next:

- Turn this into a printable one-page **cheat sheet**, or  
- Create a short **quiz** (with answers) to test your memory of MLflow & DagsHub concepts.