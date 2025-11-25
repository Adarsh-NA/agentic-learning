# MLflow, Experiment Tracking, Model Registry, and DagsHub Integration – Complete Structured Summary

## 1. Overview and Purpose of MLflow

- **MLflow** is an important tool in **MLOps (Machine Learning Operations)**.
- In this tutorial, the instructor:
  - Explains **the purpose of MLflow**.
  - Installs **MLflow locally** on a computer.
  - Demonstrates **experiment tracking**.
  - Shows how to **deploy and track experiments on a centralized server in the cloud** using **DagsHub**.
- MLflow solves problems related to:
  - **Efficient experiment tracking**.
  - **Reproducibility**.
  - **Deployment**.
  - **Model management**, including **model registry** and **versioning** (e.g., V1, V2 models).
- It is a key component of **MLOps** and helps make **ML application development easier**.

---

## 2. The Problem MLflow Solves

### 2.1 Typical Scenario in a Data Science Team

- A data science team is working on an **anomaly detection problem**.
- Team members:
  - **Kathy** – a talented data scientist.
  - **Wut (also called Wuat / Wenat in the narration)** – another data scientist.
  - **Team lead** – **Mr. Tony Sharma**.

### 2.2 Kathy’s Work

- Kathy creates a **Jupyter notebook** where:
  - She uses **logistic regression** to train models.
  - She uses **dataset V1**:
    - `V1` means **Version 1** of the dataset.
  - She performs **experimentation**:
    - Trains **logistic regression** with different parameters (e.g., `C=1`, `C=0.1`, etc.).
  - This mirrors the idea of **grid search CV**, where multiple parameter combinations are tried to find the best-performing model.
- Over time:
  - She works on this problem for **about a month**.
  - The **business** informs her that:
    - The **dataset has changed**.
    - A new feature is introduced that should help model building.
    - The dataset is now **V2**, with a new feature `F10`.
    - Previously the dataset had features `F1` to `F9`.
- On Kathy’s computer:
  - There are **multiple notebooks**.
  - These notebooks have:
    - Different **dataset versions**.
    - Different **models**.
    - Different **parameters**.
    - Possibly different **feature engineering techniques**, etc.

### 2.3 Wut’s Work

- Another data scientist, **Wut**, is also working on the **same anomaly detection problem**, but:
  - He is using **dataset V10**.
  - His dataset is different because:
    - This is an **anomaly detection** problem.
    - The dataset is **imbalanced**.
  - The **team lead** has given him the task to:
    - **Handle class imbalance**, and
    - Use that imbalanced-handled dataset for training.
- Wut may be:
  - Using **random forest** with different parameters.
  - Handling **class imbalance**, whereas Kathy is **not**.
- Wut also has **multiple notebooks** (e.g., 4 different notebooks) on his computer.

### 2.4 Real-World Example from Instructor’s Company

- At the instructor’s company **Codebasics (referred to as "at Technologies" in narration)**:
  - They help a **client in North America** with an **anomaly detection problem**.
  - They have **two parallel initiatives**:
    - **Track A**:
      - Uses **time-lag**, **moving average**, and similar **time-series features**.
      - Goal: detect **peaks** and anomalies in time series.
    - **Track B**:
      - Uses **convolution features**.
      - Convolution features can also be used for **anomaly detection**.
  - Both tracks aim to solve **the same anomaly detection problem**, but with **different approaches** (similar to Kathy and Wut using different techniques).

### 2.5 Management and Visibility Problem

- **Tony (team lead)** visits Kathy:
  - Asks: “How is it going? Can you show me your model performance?”
  - Kathy:
    - Opens a notebook.
    - Scrolls through a long notebook.
    - Extracts metrics like **precision**, **recall**, etc.
    - Then looks at **another notebook** to find other runs and metrics.
    - She may have **27 different notebooks**, each with different models, datasets, parameters, etc.
  - Tony then goes to **Wut**, who does the **same process**:
    - Opens notebooks.
    - Scrolls.
    - Reads and reports **precision**, **recall**, etc.
  - Tony becomes **tired** of this inefficient process:
    - Every time he visits, they “open their shop” (open notebooks, search for metrics).
    - It’s hard to know **which dataset version** a model used.
    - They often **do not have a clear idea** of which data or parameters were used for a particular result.

### 2.6 Naive Solution: Using Excel or Google Sheets

- The team, though talented, initially comes up with a **naive but common idea**:
  - Log experiments in **Excel** or **Google Sheets**.
- They create a **shared spreadsheet** (e.g., on OneDrive or Google Drive) that includes:
  - Experiments conducted by Kathy and Wut.
  - **Columns** such as:
    - **Experiment owner** (e.g., Kathy – 4 experiments).
    - **Dates**.
    - **Model type** (e.g., logistic regression, random forest, xgboost).
    - **Parameters** used (e.g., `C`, `n_estimators`, etc.).
    - **Dataset version** (e.g., `V1`, `V2`, `V10`).
    - **Model metrics**:
      - Precision, recall, F1, accuracy, etc.
- This can potentially work, but has **many problems**:
  - They might **forget** to log an experiment.
  - They might **record numbers inaccurately**.
  - There is **no direct link** between metrics and actual model artifacts.

### 2.7 Deployment Problem with Excel-Based Tracking

- Suppose Tony looks at the Excel sheet and decides:
  - “This is anomaly detection, and I care about **recall for the minority class (class 1)**.”
  - He sees that recall for class 1 is **maximum in model S**.
  - He decides: “Let’s **deploy model S**.”
