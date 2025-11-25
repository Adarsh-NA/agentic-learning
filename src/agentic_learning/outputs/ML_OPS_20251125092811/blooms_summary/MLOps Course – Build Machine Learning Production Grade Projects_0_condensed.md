# MLOps Course – Detailed Structured Summary (Markdown)

## 1. Course Overview and Instructor Background

- **MLOps definition**:  
  - MLOps = *Machine Learning Operations*  
  - Practice of applying **DevOps principles** to **machine learning**.
- **Course scope**:
  - End-to-end MLOps project from **data ingestion** to **deployment**.
  - Uses **state-of-the-art tools**:
    - **ZenML**
    - **MLflow**
    - Various ML libraries (e.g. scikit-learn, etc.).
- **What you will learn**:
  - Fundamentals of MLOps.
  - One **end-to-end project**:
    - Data ingestion
    - Data cleaning
    - Model training
    - Evaluation
    - Deployment
    - Monitoring
  - Use of tools like **MLflow**, **ZenML**, and others.
- **Why this course matters**:
  - MLOps is a **new field** with **few resources**.
  - Described as a **“gold mine”** and a **game-changer** for the ML community.
  - With **dedication and patience**, learners can:
    - Succeed in learning MLOps.
    - Become competitive for **international roles** and MLOps-related jobs.

- **Instructor background**:
  - Lead Data Scientist at a company (referred to as *ate* / *atate* in transcript).
  - Has led several products in the **creator’s economy**.
  - Has worked as an **MLOps engineer** with **ZenML**, one of the fastest-growing MLOps frameworks.
  - Previous Data Scientist at **Artifact**, building **large-scale NLP products** *before GPT was launched*.
  - Has created many popular ML courses on the channel.
  - Asserts that this experience makes him suitable to teach MLOps.
- **Resources**:
  - All required links and resources are available in the **YouTube description / repo**.

---

## 2. Introductory Lecture – Why MLOps?

### 2.1 Motivation: Data Growth and AI Importance

- **Exponential growth of data** and increasing importance of **Artificial Intelligence (AI)**.
- Need to:
  - Use data **properly** and **positively**.
  - Not just build prediction models but consider the **whole system**.

### 2.2 ML Code is Only 20% of the Project

- **Key claim**:
  - ML code / model is **only ~20%** of a real ML project or business problem.
- **Evidence / references**:
  - Validated by **Chip Huyen**, an expert in MLOps.
  - Also echoed by **Elon Musk**:
    - “Machine learning engineering is just 10% machine learning and 90% engineering.”
- **Problem with typical courses**:
  - Most online courses teach **only ML model building** (machine learning engineering).
  - They **ignore** the broader **engineering** side:
    - Not only DSA (Data Structures & Algorithms) or basic design patterns.
    - Includes **many more aspects** (pipelines, deployment, monitoring, etc.) that this course will cover in a project.

---

## 3. Typical ML Roles and Responsibilities in Industry

- **ML team composition**:
  - **Data Scientist**:
    - Discovers raw data.
    - Develops features.
    - Trains models.
  - **Data Engineer**:
    - *Productionizes* the data pipeline.
    - Handles where data comes from and scales it.
  - **ML Engineer**:
    - Deploys the model so that it can be used by users.
  - **Integration role**:
    - Integrates the deployed model/service into website or app.
    - Sets up **monitoring**.
  - **Lawyer / Legal**:
    - Answers: “Can I use this data for my model? Yes or No.”
- **Terminologies to be clarified in course**:
  - Training models
  - Productionizing
  - Deployment
  - Integrating
  - Monitoring
- Instructor’s goal in this introductory lecture:
  - Explain these terms so learners understand each piece used later in the project.

---

## 4. What Data Scientists Usually See vs. Reality

- **Typical beginner view of ML**:
  - Use `pandas.read_csv`, load data.
  - Fit a classifier: `clf.fit(X, y)`.
  - Predict and score: `clf.predict`, `clf.score`.
  - Assumption: a few lines of code is enough to get a job.
- **Reality**:
  - Writing a few lines of model code is **not enough** to get hired.
  - ~90% of focus in real production is on **engineering** concerns.
  - MLOps deals with this **“scary”** engineering reality.

---

## 5. ML in Production – Deployment and Continuous Loop

### 5.1 Basic Production Flow (Idealized)

- High-level simplified view:
  1. **Collect data**
  2. **Train model**
  3. **Deploy model** in production

### 5.2 What Deployment Means

- Example: **Email spam detection model**.
  - Model is trained on a local machine/server.
  - **Deployment** = making that model **available** to many Gmail users:
    - Integrate it into Gmail so it can classify spam for all users.
- Deployment = making a **local model available online** for the **actual users**.

### 5.3 Realistic Production Loop

- Actual cycle:
  1. Collect data
  2. Train model
  3. Deploy model (goes to production)
  4. **Changes happen**:
     - New data arrives.
     - Model is updated.
  5. Loop back:
     - Re-collect data.
     - Retrain.
     - Re-deploy.
- This repeats in a **never-ending loop** in production:
  - If model changes → retrain + redeploy.
  - If new data arrives → re-collect + retrain + redeploy.

### 5.4 Reasons for Returning to the Loop

- **1. Model changes (algorithm change)**:
  - Example: Change model from **Logistic Regression** to **Naive Bayes**.
  - Need to:
    - Retrain with new model.
    - Deploy updated version.

- **2. Data changes / new data**:
  - Example: **Spam detection**:
    - Spammers change strategy.
    - Patterns in emails differ from training data.
  - Need to:
    - Collect updated data.
    - Retrain to capture new patterns.
    - Redeploy.

- **3. Model performance decay (drift)**:
  - Example: **Fraud detection**:
    - Initially model works well.
    - Over time predictions degrade (incorrect predictions increase).
    - Fraudsters change strategies/patterns.
  - Response:
    - Re-collect more recent data.
    - Retrain.
    - Redeploy.
    - This may repeat after some time again.

- **4. Reformulate the problem**:
  - Possible reasons:
    - Difficult to gather the amount/quality of data needed.
    - Violation of assumptions made during training:
      - E.g., assumed input ranges, distributions, or availability.
      - If these assumptions change, need to:
        - Adjust assumptions.
        - Possibly redesign the model or problem setup.
    - Business objectives may change:
      - Might require **restarting** the ML process from scratch.

- **Continuous monitoring**:
  - Need ongoing model monitoring to:
    - Detect performance decay.
    - Detect assumption violations.
    - Detect data drift.
- **Overall**:
  - ML in production = **data affecting the output system** in real time.
  - Retraining and redeployment in a loop is **hard to make reliable**.

---

## 6. What is MLOps?

- **Definition**:
  - MLOps is a **set of practices** (not just a tool or library) that:
    - Aim to **deploy** and **maintain** ML models in **production**.
    - Ensure deployment is **reliable** and **efficient**.
- **Goals**:
  - Handle:
    - Data changes (trigger retraining).
    - Assumption changes (trigger redesign/adjustment).
    - Model monitoring, versioning, scaling.
- **Relation to DevOps**:
  - MLOps = **extension of DevOps methodology**:
    - Includes **ML and data science assets** as **first-class citizens** in the DevOps ecosystem.

### 6.1 City-Building Analogy

- **Analogy**:
  - Building a single **beautiful building** in a city vs. building the entire **functional city**:
    - Just a building:
      - Not useful alone.
      - Needs:
        - Electrical connectivity.
        - Maintenance.
        - Security systems.
        - Connectivity to roads and railways.
    - A full city:
      - Is like a complete ML system: model + infrastructure + monitoring + integration.
- **Mapping to ML**:
  - **Model alone** = beautiful building.
  - **MLOps** = building the **entire city** (infrastructure and operations):
    - Connections
    - Monitoring
    - Reliability
    - Maintenance
- **Job market implication**:
  - Companies want **full standalone “cities”**, not just isolated “buildings”.
  - Many people lack jobs because they focus only on model-building, not full-system MLOps.

---

## 7. Challenges After Deployment

Deployment is not the end; **trouble begins after deployment**.

### 7.1 Latency

- **Latency definition**:
  - Time taken for the system to respond to a request (e.g. page load, prediction).
- **Statistic**:
  - **53% of visitors abandon** a mobile site if it takes **more than 3 seconds** to load.
- **Implication**:
  - If you deploy a huge model (e.g. **120 billion parameters**), it may:
    - Not return predictions in <3 seconds.
    - Lead to user abandonment and low engagement.
  - Latency directly impacts:
    - User engagement.
    - Conversions.
    - Brand interaction.

### 7.2 Fairness and Bias

- **Microsoft Twitter bot example**:
  - Microsoft created a Twitter bot that learns from users.
  - It quickly became **racist** and supported:
    - Various **bad ideologies**.
  - It was taken down by Microsoft within **a few hours**.
  - It turned against various protected groups/ideologies (exact names not repeated in transcript).
- **Lesson**:
  - Must monitor **fairness** and avoid biased or harmful behavior.
  - Sometimes requires **retraining**, redesign, or shutdown.

### 7.3 Explainability and Auditability

- Hard to:
  - Explain **why** a model made a particular prediction.
  - Guarantee that its behavior is **authentic**, **trustworthy**, and **compliant**.
- **Regulatory angle**:
  - EU and other regions are introducing **rules and principles** for AI.
  - Systems need **explainability** and **auditability**.

### 7.4 Slow and Painful Deployment

- Survey of data scientists:
  - **36%** spend a **quarter of their time** deploying ML models.
  - Another **36%** spend **one-quarter to half** of their time.
  - **20%** spend **half to three-quarters** of their time.
  - **7%** spend **more than three-quarters** of their time on deployment.
- **Instructor’s experience**:
  - Built entire ML model + preprocessing in **2 days (4 hours/day)**.
  - Spent a **whole week** deploying the model.
  - Deployment is “**painfully slow**”.

---

## 8. Model-Centric vs Data-Centric AI

- **Model-Centric approach**:
  - **Fix the data**, keep the dataset constant.
  - Iteratively **improve the model** by:
    - Tuning hyperparameters.
    - Changing model architectures.
  - Expect better performance primarily by modifying **code/model**.
  - Most current work is in this approach.

- **Data-Centric approach**:
  - **Hold the model fixed** (or mostly fixed).
  - Iteratively **improve the data**:
    - Better labels.
    - More representative samples.
    - Cleaning noise.
  - Emphasis on **data quality** over model complexity.

- **Recommendation**:
  - Instructor, referencing **Andrew Ng**, recommends focusing more on **Data-Centric** approach.
  - This reflects what many data scientists observe in practice.

---

## 9. End-to-End ML/MLOps Process: Business to Monitoring

### 9.1 Start with the Business Problem

- Before any ML or MLOps:
  - Ask: **What is the business problem?**
  - Don’t jump directly to models; clarify **business objective**.

#### Example: Retail Sales Forecasting

- Problem:
  - Forecast retail sales.
  - Issues:
    - **Overstock**:
      - Too much inventory → wasted resources, unsold goods, losses.
    - **Understock**:
      - Insufficient stock → missed sales, unhappy customers, revenue loss.
- **Cost of wrong predictions**:
  - Both overstock and understock have **high cost**.
- **Goal**:
  - Improve forecasting to reduce:
    - Overstock.
    - Understock.

#### Decomposing the Sales Forecasting Process

- Break the process into components:
  1. **Data Gathering**:
     - Collect all required data.
  2. **Historical Sales Analysis**:
     - Analyze past sales.
  3. **Market Trend Analysis**:
     - Study current and emerging trends.
  4. **Actual Forecasting**:
     - Predict future sales numbers.

- **Where does ML help most?**
  - While all steps are important, **Actual Forecasting** is where ML can be applied to:
    - Analyze:
      - Past sales data.
      - Market trends.
    - Predict future sales **more accurately** than traditional methods.
- **ROI estimation**:
  - Estimate ROI based on:
    - Decrease in wasted resources (from overstock).
    - Decrease in missed opportunities (from understock).
  - Compare potential savings vs. cost to:
    - Develop.
    - Maintain the ML solution.
- **Prioritization**:
  - If ROI is high, prioritize building ML for **actual forecasting**.

### 9.2 Machine Learning Canvas – Structured Project Thinking

A structured approach to designing ML solutions:

1. **Value Proposition**:
   - Define:
     - The **problem**.
     - Its **importance**.
     - **Who** the end users are.
   - Example format:
     - For *target customer* who need *X*, our *product* is a *category* that *benefits Y*.
   - Ensure the **business importance** is high enough to justify ML investment.

2. **Data Sources**:
   - Identify **potential data sources**:
     - Internal databases.
     - APIs.
     - Open datasets.
   - Consider **hidden costs**:
     - Data storage.
     - Purchasing external data.
     - Data access costs.