- Issues:
  - There is **no magic button** to **download model S** directly from Excel.
  - Wut (or Kathy) must:
    - Go to their local computer.
    - Find the right notebook/run.
    - Export the model to a file (e.g., `.joblib` or `.pkl`).
    - Send that file to Tony.
  - This is **inefficient** and **error-prone**.

### 2.8 Desired Tool Features

The team wants a better tool that:

- Shows **all experiments** and their metadata.
- Displays all **artifacts** (e.g., model files).
- Supports:
  - **Download of artifacts** (e.g., model binary).
  - **Viewing datasets** or references to them.
  - Inspecting **all parameters**.
  - **Comparing models** visually and numerically.
    - E.g., comparing experiments 5 and 7.
    - Displaying performance metrics in a nice UI.

Such a tool **exists** and is called **MLflow**.

---

## 3. What MLflow Provides

- **UI Capabilities**:
  - View **all experiments** (grouped logically).
  - View **models** and specific model runs.
  - See all **parameters**, **metrics**, and **artifacts** for each run.
  - Compare multiple runs:
    - Select multiple runs (e.g., run 5 and 7).
    - Click **Compare**.
    - View comparison of metrics like **precision**, **recall**, **F1**, etc., in:
      - **Tabular format**.
      - **Charts and visualizations**.
- **Tracked Elements**:
  - **Model parameters** (hyperparameters).
  - **Metrics** (accuracy, precision, recall, F1, etc.).
  - **Artifacts** (model files, environment files).
- **Model Registry**:
  - Export and register models in **Model Registry**.
  - Maintain versions, e.g., **model V1**, **model V2**.
  - Deploy those registered models to **production** easily.
- **Benefits**:
  - Makes **experiment tracking efficient and better**.
  - Improves **reproducibility**.
  - Enables **deployment** workflows.
  - Supports **model management** lifecycle.

---

## 4. Installing MLflow Locally

### 4.1 Installation Steps

1. Open **Git Bash** or a command prompt.
2. Run:
   ```bash
   pip install mlflow
   ```
3. After installation, launch the UI:
   ```bash
   mlflow ui
   ```
4. This starts MLflow UI on:
   - `http://localhost:5000`

### 4.2 Accessing the UI

- Open a browser and navigate to:
  - `http://localhost:5000`
- The UI shows:
  - **Experiments** section.
  - **Models** section (if any are registered).
- If there are existing models (from previous use), they can be **ignored** for the tutorial.

### 4.3 Documentation

- In the MLflow UI, click on **Docs**.
- You will find:
  - **Detailed documentation**.
  - **Getting Started** guide.
  - **Installation instructions**.
  - Alternative ways to **launch MLflow server**, for example:
    - Using specific `mlflow server` commands with options (described in docs).
  - **Screenshots** and reference examples.
- The documentation is **very well done** by the MLflow team and is recommended for deeper reading.

---

## 5. Basic Experiment Tracking with MLflow (Local)

### 5.1 Example Notebook Setup

- A **sample notebook** is used to demonstrate experiment tracking.
- The notebook:
  - Performs **classification** on a **synthetic dataset**.
  - The dataset is **imbalanced**:
    - Class `0`: **900 samples**.
    - Class `1`: **100 samples**.
  - The use case is similar to **anomaly detection**, **fraud detection**, etc.

- A **basic logistic regression model** is trained:
  - With certain hyperparameters (e.g., `C`, etc.).
  - A **classification report** is generated using:
    ```python
    classification_report(y_true, y_pred, output_dict=True)
    ```
  - `output_dict=True` returns the report as a **dictionary**.

- This **report dictionary** will be used to **log metrics into MLflow**.

### 5.2 Connecting the Notebook to MLflow

1. **Import MLflow**:
   ```python
   import mlflow
   ```
   (If not installed, use `pip install mlflow` first.)

2. **Set the experiment name**:
   ```python
   mlflow.set_experiment("first_experiment")
   ```

3. **Set tracking URI**:
   - Use the same URI where `mlflow ui` is running.
   - Example:
     ```python
     mlflow.set_tracking_uri("http://127.0.0.1:5000")
     ```
   - This URI corresponds to what was shown when `mlflow ui` was started (local MLflow instance).

4. **Start a run and log data**:
   ```python
   with mlflow.start_run():
       # After training the model and computing report dict
       mlflow.log_params(params_dict)
       mlflow.log_metrics(metrics_dict)
       mlflow.sklearn.log_model(model, artifact_path="logistic_regression")
   ```

### 5.3 Logging Parameters

- **Parameters** are typically:
  - Hyperparameters of the model, e.g., for logistic regression:
    - `C`, `max_iter`, `solver`, etc.
- Can be logged:
  - Individually with `mlflow.log_param("param_name", value)`, or
  - As a dictionary with `mlflow.log_params(params_dict)`.
- In the example, all Logistic Regression parameters are logged at once using a dictionary.

### 5.4 Logging Metrics

- Metrics are derived from the **classification report dictionary**:
  - For example, `report_dict["accuracy"]`, `report_dict["0"]["recall"]`, `report_dict["1"]["recall"]`, etc.
- Metrics logged (as a dictionary) include:
  - `accuracy`
  - `recall` for **class 0**
  - `recall` for **class 1** (especially important in anomaly/fraud detection).
  - **F1 score** using **macro average**:
    - Could also use **weighted average**, but macro average is used here.