3. **Prediction Task Specification**:
   - Define:
     - **Problem type**:
       - Supervised vs unsupervised.
       - Classification, regression, anomaly detection, ranking, etc.
     - **Inputs and outputs**:
       - What features?
       - What target?
     - **Model complexity**:
       - Simple baseline vs complex architectures.

4. **Feature Engineering**:
   - Interact with **domain experts**:
     - Example: Healthcare → need input from doctors.
   - Understand domain terminology.
   - Extract more meaningful features from raw data.

5. **Offline Evaluation**:
   - Set up **metrics** to evaluate the system before deployment.
   - Analyze **prediction errors**.
   - Understand **cost of wrong predictions** in business terms.

6. **Using Predictions in Decisions**:
   - Clarify:
     - How end users interact with predictions.
     - Whether:
       - There is **human-in-the-loop**.
       - Any **hidden costs** from human intervention.

7. **Data Collection for Retraining**:
   - Plan how to:
     - Continuously collect **new data**.
     - Retrain the model.
     - Prevent **model performance decay**.
   - Consider:
     - Cost of ongoing data collection.
     - Human labeling costs.
     - Frequency of retraining.
     - Tech stack changes.

8. **Monitoring and Metrics in Production**:
   - Define **metrics** for monitoring in production:
     - Example: For spam detection, track:
       - False positives/negatives.
       - Drift.
   - Identify scenarios where **AI/ML might not be the best solution**:
     - Some subtasks might be simpler without ML.
   - Remember:
     - Implementing ML solutions can be costly and complex.
     - Sometimes a simpler non-ML solution may suffice.

---

## 10. Three Core Artifacts and Engineering Phases

### 10.1 Three Main Artifacts

1. **Data**
2. **ML Model**
3. **Code**

### 10.2 Three Main Engineering Phases

1. **Data Engineering**:
   - Tasks:
     - Collect / acquire data.
     - Prepare data.
   - **Data engineering pipeline steps**:
     1. **Ingest data**.
     2. **Explore and validate** data:
        - Ensure data is correct and reliable.
     3. **Format and clean** data.
     4. **Label** data (if supervised learning).
     5. **Split** into:
        - Train.
        - Validation.
        - Test sets.

2. **Model Engineering**:
   - Core ML workflow:
     - Writing and executing ML algorithms.
   - **Model engineering pipeline steps**:
     1. Train model.
     2. Evaluate model.
     3. Validate (pre-deployment verification).
     4. Test model on unseen data.
     5. Package model (e.g. `.pkl`).

3. **Code / Serving / Ops Engineering**:
   - **Serving and operations pipeline steps**:
     1. Deploy model in production.
     2. Serve predictions.
     3. Monitor performance.
     4. Record and log predictions & metadata.

- These pipelines will be implemented in detail using **ZenML** in the course project.

---

## 11. ZenML: Pipelines and Steps

### 11.1 Why ZenML?

- **ZenML** is:
  - An **open-source library** for building full-stack MLOps applications.
  - Supports **pipeline-based** approach.
- Instructor’s experience:
  - Has worked at ZenML for **6–7 months** with the core team.
  - Finds it **super simple** and **one of the easiest/best** orchestrators.
- Alternatives:
  - Other orchestrators exist, but ZenML is chosen here for **simplicity**.

### 11.2 Key Concepts: Pipelines and Steps

- **Pipeline**:
  - High-level **workflow** made of ordered **steps**.
  - Promotes:
    - **Efficiency**.
    - **Reproducibility**.
    - **Collaboration**.
- **Analogy**:
  - Movie production pipeline:
    - Script writing → Casting → Filming → Editing → Distribution.
    - Each step depends on previous ones.
  - ML pipeline in ZenML:
    - Data preparation → Feature engineering → Training → Evaluation → Deployment.

### 11.3 Example ZenML Pipeline

- Steps (decorated with `@step`):
  1. `importer_step`:
     - Loads data:
       - `load_digits` dataset from scikit-learn.
       - Reshapes data.
       - Splits into train/test: `X_train`, `X_test`, `y_train`, `y_test`.
     - Returns:
       - `np.ndarray` for X and y (both train and test).
  2. `svc_trainer`:
     - Trains **SVC (Support Vector Classifier)**:
       - On `X_train`, `y_train`.
     - Returns:
       - Trained `ClassifierMixin` object (SVC model).
  3. `evaluator`:
     - Takes:
       - `X_test`, `y_test`.
       - Trained model.
     - Computes metrics (e.g. accuracy).
     - Returns:
       - `float` score.

- Pipeline (decorated with `@pipeline`):
  - Combines these steps:
    ```python
    @pipeline
    def digits_pipeline():
        X_train, X_test, y_train, y_test = importer()
        model = svc_trainer(X_train, y_train)
        accuracy = evaluator(model, X_test, y_test)
    ```
  - Running `digits_pipeline()`:
    - Creates a **pipeline run**.
    - Steps:
      - `importer` → `svc_trainer` → `evaluator`.

### 11.4 ZenML Dashboard

- `zenml up`:
  - Starts ZenML server and dashboard.
- Dashboard features:
  - View **pipelines** and **runs**.
  - See:
    - Step start/finish times.
    - Logs.
    - Artifacts:
      - E.g. dataframes, models, metrics.
  - Access:
    - Prompted to login (`username: default`).

### 11.5 Benefits of Pipelines

- **Rerun entire workflows** easily, not just the model.
- **Track previous runs**:
  - Compare versions.
  - Analyze metric changes over time.
- Automate:
  - Retraining.
  - Redeployment.
  - Integrations with CI/CD.

---

## 12. Pipeline Caching in ZenML

- **Caching concept**:
  - If a step’s input and code haven’t changed:
    - ZenML can **reuse outputs** from previous runs.
    - Shows logs like “using cached version of step X”.
- **Effect**:
  - Greatly speeds up repeated pipeline runs.
  - Example:
    - For large models, reusing cached steps can save huge time.

- **How to control caching**:
  - At step-level with `@step(enable_cache=True/False)`.
- **Demonstrated behavior**:
  - When `enable_cache=True`:
    - Steps reuse previous artifacts if unchanged.
  - When `enable_cache=False`:
    - Steps rerun regardless of previous outputs.

---

## 13. Project Setup: Customer Satisfaction Use Case

### 13.1 Dataset Description