- Usage:
  ```python
  mlflow.log_metrics({
      "accuracy": report_dict["accuracy"],
      "recall_class_0": report_dict["0"]["recall"],
      "recall_class_1": report_dict["1"]["recall"],
      "f1_macro": report_dict["macro avg"]["f1-score"]
  })
  ```
- Alternatively, each metric can be logged individually using `mlflow.log_metric(name, value)`. Both approaches are equivalent in effect.

### 5.5 Logging Models (Artifacts)

- Models are logged as artifacts using:
  ```python
  mlflow.sklearn.log_model(model, artifact_path="logistic_regression")
  ```
  - If using **XGBoost**, you would use `mlflow.xgboost.log_model`.
  - Different frameworks have appropriate logging functions (`mlflow.sklearn`, `mlflow.xgboost`, etc.).
- The arguments:
  - First argument: the actual **model object**.
  - Second argument: the **artifact path** (a name such as `"logistic_regression"`).

### 5.6 Handling Run ID Errors

- Sometimes, on first attempt, MLflow may show an error such as:
  - “Experiment ID XYZ doesn’t exist.”
- In such cases:
  - **Rerun** the cell / experiment code.
  - Usually, this resolves the issue.

### 5.7 Inspecting Results in MLflow UI

- After running the notebook:
  - Refresh the MLflow UI page.
  - You should see:
    - A new **experiment**: e.g., `first_experiment`.
  - MLflow automatically generates a **run name** if not given explicitly.
- Inside a run:
  - You will see:
    - **Parameters** tab:
      - Hyperparameters passed to logistic regression.
    - **Metrics** tab:
      - Logged metrics such as accuracy, precision, recall, F1, etc.
      - Option to see them also in **chart format**.
    - **Artifacts** tab:
      - Contains the model artifact (e.g., `logistic_regression` folder).
      - Inside, you might see:
        - `model.pkl` or similar model binary (e.g., `model.pickle`).
        - `MLmodel` file (MLflow metadata).
        - `conda.yaml` (conda environment description).
        - `requirements.txt` (Python dependencies).
        - `python_env.yaml` or similar environment files (depending on MLflow version/config).

### 5.8 Using Artifacts for Deployment

- Artifacts such as model files (`model.pkl`) and environment files (`requirements.txt`, `conda.yaml`) can be:
  - **Downloaded** from the UI.
  - Packaged into a **Docker container**.
  - Deployed to a **cloud environment** (AWS, Databricks, etc.).
- `requirements.txt`:
  - Lists all **Python libraries** used by the model.
- `conda.yaml`:
  - Similar to `requirements.txt`, but for **conda environments**.
- These files ensure you can deploy the model as an **atomic unit** with a known environment.

---

## 6. Running Multiple Experiments in a Loop

### 6.1 Setup with Multiple Models

- Another notebook demonstrates running **four different experiments** on the same synthetic imbalanced dataset:
  - Dataset:
    - Class 0: **900 samples**.
    - Class 1: **100 samples**.
  - Use case: anomaly detection or fraud detection.
- Four models:
  1. **Logistic Regression**:
     - Good metrics on **class 0**.
     - Poor performance on **class 1**.
  2. **Random Forest**:
     - Improves performance on **class 1**.
     - Recall for class 1 is still relatively low.
  3. **XGBoost (XGBClassifier)**:
     - Improves performance further.
     - Recall for class 1 reaches about **80%**.
  4. **XGBoost with SMOTETomek (SMOTE + Tomek links)**:
     - **SMOTETomek** is a technique for **handling class imbalance**:
       - **Oversampling** minority class (SMOTE).
       - **Undersampling / cleaning** using Tomek links.
     - This produces a rebalanced dataset.
     - XGBoost trained on this data:
       - Recall for class 1 **improves slightly** further.
       - **Precision** goes **down** somewhat.

### 6.2 Looping Through Models

- The notebook organizes models in an **array/list**:
  - Each element can be a **tuple** like:
    - `(model_name, model_object)`.
- Example pseudo-structure:
  ```python
  models = [
      ("Logistic Regression", logistic_regression_model),
      ("Random Forest", random_forest_model),
      ("XGB Classifier", xgb_model),
      ("XGB Classifier with SMOTETomek", xgb_smot_model)
  ]
  ```
- All models are trained and classification reports are stored in a list:
  - `reports = [report1, report2, report3, report4]`
  - Each `report` is the dictionary produced by `classification_report(..., output_dict=True)`.

### 6.3 Using `enumerate` in the Loop

- The code uses:
  ```python
  for i, element in enumerate(models):
      # i: index (0,1,2,3,...)
      # element: ("model_name", model_object)
  ```
- `print(i)` would show:
  - `0, 1, 2, 3, ...`
- `print(element)` would show:
  - Each tuple (`(model_name, model)`).
- `reports[i]` gives the corresponding classification report for that model.

### 6.4 Logging Runs in a Loop with MLflow

1. **Import MLflow and set experiment**:
   ```python
   import mlflow
   mlflow.set_experiment("anomal_detection")  # experiment name (typo kept as used: "anomal detection")
   mlflow.set_tracking_uri("http://127.0.0.1:5000")
   ```

2. **Inside loop**:
   ```python
   for i, element in enumerate(models):
       model_name = element[0]
       model = element[1]
       report = reports[i]

       with mlflow.start_run(run_name=model_name):
           # Log params
           mlflow.log_params({"model_name": model_name})
           # Or more detailed params as needed

           # Log metrics (individually or via dict)
           mlflow.log_metric("accuracy", report["accuracy"])
           mlflow.log_metric("recall_class_1", report["1"]["recall"])
           mlflow.log_metric("recall_class_0", report["0"]["recall"])
           mlflow.log_metric("f1_macro", report["macro avg"]["f1-score"])

           # Log model depending on algorithm
           if "xgb" in model_name.lower():
               mlflow.xgboost.log_model(model, artifact_path="xgb_model")
           else:
               mlflow.sklearn.log_model(model, artifact_path="sklearn_model")
   ```