- Uses a **customer dataset** (likely from an e-commerce context).
- Source CSV structure (large file) contains:
  - `order_id`
  - `customer_id`
  - `order_status`
  - `order_purchase_timestamp`
  - `order_approved_at`
  - `order_delivered_carrier_date`
  - `order_delivered_customer_date`
  - `order_estimated_delivery_date`
  - customer info:
    - `customer_city`
    - `customer_state`
    - etc.
  - Geolocation dataset.
  - Items dataset.
  - Many other fields.
- **Custom dataset**:
  - Instructor combined multiple original tables into a **single dataset**.
  - Final dataset contains:
    - Many combined features.
    - `review_score` (from 1 to 5) as the **target variable**.
  - Initially will **not** use `review_comment` text:
    - Many features will be **dropped** for simplicity.
    - Students can extend later for more complex modeling.

### 13.2 Environment Setup

- Strong recommendation to use a **virtual environment**:
  - Examples:
    - `pipenv`
    - `conda`
    - `venv`
  - Benefits:
    - Prevent dependency conflicts.
    - Contain project-specific libraries.
- Instructor uses:
  - Something called **“spy env”** (likely `pipenv`/`pyenv`).
  - Environment named `customer_satisfaction`.

- **Important note**:
  - Earlier in the course, resources are linked explaining:
    - What virtual environments are.
    - How to create and use them.

### 13.3 Installing Dependencies

- Example dependencies:
  - `zenml[server]`
  - `pandas`
  - `scikit-learn`
  - `pyarrow`
  - Additional ML libraries:
    - `catboost`
    - `xgboost`
    - `lightgbm`
  - **Note**:
    - The course uses only **simple models** in this project.
    - Other advanced models (CatBoost, XGBoost, LightGBM) are for exploration and the core ML course.
- Commands:
  - `pip install zenml[server]`
  - `zenml init` – initializes ZenML repository (`.zen` folder).
  - `zenml up` – starts dashboard/server.

### 13.4 Initial Project Folder Structure

Created folders/files:

- `.zen/` (auto-created by ZenML)
- `data/`:
  - Contains CSV dataset(s), e.g. `olist_customers_dataset.csv` (combined file).
- `src/` (or `source/`):
  - Contains core source code.
- `pipelines/`:
  - Contains pipeline definitions, e.g. `training_pipeline.py`, `deployment_pipeline.py`.
- `steps/`:
  - Contains individual pipeline steps:
    - `ingest_data.py`
    - `clean_data.py`
    - `model_train.py`
    - `evaluation.py`
- `saved_models/`:
  - For storing serialized models (optional; ZenML artifacts can handle storage).
- `__init__.py`:
  - To treat directories as packages.
- `requirements.txt`:
  - List of all dependencies.
- `run_pipeline.py`:
  - Script to run training pipeline.
- `run_deployment.py`:
  - Script to run deployment/inference pipelines (later).

- **Future enhancement**:
  - In later projects, rather than using CSVs:
    - Data will be sourced from **PostgreSQL** or other SQL databases.
    - More realistic setup.

---

## 14. Step 1: Data Ingestion Step (`ingest_data.py`)

### 14.1 Ingestion Class and Step

- **Imports**:
  - `logging`
  - `pandas as pd`
  - `from zenml import step`
- **Class: `IngestData`**:
  - Attributes:
    - `data_path` – path to CSV.
  - Methods:
    - `__init__(self, data_path: str)`.
    - `get_data(self) -> pd.DataFrame`:
      - Reads CSV via `pd.read_csv(self.data_path)`.

- **Step function: `ingest_df`**:
  - Decorated with `@step`.
  - Signature:
    ```python
    @step
    def ingest_df(data_path: str) -> pd.DataFrame:
        """
        Ingests the data from the data path.

        Args:
            data_path: The path to the data.

        Returns:
            A pandas DataFrame.
        """
    ```
  - Implementation:
    - Uses try/except.
    - Instantiates `IngestData(data_path)`.
    - Calls `get_data()`.
    - Logs success or error.
    - Returns DataFrame.

- This step provides the **raw DataFrame** to the rest of the pipeline.

---

## 15. Step 2: Data Cleaning with Strategy Pattern (`clean_data.py` and `data_cleaning.py`)

### 15.1 Strategy Pattern Overview

- Uses **Strategy Design Pattern**:
  - Abstract base class defines an interface.
  - Concrete strategy classes implement specific behaviors.
- Related concepts:
  - Students are expected to know:
    - Strategy pattern.
    - Factory pattern.
    - Singleton pattern.
  - These are covered in earlier resources or the core ML course.

### 15.2 `src/data_cleaning.py`

#### 15.2.1 Imports

- `logging`
- `from abc import ABC, abstractmethod`
- `from typing import Union, Tuple`
- `pandas as pd`
- `numpy as np`
- `from sklearn.model_selection import train_test_split`

#### 15.2.2 Abstract Class: `DataStrategy`

- Inherits from `ABC`.
- Abstract method:
  ```python
  @abstractmethod
  def handle_data(self, df: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]:
      pass
  ```
- Purpose:
  - Unified interface for different data strategies.

#### 15.2.3 Concrete Strategy: `DataPreprocessStrategy`

- Inherits from `DataStrategy`.
- Implements:
  ```python
  def handle_data(self, data: pd.DataFrame) -> pd.DataFrame:
      # Steps:
      # 1. Drop specific columns.
      # 2. Fill null values.
      # 3. Select only numeric columns.
      # 4. Drop unnecessary columns.
      # 5. Return cleaned data.
  ```
- Detailed operations (for simplicity; not claiming these are unimportant, but simplifying):
  1. **Drop columns**:
     - E.g.:
       - `order_approved_at`
       - `order_delivered_carrier_date`
       - `order_delivered_customer_date`
       - `order_estimated_delivery_date`
       - And other date/time features.
  2. **Fill nulls**:
     - For several numeric columns:
       - Fill with **median**.
     - For text columns like `review_comment_message`:
       - Fill nulls with `"No review"`.
  3. **Select numeric columns only**:
     - `data = data.select_dtypes(include=np.number)`
     - Result: All **categorical** and text fields removed.
     - This avoids:
       - Encoding.
       - Tokenization.
       - More complex preprocessing.
  4. **Drop additional columns**:
     - E.g.:
       - `customer_zip_code_prefix`
       - `order_item_id`
     - These are deemed less relevant for this simplified project.
  5. **Return cleaned `DataFrame`**.

- Rationale:
  - Simplify the project to focus on **MLOps**, not complex feature engineering.
  - Advanced feature engineering is taught in the **core ML course**.

#### 15.2.4 Concrete Strategy: `DataDivideStrategy`

- Inherits `DataStrategy`.
- Implements:
  - Splitting data into **train/test**:
    ```python
    def handle_data(self, data: pd.DataFrame):
        X = data.drop("review_score", axis=1)
        y = data["review_score"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        return X_train, X_test, y_train, y_test
    ```
- Return type:
  - `Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]`.

#### 15.2.5 Class: `DataCleaning`

- Purpose:
  - Compose strategies and expose a unified interface.
- Constructor:
  ```python
  def __init__(self, data: pd.DataFrame, strategy: DataStrategy):
      self.data = data
      self.strategy = strategy
  ```
- Method:
  ```python
  def handle_data(self) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]]:
      return self.strategy.handle_data(self.data)
  ```

- Example usage:
  ```python
  if __name__ == "__main__":
      df = pd.read_csv("data.csv")
      cleaner = DataCleaning(df, DataPreprocessStrategy())
      processed_df = cleaner.handle_data()

      divider = DataCleaning(processed_df, DataDivideStrategy())
      X_train, X_test, y_train, y_test = divider.handle_data()
  ```

### 15.3 `steps/clean_data.py`

- **Imports**:
  - `logging`
  - `from zenml import step`
  - `from typing_extensions import Annotated`
  - `from typing import Tuple`
  - `pandas as pd`
  - `from src.data_cleaning import DataCleaning, DataPreprocessStrategy, DataDivideStrategy`

- **Step function: `clean_df`**:
  - Decorated with `@step`.
  - Signature:
    ```python
    @step
    def clean_df(
        data: pd.DataFrame,
    ) -> Tuple[
        Annotated[pd.DataFrame, "X_train"],
        Annotated[pd.DataFrame, "X_test"],
        Annotated[pd.Series, "y_train"],
        Annotated[pd.Series, "y_test"],
    ]:
    ```
  - Body:
    - Try/except.
    - Instantiate `DataCleaning` with `DataPreprocessStrategy`.
    - Apply `handle_data` → `processed_data`.
    - Instantiate `DataCleaning` with `DataDivideStrategy`.
    - Apply `handle_data` → `X_train, X_test, y_train, y_test`.
    - Log:
      - Data cleaning completed.
    - Return:
      - `X_train`, `X_test`, `y_train`, `y_test`.

- Uses `Annotated` from `typing_extensions` to:
  - Add names to outputs for ZenML metadata.

---

## 16. Step 3: Model Development (`src/model_dev.py` and `steps/model_train.py`)

### 16.1 `src/model_dev.py`

- **Imports**:
  - `from abc import ABC, abstractmethod`
  - `pandas as pd`
  - `numpy as np`
  - `from sklearn.linear_model import LinearRegression`

- **Abstract class: `Model`**:
  - Similar to strategy pattern for models.
  - Abstract method:
    ```python
    @abstractmethod
    def train(self, X_train: pd.DataFrame, y_train: pd.Series):
        pass
    ```

- **Concrete class: `LinearRegressionModel`**:
  - Inherits `Model`.
  - Attributes:
    - Underlying `LinearRegression()` instance.
  - Method:
    ```python
    def train(self, X_train, y_train):
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    ```
  - Wrapped in try/except with logging and error propagation.

- Note:
  - This is a **simple baseline** for demonstration.
  - More advanced models and validations are left to core ML course.

### 16.2 Step: `train_model` (`steps/model_train.py`)

- **Imports**:
  - `logging`
  - `pandas as pd`
  - `from zenml import step`
  - `from sklearn.base import RegressorMixin`
  - `from src.model_dev import LinearRegressionModel`
  - `from .config import ModelNameConfig` (config file)
- **Config class** (`config.py`):
  - Uses:
    ```python
    from zenml.steps import BaseParameters

    class ModelNameConfig(BaseParameters):
        model_name: str = "linear_regression"
    ```

- **Step function: `train_model`**:
  - Signature:
    ```python
    @step
    def train_model(
        X_train: pd.DataFrame,
        X_test: pd.DataFrame,
        y_train: pd.Series,
        y_test: pd.Series,
        config: ModelNameConfig,
    ) -> RegressorMixin:
    ```
  - Logic:
    - Checks `config.model_name`.
    - If `"linear_regression"`:
      - Instantiates `LinearRegressionModel()`.
      - Trains on `X_train, y_train`.
      - Returns trained model.
    - Else:
      - Raises `ValueError` if unknown model name.
    - Includes try/except logging.

- Allows easy extension:
  - Add new model classes (e.g. `RandomForestModel`).
  - Adjust `if` logic in step to support more models without changing pipeline.

---

## 17. Step 4: Evaluation (`src/evaluation.py` and `steps/evaluation.py`)

### 17.1 `src/evaluation.py` – Strategy Pattern for Metrics

- **Imports**:
  - `logging`
  - `from abc import ABC, abstractmethod`
  - `from sklearn.metrics import mean_squared_error, r2_score`
  - `numpy as np`

- **Abstract class: `Evaluation`**:
  - Method:
    ```python
    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        pass
    ```

- **Concrete strategies**:

  1. **`MSE`**:
     - Implements:
       ```python
       def calculate_scores(self, y_true, y_pred):
           mse = mean_squared_error(y_true, y_pred)
           return mse
       ```

  2. **`R2`**:
     - Implements:
       ```python
       def calculate_scores(self, y_true, y_pred):
           r2 = r2_score(y_true, y_pred)
           return r2
       ```

  3. **`RMSE`**:
     - Implements:
       ```python
       def calculate_scores(self, y_true, y_pred):
           rmse = mean_squared_error(y_true, y_pred, squared=False)
           return rmse
       ```

- All use try/except with logging.

### 17.2 Step: `evaluate_model` (`steps/evaluation.py`)

- **Imports**:
  - `logging`
  - `from typing import Tuple`
  - `from typing_extensions import Annotated`
  - `import numpy as np`
  - `import pandas as pd`
  - `from sklearn.base import RegressorMixin`
  - `from zenml import step`
  - `from src.evaluation import MSE, RMSE, R2`
  - `import mlflow` (for logging metrics to MLflow later).