3. **Notes**:
   - `run_name` is set to `model_name`, so runs are easily identifiable in the UI.
   - You can expand `log_params` to log all hyperparameters for each model.

### 6.5 Viewing and Comparing Runs in MLflow UI

- After running the code:
  - Refresh the MLflow UI.
  - You should see a new experiment: e.g., `anomal_detection`.
  - It will list **4 runs**, one for each model:
    - Logistic Regression.
    - Random Forest.
    - XGB Classifier.
    - XGB Classifier with SMOTETomek.

- In each run:
  - **Parameters**:
    - Shows `model_name`, and potentially other hyperparameters if logged.
  - **Metrics**:
    - accuracy, recall_class_0, recall_class_1, f1_macro, etc.
  - **Artifacts**:
    - Model binaries, environment files, etc.

- **Comparing runs**:
  1. Select multiple runs using checkboxes.
  2. Click **Compare**.
  3. Use the comparison view to:
     - Plot and compare metrics, such as:
       - Recall for class 1 (most relevant for anomaly detection).
       - Recall for class 0.
       - F1 scores.
     - Observe trends, e.g.:
       - Logistic Regression:
         - Recall for class 1 ~ 0.5
         - Recall for class 0 ~ 0.96
         - F1 score ~ 0.74
       - Random Forest improves recall for class 1 compared to Logistic Regression.
       - XGB and XGB with SMOTETomek further change metrics, with trade-offs between recall and precision.

- The comparison UI includes:
  - **Charts**: you can pick which metric to plot (e.g., `recall_class_1`).
  - **Table view**:
    - Shows metrics and system info in rows and columns.
    - Includes **runtime**:
      - E.g., logistic regression might take the **maximum training time** among compared models (as mentioned).
  - **Scatter plots**:
    - E.g., F1 score vs recall for class 1.
    - Models in the **top-right quadrant** (high F1 and high recall) can be considered the best.
    - Example:
      - XGB classifier and XGB classifier with SMOTETomek might appear in the top-right quadrant.
      - If recall for class 1 is the primary metric, SMOTETomek model may be selected despite a small drop in precision.

- **Filtering**:
  - MLflow allows filters like:
    ```text
    metrics.rmse < 1
    params.model = 'tree'
    ```
  - In the tutorial context:
    - They mention filters like `metrics.rms < 1`, `params.model = 3`, etc., as examples.
  - Filters help narrow down runs meeting specific criteria.

- **New UI Features** (mentioned):
  - **Evolution** and **Traces** tabs:
    - These are newer UI features.
    - The instructor notes he does not yet have content to show under these, but they are present for more advanced use.
  - The **Table** view is highlighted as the **most important visual** for comparing experiments.

---

## 7. Model Registry and Model Registration

### 7.1 Logging Parameters Properly Before Registration

- The instructor modifies the notebook to include **detailed parameters** in the `models` array.
- Each element in the models array may now include:
  - Model name.
  - Model object.
  - Associated **parameters**.
- In the loop, he:
  - Sets those parameters on the model.
  - Logs the parameters using:
    ```python
    mlflow.log_params(params)
    ```
- He then:
  - Goes to MLflow UI.
  - Deletes previous `anomal_detection` experiments (to start fresh):
    - Click on the **delete icon** next to experiment(s).
- Then reruns the notebook start-to-finish:
  - Recreates the `anomal_detection` experiment.
  - Logs all metrics and parameters **fresh**.

### 7.2 Deciding Which Model to Register

- Examining the experiment in the MLflow UI:
  - He focuses on **recall for class 1** because:
    - It is crucial in **anomaly detection** and **fraud detection**.
  - He identifies that recall for class 1 is **maximum** for:
    - The **XGBoost model with SMOTETomek** (XGB + SMOTETomek).
  - Specifically:
    - Recall for class 1 is around **0.833** (i.e., **83.3%**).
  - Therefore, he decides to **register this model** in the **Model Registry**.

### 7.3 Ways to Register a Model

- In the documentation:
  - You can register a model **directly within `log_model`** during the run.
  - But in this tutorial:
    - The instructor wants to **finish all experiments first**, then **pick a single best run** and register that model **afterwards**.
  - For this, a separate **MLflow API** is used: `mlflow.register_model`.

### 7.4 Using `mlflow.register_model`

- API usage:
  ```python
  from mlflow import register_model  # or mlflow.register_model

  mlflow.register_model(
      model_uri="runs:/<run_id>/model",  # path to the model artifact within the run
      name="xgb_sm"                      # name of the registered model
  )
  ```
- Parameters:
  - `model_uri`:
    - Format: `"runs:/<run_id>/<artifact_path>"`
    - `<run_id>` is the **unique MLflow run ID**.
    - `<artifact_path>` is where the model was logged (e.g., `"model"`, `"xgb_model"`, etc.).
  - `name`:
    - A unique name for the model in the **Model Registry**, e.g., `"xgb_sm"`.

- **Getting the Run ID**:
  - Open the MLflow UI.
  - Click on the run of interest (the one with best recall_class_1).
  - Locate the **Run ID** (a long unique identifier).
  - In the notebook:
    ```python
    run_id = input("Enter run ID: ")
    ```
    - Paste the run ID in when prompted.
  - Use this run ID to construct `model_uri`.

- Example in the tutorial:
  - The instructor uses:
    - Model name: `xgb_sm`.
    - Model URI: something like `runs:/<run_id>/model` (adjusted to match the artifact path used in his logging).

### 7.5 Viewing the Registered Model

- After running `register_model`:
  - Go to the **Models** tab in MLflow UI.
  - You will see a model named `xgb_sm`:
    - **Version 1** is created by default.
- Inside the registered model page:
  - You see:
    - Model name: `xgb_sm`.
    - Version number(s).
    - Associated details and run(s).
  - You can add:
    - **Description**:
      - E.g., “This model was trained on oversampled dataset using SMOTETomek; classifier is XGBoost; anomaly detection use case”, etc.
    - **Tags**:
      - Arbitrary useful metadata.
    - **Aliases**:
      - E.g., `Challenger` (commonly used in production workflows):
        - **Champion**: current **production-deployed** model.
        - **Challenger**: new candidate that may replace the champion.

- Example alias:
  - The instructor sets alias:
    - `Challenger` for Version 1 of `xgb_sm`.

### 7.6 Multiple Versions in Model Registry

- If you run the registration code **again** (for the same or another run):
  - The registry will create a **new version**, e.g.:
    - `xgb_sm` **Version 2**.
- Aliases:
  - Initially, `Challenger` may point to **Version 1**.
  - You can update alias assignments:
    - Reassign `Challenger` to **Version 2**.
    - This way alias `Challenger` always points to the **latest** challenger.
- The tutorial:
  - Demonstrates that multiple versions appear:
    - Version 1, Version 2, etc.
  - Then:
    - The instructor decides to **delete** these extra versions.
    - Re-run everything with just **Version 1** for simplicity.
    - The goal is to illustrate **versioning** concept, not to keep multiple versions at that point.

---

## 8. Loading Models from Model Registry for Local Testing

### 8.1 Loading by Version Number

- To **load a registered model**, use framework-specific load APIs, e.g. for XGBoost:
  ```python
  import mlflow.xgboost

  model_uri = "models:/xgb_sm/1"  # "models:/<model_name>/<version_number>"
  loaded_model = mlflow.xgboost.load_model(model_uri)
  y_pred = loaded_model.predict(X_test)
  print(y_pred[:n])  # print first few predictions
  ```
- Steps:
  1. Set `model_uri` to `"models:/<model_name>/<version>"`, e.g. `"models:/xgb_sm/1"`.
  2. Use `mlflow.xgboost.load_model(model_uri)` (or `mlflow.sklearn.load_model` depending on library).
  3. Use `.predict(X_test)` to generate predictions.

### 8.2 Debugging Path Issues

- The instructor encountered issues where:
  - Using `model_name` alone in `model_uri` caused errors due to path confusion.
- Resolution:
  - Use a **fixed string** pattern:
    ```python
    model_uri = "models:/model/1"  # Example; adjust to real name such as "xgb_sm"
    ```
    Or specifically:
    ```python
    model_uri = "models:/xgb_sm/1"
    ```
  - Ensure that the format matches MLflow’s requirement: `models:/<name>/<version_or_stage>`.

- The instructor mentions:
  - He debugged offline and found that a **previous approach using `model_name` variable** directly in the URI caused issues.
  - The correct, stable approach:
    - Use a **fixed string** in the example to ensure correctness.
  - The notebook provided for download has the **correct URI string format**.

### 8.3 Loading by Alias (e.g., Challenger)

- Instead of specifying a version number, you can load by **alias**:
  ```python
  model_uri = "models:/xgb_sm@Challenger"
  loaded_model = mlflow.xgboost.load_model(model_uri)
  y_pred = loaded_model.predict(X_test)
  ```
- Explanation:
  - `@Challenger` refers to the **alias** attached to one specific version of the model.
  - You **do not** need to remember or specify the exact version number.
  - Changing alias assignment in the registry allows seamless switching of actual underlying version.

- The instructor:
  - Demonstrates loading the `xgb_sm` model with `Challenger` alias.
  - Runs predictions to verify functionality.

---

## 9. Transitioning from Development to Production Using MLflow Client

### 9.1 Using MLflow Client for Model Movement

- You can use `mlflow.client.MlflowClient` to:
  - **Copy models** between different names or stages.
  - Implement multi-stage deployment processes (e.g., dev → prod).
- Example pattern:
  ```python
  from mlflow.tracking import MlflowClient

  client = MlflowClient()
  client.copy_model_version(
      src_model_uri="models:/xgb_sm@Challenger",  # dev model
      dst_model_name="anomaly_data"               # production model registry name
  )
  ```
- In the tutorial:
  - The instructor uses:
    - `dev_model_uri` like `"models:/xgb_sm@Challenger"` (development/Challenger).
    - `prod_model` name such as `"anomaly_data"` (or similar, exact spelling may vary but the idea is: prod model name).

- After copying:
  - A new entry appears in the **Model Registry** with the `prod` model name (e.g., `anomaly_data`):
    - This is treated as a **production** model.
  - You can set an alias such as:
    - `Champion` for the production model version.

### 9.2 Setting Champion Alias for Production Model

- In the MLflow UI:
  - Go to the **production model** entry (e.g. `anomaly_data`).
  - Assign alias:
    - `Champion` to its active version.