- **Step function: `evaluate_model`**:
  - Signature:
    ```python
    @step
    def evaluate_model(
        model: RegressorMixin,
        X_test: pd.DataFrame,
        y_test: pd.Series,
    ) -> Tuple[
        Annotated[float, "mse"],
        Annotated[float, "r2"],
        Annotated[float, "rmse"],
    ]:
    ```
  - Implementation:
    - `predictions = model.predict(X_test)`.
    - Creates instances:
      - `mse_evaluator = MSE()`
      - `r2_evaluator = R2()`
      - `rmse_evaluator = RMSE()`
    - Computes:
      - `mse = mse_evaluator.calculate_scores(y_test, predictions)`
      - `r2 = r2_evaluator.calculate_scores(y_test, predictions)`
      - `rmse = rmse_evaluator.calculate_scores(y_test, predictions)`
    - Logs metrics with:
      - `mlflow.log_metric("mse", mse)`
      - `mlflow.log_metric("r2", r2)`
      - `mlflow.log_metric("rmse", rmse)`
    - Returns `(mse, r2, rmse)`.

---

## 18. Training Pipeline (`pipelines/training_pipeline.py`) and `run_pipeline.py`

### 18.1 Training Pipeline Definition

- **Imports**:
  - `from zenml import pipeline`
  - `from steps.ingest_data import ingest_df`
  - `from steps.clean_data import clean_df`
  - `from steps.model_train import train_model`
  - `from steps.evaluation import evaluate_model`
  - `from steps.config import ModelNameConfig`

- **Pipeline decorator**:
  ```python
  @pipeline(enable_cache=True)
  def train_pipeline(data_path: str):
      df = ingest_df(data_path)
      X_train, X_test, y_train, y_test = clean_df(df)
      model = train_model(X_train, X_test, y_train, y_test, ModelNameConfig())
      mse, r2, rmse = evaluate_model(model, X_test, y_test)
  ```

### 18.2 Running the Training Pipeline

- **`run_pipeline.py`**:
  - Imports pipeline:
    ```python
    from pipelines.training_pipeline import train_pipeline
    ```
  - In `if __name__ == "__main__":`:
    - Calls:
      ```python
      data_path = "data/your_dataset.csv"
      train_pipeline(data_path=data_path)
      ```
- **Command**:
  - `python run_pipeline.py`

### 18.3 Observations and Fixes During Development

- Common errors and fixes:
  - `ModuleNotFoundError` for `pandas` → `pip install pandas`.
  - `TypeError: cannot unpack non-iterable StepArtifact`:
    - Occurs if a step doesn’t return outputs as specified.
    - E.g. `clean_df` must `return X_train, X_test, y_train, y_test`.
  - `NameError` issues like `R2_score not defined`:
    - Corrected to `R2` or proper naming consistent with implementation.
  - Mis-typed pipeline decorator or imports (e.g. `pipelin` vs `pipeline`).

- After fixes:
  - Pipeline runs successfully.
  - ZenML dashboard shows:
    - `ingest_df` outputs (DataFrame artifact).
    - `clean_df` outputs (split data).
    - `train_model` outputs (trained model).
    - `evaluate_model` outputs (metrics).
  - Artifacts stored in artifact store:
    - Each step writes outputs to a specific URI.

---

## 19. Integrating Experiment Tracking with MLflow

### 19.1 Why Track Experiments?

- Need to:
  - Track every experiment run.
  - Compare model performance across:
    - Different hyperparameters.
    - Different versions.
  - Use metrics to select best model for deployment.

### 19.2 Setting Up MLflow in ZenML Stack

- **Install MLflow integration**:
  - `zenml integration install mlflow`
- **Check current stack**:
  - `zenml stack list`
  - `zenml stack describe`
- **Register experiment tracker**:
  - Example:
    ```bash
    zenml experiment-tracker register mlflow_tracker --flavor=mlflow
    ```
  - If names conflict (already used), use a new name:
    - e.g. `mlflow_tracker_customer`.
- **Register model deployer**:
  - Example:
    ```bash
    zenml model-deployer register mlflow_customer --flavor=mlflow
    ```
- **Create new stack including MLflow components**:
  - Example:
    ```bash
    zenml stack register customer_stack \
      -a default \
      -o default \
      -d mlflow_customer \
      -x mlflow_tracker_customer
    zenml stack set customer_stack
    ```

- After this:
  - `zenml stack describe` shows:
    - Artifact store: `default`
    - Orchestrator: `default`
    - Model deployer: `mlflow_customer`
    - Experiment tracker: `mlflow_tracker_customer`

### 19.3 Using MLflow in Steps

- **In `model_train` and `evaluate_model`**:
  - Import:
    ```python
    import mlflow
    from zenml.client import Client
    ```
  - Get experiment tracker:
    ```python
    client = Client()
    experiment_tracker = client.active_stack.experiment_tracker
    ```
  - Add to step decorator:
    ```python
    @step(experiment_tracker=experiment_tracker.name)
    def train_model(...):
        with mlflow.sklearn.autolog():
            # training logic
    ```

- `mlflow.sklearn.autolog()`:
  - Automatically logs:
    - Parameters.
    - Metrics.
    - Model artifact.

- In `evaluate_model`:
  - Explicit metric logging:
    - `mlflow.log_metric("mse", mse)`
    - `mlflow.log_metric("r2", r2)`
    - `mlflow.log_metric("rmse", rmse)`

### 19.4 Accessing MLflow UI

- Need MLflow tracking URI; ZenML stores runs in `mlruns/`.
- In Python:
  ```python
  import mlflow
  print(mlflow.get_tracking_uri())
  ```
- Use:
  ```bash
  mlflow ui --backend-store-uri "file:/path/to/mlruns"
  ```
  or:
  ```bash
  mlflow ui --backend-store-uri file:/absolute/path/to/mlruns
  ```
- Access MLflow UI in browser:
  - See experiments, runs, metrics, and model artifacts.

---

## 20. Deployment with MLflow and ZenML

### 20.1 Overview

- Goal:
  - Deploy the trained model **locally** using **MLflow model deployer**.
  - Implement:
    - **Continuous deployment pipeline**:
      - Train → Evaluate → Decide to deploy.
    - **Inference pipeline**:
      - Load deployed service + data → Make predictions.

- This approach is for **local deployment**:
  - For cloud platforms (AWS, GCP), would use other tools (like Seldon, etc.).

### 20.2 Deployment Pipeline (`pipelines/deployment_pipeline.py`)

#### 20.2.1 Imports

- `numpy as np`
- `pandas as pd`
- `from zenml import pipeline, step`
- `from zenml.config import DockerSettings`
- `from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT`
- `from zenml.integrations.mlflow.steps import mlflow_model_deployer_step`
- Steps:
  - `from steps.ingest_data import ingest_df`
  - `from steps.clean_data import clean_df`
  - `from steps.model_train import train_model`
  - `from steps.evaluation import evaluate_model`
  - `from steps.deployment_trigger import deployment_trigger`
- MLflow deployer:
  - `from zenml.integrations.mlflow.model_deployers import MLFlowModelDeployer` (or similar).

#### 20.2.2 Docker Settings

- Define Docker settings:
  ```python
  docker_settings = DockerSettings(required_integrations=["mlflow"])
  ```

- Used in pipeline:
  ```python
  @pipeline(enable_cache=True, settings={"docker": docker_settings})
  def continuous_deployment_pipeline(...):
      ...
  ```

#### 20.2.3 Deployment Trigger Step (`steps/deployment_trigger.py`)

- Uses a config to decide **whether to deploy** based on metric (e.g. R²).
- **Config class**:
  ```python
  from zenml.steps import BaseParameters

  class DeploymentTriggerConfig(BaseParameters):
      minimum_accuracy: float = 0.5  # or 0.992 initially, later adjusted
  ```
- **Step function**:
  ```python
  @step
  def deployment_trigger(
      accuracy: float, config: DeploymentTriggerConfig
  ) -> bool:
      """
      Implements a simple deployment trigger that checks if accuracy
      is good enough for deployment.
      """
      return accuracy >= config.minimum_accuracy
  ```

- Instructor initially sets `minimum_accuracy` high (e.g. `0.992`), then lowers it when R² is poor.

#### 20.2.4 Continuous Deployment Pipeline Logic

- Pipeline signature:
  ```python
  @pipeline(
      enable_cache=True,
      settings={"docker": docker_settings},
  )
  def continuous_deployment_pipeline(
      data_path: str,
      minimum_accuracy: float = 0.5,
      workers: int = 3,
      timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT,
  ):
  ```
- Inside:
  - `df = ingest_df(data_path)`
  - `X_train, X_test, y_train, y_test = clean_df(df)`
  - `model = train_model(X_train, X_test, y_train, y_test, ModelNameConfig())`
  - `mse, r2, rmse = evaluate_model(model, X_test, y_test)`
  - `deploy_decision = deployment_trigger(r2, DeploymentTriggerConfig(minimum_accuracy=minimum_accuracy))`
  - `mlflow_model_deployer_step(
        model=model,
        deploy_decision=deploy_decision,
        workers=workers,
        timeout=timeout
    )`

- `mlflow_model_deployer_step`:
  - Prebuilt ZenML step from MLflow integration.
  - Handles:
    - Deploying the trained model as an MLflow service.
    - Updating existing deployment if deployed already.

#### 20.2.5 Handling Errors and Adjustments

- Common issues:
  - `TypeError` due to wrong `settings` key (`"DockerSettings"` instead of `"docker"`).
  - `deployment_decision` vs `deploy_decision` naming mismatches.
  - Missing `data_path` arg in pipeline call.
  - R² being too low to meet `minimum_accuracy`, causing:
    - “Skipping model deployment because model quality does not match criteria.”
  - Fix:
    - Lower `minimum_accuracy` to allow deployment (e.g. `0.0` or `0.5`) to verify pipeline works.

- Service startup issues:
  - `MLflow deployment service daemon is not running`:
    - Often due to:
      - Old leftover services or environment conflicts.
    - Resolutions:
      - Delete old deployments.
      - Ensure correct stack usage.
      - Adjust environment, re-run `zenml up`.
      - Sometimes simply restarting the machine.

### 20.3 Run Deployment Script (`run_deployment.py`)

#### 20.3.1 Using `click` for CLI

- **Imports**:
  - `click`
  - `from pipelines.deployment_pipeline import continuous_deployment_pipeline, inference_pipeline`
  - `from zenml.client import Client`
  - `from zenml.integrations.mlflow.model_deployers import MLFlowModelDeployer`
  - Other utilities.

- **Command options**:
  - `--config`:
    - Choices: `"deploy"`, `"predict"`, `"deploy_and_predict"`.
  - `--min-accuracy`:
    - Float threshold (e.g. `0.5`).
- **Function**:
  ```python
  @click.command()
  @click.option("--config", type=click.Choice(["deploy", "predict", "deploy_and_predict"]), default="deploy")
  @click.option("--min-accuracy", type=float, default=0.5)
  def run_deployment(config: str, min_accuracy: float):
      ...
  ```
- **MLflow deployer retrieval**:
  - `mlflow_model_deployer = MLFlowModelDeployer.get_active_model_deployer()`
- **Logic**:
  - If `config == "deploy"`:
    - Calls `continuous_deployment_pipeline(...)`.
    - Checks if service is running with:
      - `mlflow_model_deployer.find_model_server(...)`.
    - Prints status messages.
  - If `config` includes `"predict"`:
    - Also run `inference_pipeline(...)` (see next).

### 20.4 Inference Pipeline

#### 20.4.1 Prediction Service Loader Step

- **Step: `prediction_service_loader`**:
  - Inputs:
    - `pipeline_name: str`
    - `pipeline_step_name: str`
    - `model_name: str = "model"`
    - `running: bool = True` (or `False` if just retrieving).
  - Returns:
    - `MLFlowDeploymentService` (or similar MLflow service object).
  - Implementation:
    - Fetches active MLflow deployer:
      ```python
      mlflow_model_deployer = MLFlowModelDeployer.get_active_model_deployer()
      ```
    - Uses:
      ```python
      existing_services = mlflow_model_deployer.find_model_server(
          pipeline_name=pipeline_name,
          pipeline_step_name=pipeline_step_name,
          model_name=model_name,
          running=running
      )
      ```
    - If none found:
      - Raises `RuntimeError`:
        - “No MLflow service found for pipeline X and step Y; model not deployed.”
    - Else:
      - Returns the existing service.

#### 20.4.2 Dynamic Data Importer Step

- **Step: `dynamic_importer`**:
  - Returns `str`:
    - JSON string representing test data.
  - Implementation:
    - Calls `get_data_for_test()` from `src.utils`.
- **`src/utils.py`**:
  - Imports:
    - `logging`
    - `pandas as pd`
    - From `src.data_cleaning`: `DataCleaning`, `DataPreprocessStrategy`.
  - `get_data_for_test()`:
    - Reads full dataset (similar to ingestion).
    - Preprocesses using `DataPreprocessStrategy`.
    - Samples a subset (e.g. 100 rows).
    - Drops target `review_score`.
    - Converts to JSON string with `.to_json(orient="records")`.
    - Returns JSON string.