- Accordingly:
  - The dev model (e.g. `xgb_sm`) might hold alias `Challenger`.
  - The prod model (e.g. `anomaly_data`) holds alias `Champion`.

### 9.3 Downloading and Using the Production Model

- To load and test the production model locally:
  ```python
  import mlflow.xgboost

  model_uri = "models:/prod_model@Champion"  # Example: "models:/anomaly_data@Champion"
  loaded_prod_model = mlflow.xgboost.load_model(model_uri)
  y_pred = loaded_prod_model.predict(X_test)
  ```
- In the tutorial:
  - The instructor:
    - Copies the production model URI structure into his code.
    - Uses the appropriate registry name (e.g., `prod_model`) and alias `Champion`.
    - Executes the notebook cell to:
      - Download the model artifact from the registry.
      - Perform predictions (`predict` on test data).
- This confirms:
  - The model registry works for **Dev → Prod** transitions.
  - Models can be:
    - **Downloaded**.
    - **Packaged in Docker**.
    - **Deployed** to various platforms (Databricks, AWS, etc.).

### 9.4 CI/CD Integration

- MLflow workflows (experiment tracking, model registration, alias changes, copying between registries) can be:
  - Integrated with **Jenkins** or similar **CI/CD tools**.
  - Controlled via:
    - **Jenkinsfile** pipelines.
    - Automated scripts (e.g., automatically tagging a new model as `Champion` if metrics exceed threshold).
- Cloud Provider Support:
  - Many cloud platforms provide **native integration** or easy patterns to:
    - Deploy MLflow models.
    - Manage MLflow model registries.
  - Documentation includes examples for:
    - **Databricks**.
    - **AWS** and other providers.

---

## 10. DagsHub Integration for Centralized Experiment Tracking

### 10.1 Motivation

- So far:
  - MLflow server has been run **locally** (on `localhost:5000`).
- Problem:
  - What if **2–3 data scientists** in the **same team** want to:
    - **Publish experiment results** to a **centralized cloud-based server**?
  - They need:
    - A **shared MLflow server** in the cloud.
- **DagsHub**:
  - A platform that helps with:
    - **Centralized experiment tracking**.
    - **Versioning code and data**.
    - **Annotating data**.
    - **Generating training datasets**.
    - Integrating with **MLflow** for experiment tracking.

### 10.2 Creating a GitHub Repository

1. Create a new **GitHub repository** for the notebook.
2. Choose:
   - `.gitignore` template: e.g., **Python**.
3. After creating:
   - Clone the repository locally:
     ```bash
     git clone <repository_url>
     ```
4. Copy the **MLflow Model Management notebook** (from previous sections) into this repository folder.
5. Use Git to add and commit:
   ```bash
   cd <repo_folder>
   git status  # see the new notebook file
   git add <notebook_file>
   git commit -m "mlflow dagshub notebook"
   git push
   ```
6. Verify on GitHub:
   - Refresh repository page.
   - Confirm the notebook is visible in the main branch.

### 10.3 Creating and Connecting a DagsHub Account

1. Go to **DagsHub** website.
2. Create a **free account**:
   - You can sign up using:
     - Google account.
     - GitHub account.
   - The instructor uses **Google**.
   - There may be a brief issue with captcha (“I’m not a robot”), but ultimately the account is set up.
3. Fill in basic profile details:
   - Organization type: e.g., **Personal**.
   - Team type: e.g., **Just me**.
   - Data type interest: e.g., **Tabular and text data**.
4. DagsHub capabilities:
   - Like GitHub, it can:
     - Version **code** (like GitHub).
     - Additionally, it can version **data** (datasets).
     - Perform **data annotation**.
     - Generate **training datasets**.
     - Track **experiments**.
   - In this tutorial:
     - The focus is on **track experiments**.

5. The UI of DagsHub:
   - Very similar to GitHub:
     - Has **repositories**, **pull requests**, etc.
   - Can be used as a **Git hosting platform** in its own right.

### 10.4 Connecting a GitHub Repo to DagsHub

1. In DagsHub:
   - Click **Create new repository**.
2. Option 1:
   - Create a repository directly in DagsHub, then push code there (similar to GitHub).
3. Option 2 (used in tutorial):
   - **Connect an existing GitHub repository**:
     - Click “Connect with GitHub”.
     - Authorize DagsHub to access GitHub repositories (if prompted).
4. After authorization:
   - Search for the specific repository, e.g., `mlflow_dagshub_demo` (or the actual name used).
   - Select it and click to **connect**.
5. Now:
   - DagsHub has a **copy** (mirror) of your GitHub repo, synchronized:
     - The UI shows the same notebook file.
     - Repository pages look very similar to GitHub.

---

## 11. Configuring the Notebook to Use DagsHub as MLflow Server

### 11.1 DagsHub Experiment Tracking Setup

- In DagsHub, navigate to **Remote → Experiments**.
- DagsHub shows code snippets to set up MLflow tracking with DagsHub:
  - Example:
    ```python
    import dagshub
    dagshub.init(repo_owner="your_username", repo_name="your_repo", mlflow=True)
    ```
  - DagsHub provides:
    - `repo_owner`
    - `repo_name`
    - And sets up MLflow tracking URI automatically.

### 11.2 Installing DagsHub Python Package

- On local machine:
  ```bash
  pip install dagshub
  ```
- Ensure this is done before importing in the notebook.

### 11.3 Modifying the Notebook

1. Open Jupyter Notebook pointing to the local repository:
   - Navigate to directory containing `mlflow_dagshub_demo` (or equivalent).
2. Open the MLflow notebook.
3. Run initial cells (imports, dataset creation, model definitions, etc.).
   - The instructor fixed a small bug:
     - A variable `smt` vs `r_s` (e.g., `R` vs `RS`) mismatch.
     - Ensure proper variable names are used; e.g.: `r_s` for random state or similar.
4. Add a new cell for **DagsHub setup**:
   ```python
   import dagshub

   dagshub.init(repo_owner="your_dagshub_username",
                repo_name="mlflow_dagshub_demo",
                mlflow=True)
   ```
   - `mlflow=True` ensures that:
     - MLflow tracking is configured to point to the DagsHub-hosted MLflow server.
5. Previously, the notebook had:
   ```python
   mlflow.set_tracking_uri("http://127.0.0.1:5000")
   ```
   - **Comment out** or remove this local URI line:
     - Because now you want to track to the **DagsHub cloud** server, not localhost.

6. Replace `set_tracking_uri` with:
   - The MLflow tracking URI from DagsHub:
     - Usually provided in the DagsHub UI (e.g., a URL like `https://dagshub.com/<user>/<repo>.mlflow`).
   - You can copy this tracking URI and paste into your code if needed:
     ```python
     mlflow.set_tracking_uri("https://dagshub.com/<user>/<repo>.mlflow")
     ```
   - But if using `dagshub.init(..., mlflow=True)`, it can also **automatically** configure the tracking URI.

### 11.4 Handling Authentication and Environment Variables

- The instructor initially encountered an error:
  - Something like:
    - “API request to endpoint failed with error …” (due to mismatched credentials or stale configuration).
  - This happened because:
    - He was previously connected to a **different DagsHub account**, and some old settings remained cached.

- To fix such issues:
  - **Set environment variables** manually in the notebook:
    ```python
    import os

    os.environ["MLFLOW_TRACKING_USERNAME"] = "<your_dagshub_username>"
    os.environ["MLFLOW_TRACKING_PASSWORD"] = "<your_token_or_password>"
    os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/<user>/<repo>.mlflow"
    ```
  - Where:
    - `MLFLOW_TRACKING_USERNAME`:
      - Your DagsHub **username** (e.g., `learnpython_language` in the example).
    - `MLFLOW_TRACKING_PASSWORD`:
      - A **personal access token** from DagsHub (not your plain account password).
      - Obtain it by:
        - Going to **Public Keys / Tokens** page in DagsHub settings.
        - Clicking **View** and **copying the token**.
    - `MLFLOW_TRACKING_URI`:
      - The MLflow endpoint for your DagsHub repo:
        - E.g., `https://dagshub.com/<user>/<repo>.mlflow`.

- After setting these environment variables:
  - Run the cell to confirm they are in effect.
  - Rerun experiment logging cells.
  - The experiments should now publish to the **DagsHub MLflow server** without errors.

### 11.5 Publishing Metrics to DagsHub

- After configuration:
  - Rerun the cells that:
    - Train models.
    - Start MLflow runs.
    - Log parameters, metrics, and models.
- DagsHub will now:
  - Receive these metrics and artifacts.
  - Serve them through its hosted MLflow UI.

- On DagsHub:
  - Click **Go to MLflow UI** (from the repository page).
  - Confirm that:
    - Your experiment (e.g., `anomal_detection`) is visible.
    - All runs and metrics appear as expected.
  - This MLflow UI is now hosted at a URL like:
    - `https://dagshub.com/<user>/<repo>.mlflow` (not localhost).

---

## 12. Using DagsHub MLflow UI

### 12.1 Viewing Experiments

- You will see:
  - Experiments created from your notebook, e.g., `anomal_detection`.
  - Each run:
    - Has parameters, metrics, artifacts, etc.
- Functionality is **the same** as your local MLflow UI:
  - Compare experiments.
  - View charts.
  - Download artifacts.

### 12.2 Model Registration on DagsHub

- You can:
  - **Register models** in the **Models** section of DagsHub’s MLflow UI, just like before.
  - Either:
    - Do it via code:
      - Using `mlflow.register_model(...)` with a correct `model_uri`.
    - Or do it **manually** via the UI:
      - Click **Create Model**.
      - Provide a model name (e.g., `"XGBoost Anomaly Detection"`).
      - Then associate specific runs with this model to create versions.

- Example workflow:
  1. Click on **Models**.
  2. Click **Create model**.
  3. Name it something like:
     - `"XGBoost_Anomaly_Detection"` (or more generic: `"Anomaly_Detection_Dev_Candidate"`).
  4. Once created:
     - Go back to **Experiments**.
     - Select a run.
     - Register this run under the created model.
  5. The registered model now appears with:
     - **Version 1** in the Models tab.
  6. Later, if another better model is found (e.g., Random Forest becomes better in some metric):
     - Register its run under the **same model name**.
     - This produces **Version 2** of the model.

- Note:
  - The instructor mentions:
    - Instead of naming model specifically "XGBoost", a more generic name like **"Anomaly detection Dev candidate"** or **"Dev candidate"** might make more sense.
    - This helps when different algorithms (RandomForest, XGBoost, etc.) are used, but all represent the same high-level artifact (an anomaly detection model).

### 12.3 Centralized Collaboration

- With DagsHub as a central MLflow server:
  - Multiple data scientists on the team can:
    - Use the **same tracking URI and credentials**.
    - Publish their experiment results to the same **central repository**.
  - This allows:
    - Shared visibility over experiments.
    - Easy comparison of results across team members.
  - Team-specific credentials will be set so that:
    - Everyone uses the same environment variables (username/token/URI).