#### 20.4.3 Predictor Step

- **Step: `predictor`**:
  - Inputs:
    - `service`: MLflow deployment service (from `prediction_service_loader`).
    - `data: str` (JSON string).
  - Process:
    - `json_data = json.loads(data)` → Python list.
    - Convert to `pd.DataFrame`.
    - Prepare:
      - Possibly rename columns or ensure correct shape.
    - Use service’s prediction endpoint:
      - `service.predict(df)` or sending data via REST (implementation from ZenML sample).
    - Convert predictions to `np.ndarray`.
  - Return:
    - `np.ndarray` with predictions.

- **Note on materializers**:
  - There was an error:
    - “Built-in materializer cannot handle numpy.ndarray; using default pickle materializer.”
  - This indicates:
    - ZenML falls back to a default `pickle` materializer.
  - It warns that this may not be production-grade but is acceptable for demo.

#### 20.4.4 Inference Pipeline Definition

- **Pipeline**:
  ```python
  @pipeline(
      enable_cache=False,
      settings={"docker": docker_settings},
  )
  def inference_pipeline(pipeline_name: str, pipeline_step_name: str):
      data = dynamic_importer()
      service = prediction_service_loader(
          pipeline_name=pipeline_name,
          pipeline_step_name=pipeline_step_name,
          running=False,
          model_name="model",
      )
      predictions = predictor(service=service, data=data)
  ```

- Called from `run_deployment.py` when `config` is `predict` or `deploy_and_predict`.

### 20.5 Running Deployment and Inference

- **Deploy**:
  ```bash
  python run_deployment.py --config deploy --min-accuracy 0.0
  ```
  - Trains model.
  - Evaluates.
  - Triggers deployment if R² ≥ min_accuracy.
  - If successful:
    - MLflow service is running.
- **Predict**:
  ```bash
  python run_deployment.py --config predict
  ```
  - Loads deployed service.
  - Fetches test data via `dynamic_importer`.
  - Produces predictions.
  - ZenML dashboard shows:
    - `dynamic_importer` step output (data).
    - `prediction_service_loader` step output (service).
    - `predictor` step output (predictions).
    - Visualization of predictions:
      - E.g., mean and standard deviation.

---

## 21. Streamlit App for Interactive Inference (`streamlit_app.py`)

- **Purpose**:
  - Allow **single-click** inference using deployed MLflow model.
- **Imports**:
  - `streamlit as st`
  - `pandas as pd`
  - `from pipelines.deployment_pipeline import prediction_service_loader`
  - `from run_deployment import main as run_main` (renamed function for CLI style).
  - `json` and other utilities.

- **Workflow**:
  1. User opens Streamlit app:
     - `streamlit run streamlit_app.py`.
  2. App loads:
     - UI elements for entering feature values or using default test data.
  3. On **Predict** button:
     - Uses `prediction_service_loader` to:
       - Get MLflow service (`service`).
     - Prepares input data as DataFrame.
     - Calls `service.predict(df)` or appropriate API.
     - Displays predicted **review score**.

- **Example**:
  - For some input features, app shows:
    - “Your predicted review score is **4.22**” (example from transcript).

- **Note**:
  - The app directly uses the **deployed MLflow model**, not a locally loaded `.pkl` file.
  - Pipeline and service infrastructure remain in place.

---

## 22. Debugging, Warnings, and Practical Notes

- **Frequent issues & remedies**:
  - **Version mismatches**:
    - ZenML vs MLflow vs sklearn.
    - Solutions:
      - `zenml downgrade`
      - `pip install --upgrade mlflow`
      - `pip install --upgrade scikit-learn`
  - **ZenML store connection errors**:
    - Use:
      - `zenml disconnect`
      - Then `zenml up`.
  - **Pipeline settings errors**:
    - Ensure `settings={"docker": docker_settings}` (not `DockerSettings` as key).
  - **Name errors**:
    - Double-check step and variable names:
      - `deployment_decision` vs `deploy_decision`.
      - `main` vs `run` function names.
  - **Minimal accuracy fails**:
    - R² may be low.
    - Adjust `minimum_accuracy` for demonstration, then tune data/model.

- **Key experiential lesson**:
  - Most of the time in real projects goes into:
    - Debugging pipelines.
    - Matching library versions.
    - Configuring deployment infrastructure.
  - This matches the earlier statement:
    - Deployment is **painfully slow** compared to model building.

---

## 23. What Has Been Achieved in the Project

- Built an end-to-end **MLOps project** for **customer satisfaction / review score prediction**:

  1. **Data ingestion**:
     - CSV → DataFrame via `ingest_df` step.
  2. **Data cleaning & splitting**:
     - Strategy pattern for preprocessing and splitting.
     - `clean_df` step returning `X_train, X_test, y_train, y_test`.
  3. **Model training**:
     - Baseline **Linear Regression** model.
     - Configurable via `ModelNameConfig`.
  4. **Evaluation**:
     - Metrics: `MSE`, `R²`, `RMSE`.
     - Logged to **MLflow**.
  5. **Experiment tracking**:
     - MLflow integrated with ZenML experiment tracker.
     - MLflow UI shows all runs, metrics, parameters, and models.
  6. **Deployment**:
     - Continuous deployment pipeline with deployment trigger.
     - Uses **MLflow model deployer**.
     - Deploys model as local service.
  7. **Inference**:
     - Inference pipeline that:
       - Loads service.
       - Imports data dynamically.
       - Calls service for predictions.
  8. **Interactive demo**:
     - Streamlit app uses deployed MLflow service for predictions.

- **Key learnings**:
  - How to structure a real **MLOps project**:
    - Steps.
    - Pipelines.
    - Configs.
  - How caching and artifact management work in ZenML.
  - How to integrate MLflow for both:
    - Experiment tracking.
    - Model deployment.
  - How **end-to-end automation** (from ingestion to deployment) operates in practice.

- **Next steps (as mentioned by instructor)**:
  - Future projects:
    - More complex models.
    - Better feature engineering and validation.
    - Using SQL databases instead of CSV.
    - Additional deployment patterns and tools.

---

This Markdown document reorganizes and condenses the transcription into a coherent, structured summary while **preserving all original information**: all examples, explanations, technical details, workflows, implementation details, debugging experiences, and conceptual insights from the transcript are retained and clarified.