---

## 13. Summary of Entire Tutorial Flow

1. **Motivation**:
   - Local notebooks, multiple models and datasets, leading to confusion and inefficiency.
   - Manual logging in Excel/Google Sheets is:
     - Error-prone.
     - Inconvenient for deployment.

2. **MLflow Overview**:
   - Tool for:
     - **Experiment tracking**.
     - **Model management**.
     - **Reproducibility**.
     - **Deployment**.
   - Provides UI for:
     - Viewing experiments.
     - Viewing parameters, metrics, and artifacts.
     - Comparing runs.
     - Managing model registry.

3. **Installation and Local Usage**:
   - Install via `pip install mlflow`.
   - Run `mlflow ui` at `localhost:5000`.
   - Use:
     - `mlflow.set_experiment`.
     - `mlflow.set_tracking_uri`.
     - `mlflow.start_run`.
     - `mlflow.log_params`, `mlflow.log_metrics`, and framework-specific `log_model`.

4. **Experiment Tracking Example**:
   - Synthetic imbalanced dataset (900 vs 100 samples).
   - Logistic Regression:
     - Log hyperparameters and metrics (accuracy, precision, recall, F1).
   - Evaluate results via MLflow UI.

5. **Multiple Experiments in a Loop**:
   - Compare:
     - Logistic Regression.
     - Random Forest.
     - XGBoost.
     - XGBoost with SMOTETomek (class imbalance handling).
   - Metrics:
     - Accuracy.
     - Recall for class 0 and 1.
     - F1 macro.
   - Use loop with `enumerate`.
   - Log each model with identifiable `run_name`.

6. **Comparison and Model Selection**:
   - Use MLflow **Compare** view to:
     - Focus on **recall for class 1**, as it’s crucial in anomaly/fraud detection.
   - See trade-offs:
     - SMOTETomek increases recall for class 1 but lowers precision.
   - Use charts, table view, and scatter plots to choose best model.

7. **Model Registry**:
   - Register the best-performing model (XGB + SMOTETomek).
   - Use `mlflow.register_model` with `runs:/<run_id>/model` URI.
   - Manage:
     - Versions (V1, V2, etc.).
     - Aliases (e.g., `Challenger`, `Champion`).
     - Descriptions and tags.

8. **Loading and Testing Registered Models**:
   - Load by version:
     - `models:/xgb_sm/1`.
   - Load by alias:
     - `models:/xgb_sm@Challenger`.
   - Use `mlflow.xgboost.load_model` (or equivalent for other frameworks).
   - Run `predict` and validate output.

9. **Transition from Dev to Prod**:
   - Use `MlflowClient` to:
     - Copy dev model version (e.g., `Challenger`) to a production registry name.
   - Assign alias:
     - `Champion` for the production model.
   - Download and test:
     - `models:/prod_model@Champion` (for predictions).
   - Potential integration with CI/CD tools:
     - Jenkins and pipelines for automation.

10. **DagsHub Integration**:
    - Use DagsHub as a **central MLflow server**.
    - Steps:
      - Create GitHub repo and push notebook.
      - Create and configure DagsHub account.
      - Connect GitHub repo to DagsHub.
      - Install `dagshub` Python package.
      - Use `dagshub.init(...)` with `mlflow=True`.
      - Set environment variables:
        - `MLFLOW_TRACKING_USERNAME`.
        - `MLFLOW_TRACKING_PASSWORD` (DagsHub token).
        - `MLFLOW_TRACKING_URI`.
      - Rerun experiments to log to DagsHub MLflow.
    - On DagsHub:
      - View experiments and registered models.
      - Register new model versions.
      - Manage Dev/Prod workflows similarly to local MLflow.

11. **Course Reference and Scope Note**

    - The tutorial is based on the **MLOps chapter** of the instructor’s **Machine Learning course**.
    - The course covers:
      - **Python basics**.
      - **Data visualization**.
      - **Math and statistics basics**.
      - **Supervised and unsupervised learning**.
      - Two **end-to-end projects**:
        - Cover full ML project lifecycle:
          - Data cleaning.
          - Feature engineering.
          - Hyperparameter tuning.
          - Building **Streamlit apps**.
          - Presenting results back to business.
      - Designed with:
        - **Very simple explanations** (even a high school student can follow).
        - Many **quizzes** and **exercises**.
    - The instructor notes:
      - MLflow documentation is extensive and very good.
      - He only provides an **overview** in this tutorial.
      - A full detailed walkthrough would be extremely long (approx. 20 hours).
    - The code used in the tutorial:
      - Is available in the **video description**.
      - Includes the notebooks for MLflow, Model Registry, and DagsHub.

12. **Final Remarks**

- You should now have a **good understanding** of:
  - **Experiment tracking** in MLflow.
  - **Model Management** using MLflow’s **Model Registry**.
  - Running MLflow **locally** and on **DagsHub** as a **centralized cloud server**.
- DagsHub is **free**, which makes it a practical choice for learning and experimenting with:
  - Centralized MLflow-based workflows.
- For deeper or production-grade deployments:
  - Refer to the **official MLflow documentation**.
  - Explore cloud-specific deployment patterns (Databricks, AWS, etc.).
- If you liked this tutorial and want to learn ML in depth:
  - The instructor recommends his **Machine Learning course** where this MLflow/MLOps chapter is part of a larger curriculum.
- The instructor concludes by:
  - Encouraging learners to share this tutorial with friends learning **MLOps**.