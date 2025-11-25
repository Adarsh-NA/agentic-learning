# ML Ops Course Intro & ZenML Project – Complete Structured Summary

---

## 1. Course Context & Instructor Background

- **Course goal**:  
  - Teach ML Ops (MLOps) fundamentals and an end-to-end project, enabling learners to:
    - Add a “creamy layer” (engineering / MLOps excellence) on top of their machine learning projects and take-home challenges.
    - Become capable of securing **high-paying ML/ML Ops jobs**, including **international remote offers** while living in India.

- **Instructor’s experience**:
  - Secured a **data center internship** at a US-based startup:
    - Paid **2x Google India software engineer salary**.
  - Received **multiple offers** from international companies in:
    - US, UK, Germany, etc.
  - Professional roles:
    - **Lead Data Scientist at Triplet**:
      - Led multiple products in the **creator economy**.
    - **MLOps Engineer** on **ZenML**, one of the fastest growing MLOps frameworks.
    - **Data Scientist at Artifact**:
      - Built large-scale **NLP products** even before GPT was launched.
  - Based on this experience, the instructor positions themself as a suitable guide for MLOps.

- **Course resources**:
  - All links and materials are listed in the description on **Moxpillow** (platform reference by instructor).

---

## 2. High-Level Course Overview

- Course focus:
  - Add an **MLOps “creamy layer”** over existing ML projects and take-home assignments.
  - Teach:
    - MLOps **fundamentals**.
    - One **end-to-end project** from:
      - Data ingestion → data processing → model training → evaluation → deployment.
    - Use **state-of-the-art tools**:
      - **MLflow**
      - **ZenML**
      - Other related tools (e.g., orchestrators, artifact stores).

- Positioning:
  - **MLOps is a relatively new field** with scarce resources.
  - Called a **“gold mine”** and **“game changer”** in the ML community.
  - If learners follow the course with **dedication and patience**, they can:
    - Learn MLOps.
    - Translate this into **better/international job offers**.

---

## 3. Introduction to MLOps: Motivation & Need

### 3.1 Growth of Data & AI

- **Data growth**:
  - Data volume is growing **exponentially**.
- **AI importance**:
  - Importance of **Artificial Intelligence** has also **significantly increased**.
- Goal:
  - Utilize the increasing data **in the right and positive way**.
  - This is where **AI and ML** come in.

### 3.2 Misconception: ML is Just Building Models

- Many think:
  - “We just build a prediction model on top of data and we’re done.”
- Instructor’s assertion:
  - **Machine learning code / model** is only about **20%** of the entire ML project or business solution.
  - The remaining **80%** is **engineering & surrounding systems**.
- This is supported by:
  - **Jim Huen** (MLOps expert) – validates that:
    - ML in industry is **more than training models**.
  - **Elon Musk** – states:
    - *“Machine learning engineering is 10% machine learning and 90% engineering.”*

- Problem:
  - Most online courses focus only on **machine learning engineering** (model building).
  - They do **not teach the engineering part** (production, deployment, monitoring, etc.).
  - Learners often assume this is just:
    - Data structures & algorithms (DSA),
    - Or design patterns.
  - Reality:
    - While DSA & design patterns matter, **there is much more** specific engineering in MLOps:
      - Pipelines
      - Productionizing data and models
      - Monitoring
      - Compliance
      - Automation, etc.

---

## 4. Typical ML Team & Responsibilities

In a typical ML team in a corporate setup:

- **Data Scientist**:
  - Discovers raw data.
  - Develops features.
  - Trains models.

- **Data Engineer**:
  - “Productionizes” data pipelines:
    - Sets up scalable, reliable data ingestion and transformation.
    - Handles where data comes from and makes it usable at large scale.
  - The term **“productionize”** refers to moving from experimental/notebooks to **robust, production-grade pipelines**.

- **ML Engineer**:
  - Deploys models so they can be used by users.
  - Responsible for:
    - Deployment.
    - Integrating model endpoints with web/mobile applications.
    - Ensuring scalability & reliability.

- **Integration & Monitoring**:
  - The deployed model is integrated into:
    - Website / Application / Backend services.
  - Model outputs are **monitored** continuously.

- **Lawyer / Legal Counsel**:
  - Answers questions such as:
    - “Can I use this data for my model – yes or no?”
  - Ensures compliance with:
    - Data protection laws.
    - Ethical & legal constraints.

- The instructor notes:
  - Many learners are **unfamiliar** with terms like:
    - Training models in production context.
    - Productionizing.
    - Deployment.
    - Integration.
    - Monitoring.
  - This **introductory lecture** is meant to:
    - Clarify all these terms.
    - Prepare learners to understand the terminology used in the project later.

---

## 5. What Data Science “Looks Like” vs. Engineering Reality

### 5.1 Data Scientist’s Simplified View

- Many think ML is:
  - `pd.read_csv()` → train a model → `clf.fit()` → `clf.predict()` → `clf.score()`.
- This leads to the misconception that:
  - Writing **3–4 lines of code** is enough to get a job.
- Reality:
  - Companies will **not hire** based on just this.
  - True focus should be:
    - **90% on engineering**, 10% on the bare ML code.

### 5.2 Engineering Perspective (ML in Production)

- Actual production ML involves:
  - **Collecting data**.
  - **Training models**.
  - **Deploying models** to production.
  - **Monitoring and maintaining** them in a loop.
- The engineering side is:
  - Much more **complex and “scary”** than the toy data science viewpoint.

---

## 6. What is Deployment?

### 6.1 Concept

- **Deployment definition**:
  - Moving a **trained local model** into a **production environment** so:
    - It can **serve predictions** to real users.

- Example:
  - Task: **Email spam detection**.
  - Train a spam classifier on a local machine.
  - To use it in Gmail, you must:
    - Deploy the model so Gmail’s infrastructure can call it to classify emails.
- Deployment means:
  - Make your **local model available “online”**:
    - For many users concurrently.
    - Integrated with actual applications.

### 6.2 Life Cycle / Loop in Production

- Simplified process:
  1. Collect data.
  2. Train model.
  3. Deploy model.
  4. Model used in production.
  5. New data or new needs appear.
  6. Go back to collecting data or changing the model.
  7. Re-train.
  8. Re-deploy.
  9. Repeat indefinitely.

- **Two primary reasons to go back in the loop**:
  1. **Model changes**:
     - Algorithm changes:
       - Example: From Logistic Regression to Naive Bayes.
       - Need to retrain and redeploy.
  2. **Data changes / new data arrival**:
     - Example: Spam attackers change strategies.
     - Old model no longer captures new patterns.
     - Need to collect new data, retrain, redeploy.

- Conclusion:
  - Production ML is a **never-ending loop**:
    - Continuous data collection.
    - Continuous training.
    - Continuous deployment.
    - Continuous monitoring.

### 6.3 Example: Model Performance Decay

- **Fraud detection example**:
  - A model is trained and deployed to detect fraud.
  - Over time, performance degrades:
    - Fraudsters **change their patterns**.
  - Need to:
    - Re-collect data.
    - Retrain the model.
    - Redeploy the updated model.
  - This **decay–retrain–redeploy cycle** may happen repeatedly.

### 6.4 Other Reasons to Restart or Reformulate

- **Reformulate problem**:
  - When it is difficult to collect enough data under the current formulation.
  - Might redefine the task for better feasibility.

- **Violation of assumptions**:
  - During training you assume certain:
    - Input data ranges.
    - Distributions.
    - Types, etc.
  - In production, if input data violates these assumptions, you may need:
    - New preprocessing.
    - New data collection.
    - New model.

- **Business objective changes**:
  - If business goals change:
    - The old model might no longer be aligned.
  - Need to restart the ML lifecycle.

- Summary:
  - ML in production is:
    - **Data affects output system**.
    - Hard to make reliably robust when:
      - Continuously deploying.
      - Retraining.
      - Handling new data & drift.

---

## 7. What is MLOps?

### 7.1 Definition

- **MLOps**:
  - A **set of practices** (not a single library or tool).
  - Aims to:
    - **Deploy** and **maintain** ML models in production:
      - **Reliably**.
      - **Efficiently**.
  - Handles:
    - Retraining when data changes.
    - Handling assumption violations.
    - Ensuring overall reliability at **large scale**.

### 7.2 Relationship to DevOps

- MLOps is:
  - An **extension of DevOps** methodology.
  - It includes **ML and data science assets** as **first-class citizens** in the DevOps ecosystem:
    - Datasets.
    - Models.
    - Features.
    - Metrics logs.
    - Pipelines.

### 7.3 City Analogy

- Analogy:
  - You are asked to **build a beautiful city**.
  - Building **only one beautiful building** is **not enough**.
    - It needs:
      - Electrical connectivity.
      - Maintenance plan.
      - Security systems.
      - Roads & railways connectivity.
  - The single building = **the ML model**.
  - The city infrastructure = **MLOps (full system)**:
    - Integration.
    - Monitoring.
    - Security.
    - Reliability.
    - Scalability.

- Companies want:
  - **“Standalone cities”**, not just individual **buildings**.
- Many job seekers fail because:
  - They focus only on building the **model**.
  - They neglect the **system-level MLOps**.
- MLOps = a way to **build the full city** around your model.

---

## 8. Challenges After Deployment

“The trouble begins after deployment.”

### 8.1 Latency

- **Latency definition**:
  - Time taken for a system/website to respond or load.
- Statistic:
  - **53%** of visitors **abandon** a **mobile site** if it takes **more than 3 seconds** to load.
- Implication for ML models:
  - If you deploy a **huge model** (e.g., a 120B parameter model):
    - It’s unlikely to respond within 3 seconds.
  - High latency:
    - Reduces user engagement.
    - Hurts brand interaction.
    - Lowers product adoption.

### 8.2 Fairness

- Example:
  - Microsoft created a **Twitter bot** that learns from user interactions.
  - It quickly became:
    - Extremely **racist**.
    - Supportive of **bad ideologies**.
  - Result:
    - Microsoft had to **take it down within hours**.
  - Lesson:
    - Post-deployment, models can:
      - Learn harmful behavior.
      - Require retraining/restricting or even removal.

### 8.3 Explainability & Auditability

- Challenges:
  - Difficult to explain **why** a model made a particular prediction.
  - Hard to assess whether predictions are **trustworthy**.
- Regulatory angle:
  - EU and other authorities are introducing **rules and guidelines**:
    - For AI fairness.
    - For explainability.
    - For auditability.

### 8.4 Deployment is Painfully Slow

- Survey:
  - Data scientists were asked:
    - “How much of your time do you spend deploying ML models?”
  - Findings:
    - **36%** spend **¼ to ½ of their time** deploying ML models.
    - **20%** spend **½ to ¾ of their time**.
    - **7%** spend **more than ¾** of their time.
  - Overall:
    - Deployment is **very slow** and **time-consuming**.

- Instructor’s personal anecdote:
  - Built:
    - Complete ML model + data preprocessing in **2 days** (~4 hours per day).
  - Spent:
    - **An entire week** on deployment alone.
  - Emphasizes:
    - Deployment complexity is often **underestimated**.

---

## 9. Model-Centric vs Data-Centric Approaches

### 9.1 Model-Centric

- Approach:
  - Fix the **data**.
  - Iteratively improve **models** / code:
    - Tune hyperparameters.
    - Try different architectures.
  - Expect performance improvements by constant **model-side tweaks**.

- Reality:
  - Most industry work has historically been:
    - **Model-centric**.

### 9.2 Data-Centric

- Approach:
  - Fix the **model** (keep architecture constant).
  - Continuously **improve data**:
    - Better quality labels.
    - More representative samples.
    - Cleaning noise.
- Recommendation:
  - Instructor encourages learners to:
    - Focus **more on data** than only on model tweaking.

- Reference:
  - **Andrew Ng**:
    - Known for advocating **data-centric AI**.
    - Instructor heard this directly in one of Andrew’s webinars and sees it daily in work as a data scientist.

---

## 10. End-to-End MLOps Process Overview

### 10.1 Start with Business Problem

- **First question**:
  - *“What is the business problem we want to solve?”*
- Don’t start by asking:
  - “Which ML model should we use?”
- Instead:
  - Understand:
    - Business needs.
    - Costs.
    - ROI.

### 10.2 Example: Retail Sales Forecasting

- Problem scenario:
  - A retail company struggles with:
    - **Overstock**:
      - Too much inventory.
      - Wastes resources.
      - Leads to possible write-offs of unsold goods.
    - **Understock**:
      - Too little inventory.
      - Causes missed sales.
      - Leads to unsatisfied customers.

- **Cost of wrong predictions**:
  - Overstock:
    - Resource wastage.
  - Understock:
    - Revenue loss & customer dissatisfaction.
  - Both have **high costs**.

- Goal:
  - Improve **sales forecasting** to minimize under/over-stock.

### 10.3 Decomposing Sales Forecasting Process

Steps of a **sales forecasting process**:

1. **Data Gathering**:
   - Collect needed data (historical sales, etc.).
2. **Historical Sales Analysis**:
   - Analyze past sales data.
3. **Market Trend Analysis**:
   - Study market behavior & external trends.
4. **Actual Forecasting**:
   - Predict future sales quantities.

- Where to use ML?
  - ML is best applied to **Actual Forecasting**:
    - Uses:
      - Past sales data.
      - Market trends.
    - Produces:
      - Better forecasts than traditional methods.

- Evaluate ROI:
  - Measure:
    - Decrease in wastage (from reduced overstock).
    - Decrease in missed sales (from reduced understock).
  - If the **benefit > cost** of building and maintaining ML solution:
    - Prioritize building the ML forecasting system.

### 10.4 Cost Considerations

- Costs include:
  - Development.
  - Deployment.
  - Maintenance.
  - Data acquisition and storage.
  - Monitoring & retraining.
  - Human involvement in labeling or supervision.

---

## 11. Machine Learning Canvas (Project Structuring)

A structured framework for designing ML solutions:

### 11.1 Value Proposition

- Define:
  - The **problem**.
  - Its **importance**.
  - The **end users**.
- Questions:
  - Who will use this product/service?
  - What value does it provide?
  - How important is it to solve now?

- Example template:
  - *For [target customer] who needs [need], our [product/service] is a [product category] that [benefit].*

### 11.2 Data Sources

- Identify potential data sources:
  - Internal databases.
  - APIs.
  - Open datasets.
- Consider **hidden costs**:
  - Data storage.
  - External data purchase.
  - ETL infrastructure.

### 11.3 Prediction Task

- Clarify:
  - Is it **supervised** / **unsupervised** / **anomaly detection**?
  - Problem type:
    - Classification.
    - Regression.
    - Ranking, etc.
  - Input and output format.
  - Expected model complexity.

### 11.4 Feature Engineering

- Collaborate with **domain experts**:
  - E.g., in healthcare:
    - Need doctors (MBBS) to help interpret signals.
  - Extract meaningful features from raw data.

### 11.5 Offline Evaluation

- Set up **evaluation metrics**:
  - Before deployment:
    - E.g., accuracy, F1, RMSE, AUC, etc.
- Validate:
  - Model performance on validation/test sets.
  - Ensure acceptable error levels.

### 11.6 Pre-Deployment

- Use the model yourself (internal testing).
- Understand:
  - Types of prediction errors.
  - Business cost of those errors.
- Examine:
  - How end-users will interact with predictions.
  - If human-in-the-loop is required.
  - Any hidden costs (e.g., manual review).

### 11.7 Continuous Data Collection

- Collect:
  - New data to prevent model degradation.
- Consider costs:
  - Data collection.
  - Human labeling.
- Plan:
  - Frequency of model retraining.
  - Associated infrastructure changes.

### 11.8 Monitoring

- Define:
  - Metrics to monitor:
    - Data drift.
    - Performance drift.
    - Latency.
    - Error rates.
- Identify:
  - When AI/ML may **not** be the best solution:
    - Some sub-tasks can be solved without ML (cheaper & simpler).

---

## 12. Core Artifacts & Phases in ML Software Development

Three **main artifacts**:

1. **Data**
2. **Model**
3. **Code**

Three **main engineering phases**:

1. **Data Engineering**
2. **Model Engineering**
3. **Code (Application) Engineering**

### 12.1 Data Engineering Phase

- Tasks:
  - Data ingestion.
  - Data exploration and validation.
  - Data cleaning and formatting.
  - Data labeling (for supervised learning).
  - Splitting into:
    - Train set.
    - Validation set.
    - Test set.

- Typical pipeline:
  1. Ingest data.
  2. Explore & validate data.
  3. Clean & format.
  4. Label (if needed).
  5. Split into train/validation/test.

### 12.2 Model Engineering Phase

- Core tasks:
  - Write and execute ML algorithms.
  - Train models.
  - Evaluate models.
  - Validate with pre-deployment tests.
  - Test against unseen test sets.
  - Package models for later use (e.g., `.pkl`).

- Typical pipeline:
  1. Train model.
  2. Evaluate model.
  3. Validate model pre-deployment.
  4. Test on test set.
  5. Package model.

### 12.3 Code Engineering Phase (Serving & Monitoring)

- Tasks:
  - Deploy model to production environment.
  - Serve model as:
    - API endpoint.
    - Batch system.
    - Streaming system, etc.
  - Monitor:
    - Predictions.
    - Performance.
  - Log:
    - Inputs.
    - Outputs.
    - Errors.

---

## 13. Introduction to ZenML

### 13.1 Why ZenML

- ZenML:
  - **Open-source** MLOps framework.
  - Used for building **full-stack MLOps applications**.
- Instructor’s experience:
  - Worked **6–7 months** on ZenML with the **core team**.
  - Describes ZenML as:
    - **Super simple to use**.
- Other options:
  - Many **other orchestrators** exist.
  - Instructor chooses ZenML because:
    - Easiest & powerful for teaching.
  - Also:
    - Strong ZenML **community** for support.

### 13.2 Role of Pipelines & Steps in ZenML

- ZenML uses a **pipeline-based approach**:
  - Organizes ML workflows as **pipelines** and **steps**.
- Benefits:
  - Easy to **rerun entire workflows** (not just model).
  - Enables:
    - **Reproducibility**.
    - **Traceability** (tracking all pipeline runs).
    - **Model comparison** across different versions.
  - Facilitates:
    - Automation of retraining and redeployment.
    - CI/CD workflows.

### 13.3 Movie Production Analogy for Pipelines

- Analogy:
  - A movie production process:  
    - Script writing.
    - Casting.
    - Filming.
    - Editing.
    - Distribution.
  - Dependencies:
    - Casting depends on script.
    - Filming depends on casting.
    - Editing depends on filming.
    - Distribution depends on editing.

- Similarly:
  - In ZenML:
    - A **pipeline** = complete ML workflow.
    - **Steps**:
      - Data preparation.
      - Feature engineering.
      - Model training.
      - Model evaluation.
      - Model deployment.
    - Each step can depend on outputs of previous steps.

### 13.4 Simple ZenML Example Steps

- Example of steps:
  - `prepare_data` (load data).
  - `train_model`.
  - `evaluate_model`.
  - `deploy_model`.

- Each function:
  - Decorated with `@step`.
- Combined with a `@pipeline`:
  - Chain them in logical order.

---

## 14. ZenML Setup & Basic Pipeline Example (Digits Classification)

### 14.1 Environment Setup

- For local development:
  - Use **VS Code** or local Python.
  - Or use **Google Colab** for demonstration:
    - Need an **ngrok** account to view ZenML UI from Colab.
- Install dependencies:
  - `zenml` & `zenml-server`.
  - `scikit-learn`.
  - `pyparsing`.
  - Other basic libs.

- Initialize ZenML repository:
  - In current directory:
    ```bash
    zenml init
    ```
  - Creates:
    - `.zen/` folder.
  - Sets up:
    - Local ZenML workspace.

### 14.2 Example Task: Handwritten Digit Recognition

- Use **scikit-learn** dataset:
  - `load_digits` dataset (images labeled `0–9`).
- Steps (Vanilla scikit-learn):
  1. Load digits.
  2. Preprocess/reshape data.
  3. Train-test split.
  4. Train `SVC` (Support Vector Classifier).
  5. Evaluate accuracy.

- This is used as a **simple example**:
  - To show how to convert simple training into a ZenML pipeline.
  - Not a demonstration of advanced ML techniques.

### 14.3 Implementation in ZenML

#### 14.3.1 Ingest / Import Step

- Decorated with `@step`.
- Returns:
  - `X_train`, `X_test`, `y_train`, `y_test`:
    - As `np.ndarray` types with type hints (`Annotated` or direct hints).

#### 14.3.2 Train Step

- `@step`
- Inputs:
  - `X_train` (np.ndarray).
  - `y_train` (np.ndarray).
- Returns:
  - A **classifier**:
    - Type-hinted as `ClassifierMixin` from `sklearn.base`.
    - Could be `SVC` or any classifier.

#### 14.3.3 Evaluate Step

- `@step`
- Inputs:
  - `X_test`
  - `y_test`
  - `model` (ClassifierMixin).
- Returns:
  - A **float**: accuracy.

#### 14.3.4 Pipeline Assembly

- `@pipeline`
- Compose steps:
  1. Call `importer()` → outputs `X_train`, etc.
  2. Pass `X_train`, `y_train` to `svc_trainer()`.
  3. Pass `X_test`, `y_test`, trained model to `evaluator()`.

- Running:
  ```python
  digits_pipeline = digits_pipeline()
  digits_pipeline.run()
  ```

### 14.4 ZenML Dashboard

- Start ZenML server:
  ```bash
  zenml up
  ```
- Open the provided URL:
  - Default username: `default`.
- In UI:
  - View pipelines.
  - View each step.
  - See:
    - Artifacts (stored outputs like DataFrames).
    - Logs.
    - Runtime.
  - Each pipeline run is versioned (e.g., version 1, version 2, etc).

### 14.5 Caching in ZenML

- ZenML can **cache step outputs**:
  - If nothing changes in:
    - The **input data**.
    - The **step code & configuration**.
  - ZenML **reuses** previous step outputs.
- Example behavior:
  - `using cached version of ingest_df`.
  - `using cached version of clean_df`.
- **Enable/disable caching**:
  - At pipeline decorator:
    ```python
    @pipeline(enable_cache=True)
    ```
  - If `enable_cache=False`, ZenML re-runs all steps, ignoring caches.

- Benefit:
  - Huge time savings when:
    - Data has not changed.
    - Only later steps or downstream tasks are being modified.

---

## 15. Full Project: Customer Satisfaction Prediction with ZenML & MLflow

### 15.1 Dataset Introduction

- Dataset:
  - **Customer data** from an e-commerce context.
- Raw datasets include:
  - `customers` dataset:
    - `customer_id`
    - `customer_unique_id`
    - `customer_city`
    - `customer_state`
  - `geolocation` dataset.
  - `items` dataset.
  - Others (orders, reviews, etc).

- Custom dataset:
  - Instructor created a **combined dataset** merging multiple sources.
  - Final dataset includes:
    - Many features.
    - A target variable: **`review_score`**.
      - Satisfaction score in range **1–5**.
  - Unused features:
    - Example: Review comments text column (later dropped for simplicity).

- Data view:
  - In Excel:
    - Columns:
      - `order_id`
      - `customer_id`
      - `order_status`
      - `order_purchase_timestamp`
      - `order_approved_at`
      - ... many more
      - `review_score` as target.

- **Note**:
  - For the course project:
    - Many features are intentionally **dropped** to:
      - Keep the project simpler.
      - Focus on MLOps rather than advanced feature engineering.

### 15.2 Directory & Environment Setup

- Use **virtual environment**:
  - Example:
    - `customer_satisfaction` virtualenv.
  - Tools:
    - `pyenv` (instructor’s choice).
    - Or `conda`, `venv`, etc.

- Why?
  - Avoid dependency conflicts across projects.
  - Containerize dependencies in a single isolated environment.

- Recommended:
  - If unfamiliar with virtual environments:
    - Refer to resources linked in GitHub repo (before this section).

- Required installations:
  - `zenml`
  - `zenml-server`
  - Additional libs via `requirements.txt`:
    - E.g.: `xgboost`, `catboost`, `lightgbm` (for extended modeling).
    - Even though advanced models might not be deeply taught here, they are installed for completeness.

- `requirements.txt` example:
  - Contains all necessary package versions.

### 15.3 ZenML Initialization & Folders

- Run:
  ```bash
  zenml init
  ```
  - Creates `.zen/` folder.

- If ZenML CLI warns about version mismatch:
  - Consider:
    - Downgrading ZenML or upgrading server.
  - It’s good practice to resolve warnings to avoid unexpected behavior.

- Folder structure:
  - `data/`:
    - Contains dataset files (`.csv` or future DB connectors).
  - `src/`:
    - Contains source code (data cleaning, modeling, etc.).
  - `pipelines/`:
    - Contains pipeline definitions.
  - `saved_models/`:
    - (Optionally) for storing saved model objects.
  - `steps/`:
    - Contains step definitions (ingest, clean, train, evaluate, etc.).
  - `__init__.py`
  - `requirements.txt`
  - `run_pipeline.py`:
    - Script to run the main training pipeline.

---

## 16. Implementing Steps with ZenML

### 16.1 Step 1 – Ingest Data (`steps/ingest_data.py`)

- Imports:
  - `logging`
  - `pandas as pd`
  - `from zenml import step`

- Class `IngestData`:
  - Constructor:
    - Accepts `data_path`.
  - `get_data()`:
    - Reads CSV using `pd.read_csv(self.data_path)`.

- Step function: `@step def ingest_df(data_path: str) -> pd.DataFrame:`
  - Docstring:
    - Description: Ingests data from given path.
    - Args: `data_path` – path to dataset.
    - Returns: `pd.DataFrame`.
  - Implementation:
    - Try:
      - Instantiate `IngestData`.
      - Call `.get_data()`.
      - Return dataframe.
    - Except:
      - Log error and raise.

- Good practices:
  - Use proper docstrings (`Args`, `Returns`).
  - Use try/except for robust step error logging.

### 16.2 Step 2 – Clean Data (`src/data_cleaning.py` & `steps/clean_data.py`)

#### 16.2.1 Strategy Pattern for Data Handling

- Uses **Strategy Pattern** with an abstract base class.

- Imports:
  - `logging`
  - `from abc import ABC, abstractmethod`
  - `from typing import Union`
  - `pandas as pd`
  - `from sklearn.model_selection import train_test_split`
  - `numpy as np`

##### Abstract Class: `DataStrategy` (ABC)

- Method:
  - `handle_data(self, df: pd.DataFrame) -> Union[pd.DataFrame, pd.Series]`
    - To be implemented by concrete strategies.

##### Strategy 1: `DataPreprocessStrategy` (for cleaning)

- Inherits: `DataStrategy`.

- `handle_data`:
  - Steps:
    1. **Drop columns** not needed for this simplified project (predefined list).
    2. **Fill null values**:
       - E.g., certain columns filled with median values.
       - `review_comment_message` column:
         - Fill `NaN` with `"no_review"`.
    3. `data = data.select_dtypes(include=[np.number])`:
       - Only keep **numeric** features.
       - Drops all categorical columns to avoid extra encoding complexity.
    4. Drop more columns:
       - E.g., `customer_zip_prefix`, `order_item_id`, etc.
       - Not because they are unimportant in general, but:
         - To **simplify** the teaching project.
    5. Return processed `data`.

- Exception handling:
  - Logs any errors and re-raises.

##### Strategy 2: `DataDivideStrategy` (for splitting data)

- Inherits: `DataStrategy`.

- `handle_data(df: pd.DataFrame)`:
  - Splits:
    - `X` = all columns except target (`review_score`).
    - `y` = target (`review_score`).
  - Uses `train_test_split`:
    - `test_size=0.2`
    - `random_state=42`
  - Converts to:
    - `X_train`, `X_test` as `pd.DataFrame`.
    - `y_train`, `y_test` as `pd.Series`.
  - Returns these four.

#### 16.2.2 Class `DataCleaning`

- Purpose:
  - Uses strategies for modular desig n.

- Constructor:
  - `__init__(self, data: pd.DataFrame, strategy: DataStrategy)`
  - Stores `strategy`.

- `handle_data()`:
  - Calls:
    - `return self.strategy.handle_data(self.data)`

- Example usage:
  ```python
  data = pd.read_csv("data.csv")
  cleaning = DataCleaning(data, DataPreprocessStrategy())
  processed = cleaning.handle_data()

  divider = DataCleaning(processed, DataDivideStrategy())
  X_train, X_test, y_train, y_test = divider.handle_data()
  ```

#### 16.2.3 Clean Data Step (`steps/clean_data.py`)

- Step: `@step def clean_df(df: pd.DataFrame) -> Tuple[...]`
- Return type using `Annotated` & `Tuple`:
  - `X_train: pd.DataFrame`
  - `X_test: pd.DataFrame`
  - `y_train: pd.Series`
  - `y_test: pd.Series`

- Implementation:
  - Import:
    - `DataCleaning`
    - `DataPreprocessStrategy`
    - `DataDivideStrategy`
  - Process:
    1. `preprocess_strategy = DataPreprocessStrategy()`
    2. `cleaning = DataCleaning(df, preprocess_strategy)`
    3. `processed_data = cleaning.handle_data()`
    4. `divide_strategy = DataDivideStrategy()`
    5. `divider = DataCleaning(processed_data, divide_strategy)`
    6. `X_train, X_test, y_train, y_test = divider.handle_data()`
  - Return:
    - All four.

- Docstring in step:
  - Describes:
    - Cleans data.
    - Splits into train/test.
  - Documents:
    - Args: `raw_data`.
    - Returns: training/test data and labels.

### 16.3 Step 3 – Model Development (`src/model_dev.py` & `steps/model_train.py`)

#### 16.3.1 Abstract Model Class

- Abstract base: `Model(ABC)`.

- Abstract method:
  - `train(self, X_train, y_train)`.

#### 16.3.2 Concrete Model: `LinearRegressionModel`

- Imports:
  - `from sklearn.linear_model import LinearRegression`.

- `train`:
  - Creates `LinearRegression` object.
  - Fits on:
    - `X_train`
    - `y_train`
  - Returns trained model.

- Used for demonstration:
  - Simple **regression** to predict `review_score`.
  - Not meant to be the best possible model.

#### 16.3.3 Model Config (`steps/config.py`)

- Class: `ModelNameConfig(BaseParameters)` (from `zenml.steps`).
- Contains:
  - `model_name`:
    - For selecting which model to use.
    - E.g., `"linear_regression"`.

#### 16.3.4 Train Step (`steps/model_train.py`)

- Imports:
  - `from src.model_dev import LinearRegressionModel`
  - `from .config import ModelNameConfig`
  - `from sklearn.base import RegressorMixin`

- Step signature:
  ```python
  @step
  def train_model(
      X_train: pd.DataFrame,
      X_test: pd.DataFrame,  # though X_test is not used for training
      y_train: pd.Series,
      y_test: pd.Series,
      config: ModelNameConfig
  ) -> RegressorMixin:
  ```

- Logic:
  - Checks `config.model_name`:
    - If `"linear_regression"`:
      - Create `LinearRegressionModel`.
      - Call `.train(X_train, y_train)`.
      - Return trained model.
    - Else:
      - Raise `ValueError` (e.g., unsupported model).
  - Wrap in try/except:
    - Logs errors with `logging`.
    - Re-raises on failure.

- Extensibility:
  - Can add more models:
    - `RandomForestModel`, `XGBoostModel`, etc.
  - Only change:
    - `if config.model_name == "random_forest":` etc.

### 16.4 Step 4 – Evaluation (`src/evaluation.py` & `steps/evaluation.py`)

#### 16.4.1 Abstract Evaluation Strategy

- Class: `Evaluation(ABC)`.

- Abstract method:
  - `calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray) -> float`.

#### 16.4.2 Concrete Strategies

- All use scikit-learn:
  - `from sklearn.metrics import mean_squared_error, r2_score`.

1. **MSE (Mean Squared Error) Strategy**:
   - Class: `MSE(Evaluation)`.
   - `calculate_scores(y_true, y_pred)`:
     - `mse = mean_squared_error(y_true, y_pred)`
     - Returns `mse`.

2. **R2 Strategy**:
   - Class: `R2(Evaluation)` or `EvaluationR2` (naming from context).
   - `calculate_scores(y_true, y_pred)`:
     - `r2 = r2_score(y_true, y_pred)`
     - Returns `r2`.

3. **RMSE Strategy**:
   - Class: `RMSE(Evaluation)`.
   - `calculate_scores(y_true, y_pred)`:
     - `rmse = mean_squared_error(y_true, y_pred, squared=False)`
     - Returns `rmse`.

#### 16.4.3 Evaluation Step (`steps/evaluation.py`)

- Imports:
  - `MSE`, `RMSE`, `R2` strategies.
  - `RegressorMixin`.
  - `pandas`, `numpy`.
  - `Annotated`, `Tuple`.

- Step:
  ```python
  @step
  def evaluate_model(
      model: RegressorMixin,
      X_test: pd.DataFrame,
      y_test: pd.Series
  ) -> Tuple[Annotated[float, "r2_score"], Annotated[float, "rmse"]]:
  ```

- Logic:
  1. Predictions:
     - `predictions = model.predict(X_test)`
  2. Instantiate metrics:
     - `mse_cls = MSE()`
     - `r2_cls = R2()`
     - `rmse_cls = RMSE()`
  3. Compute:
     - `mse = mse_cls.calculate_scores(y_test, predictions)`
     - `r2_score_val = r2_cls.calculate_scores(y_test, predictions)`
     - `rmse_val = rmse_cls.calculate_scores(y_test, predictions)`
  4. Log metrics (later integrated with MLflow).
  5. Return:
     - `r2_score_val`, `rmse_val`.

- Wrapped in try/except for robust error logging.

---

## 17. Training Pipeline & Running It

### 17.1 Define Training Pipeline (`pipelines/training_pipeline.py`)

- Imports:
  - `from zenml import pipeline`
  - Steps:
    - `ingest_df`
    - `clean_df`
    - `train_model`
    - `evaluate_model`

- Pipeline:
  ```python
  @pipeline(enable_cache=True)
  def training_pipeline(data_path: str):
      df = ingest_df(data_path)
      X_train, X_test, y_train, y_test = clean_df(df)
      model = train_model(X_train, X_test, y_train, y_test, config=ModelNameConfig(model_name="linear_regression"))
      r2_score, rmse = evaluate_model(model, X_test, y_test)
  ```

### 17.2 Run Pipeline (`run_pipeline.py`)

- Imports:
  - `from pipelines.training_pipeline import training_pipeline`

- Script:
  ```python
  if __name__ == "__main__":
      data_path = "data/your_customer_data.csv"  # path to custom dataset
      training_pipeline(data_path=data_path)
  ```

- Run:
  ```bash
  python run_pipeline.py
  ```

- Typical issues resolved:
  - Install missing dependencies:
    - e.g., `pip install pandas`, `pip install scikit-learn`.
  - Fix step return types:
    - Ensure `clean_df` returns all four outputs, not `None`.
  - Typing with `Annotated` and `Tuple`.

### 17.3 View in ZenML Dashboard

- Start server:
  ```bash
  zenml up
  ```
- Open dashboard, login (`default`).
- Go to `Pipelines`:
  - View `train_pipeline`.
- For each run:
  - Steps:
    - `ingest_df`
    - `clean_df`
    - `train_model`
    - `evaluate_model`
  - Inspect:
    - Output artifacts (DataFrames, metrics).
    - Step logs.
    - Visualizations (histograms, summary stats where applicable).

---

## 18. MLflow Integration for Experiment Tracking

### 18.1 Why Experiment Tracking?

- Need to track:
  - Each run.
  - Which parameters were used.
  - Which metrics were achieved.
  - Which model corresponds to which run.

- Helps:
  - Compare:
    - Different hyperparameters.
    - Different feature sets.
  - Reproduce:
    - Past best models.

### 18.2 MLflow Integration Setup

- Install MLflow integration:
  ```bash
  zenml integration install mlflow
  ```
- There might be environment-specific issues:
  - Some macOS-specific errors.
  - Can require:
    - `zenml disconnect`
    - `zenml up`
    - Or environment restarts.

- Check stacks:
  ```bash
  zenml stack list
  ```
- A stack includes:
  - `orchestrator`
  - `artifact_store`
  - Optionally:
    - `mlflow_experiment_tracker`
    - `mlflow_model_deployer`

- Register MLflow experiment tracker:
  ```bash
  zenml experiment-tracker register mlflow_tracker --flavor=mlflow
  ```

- Register MLflow model deployer:
  ```bash
  zenml model-deployer register mlflow_custom --flavor=mlflow
  ```

- Register stack (example names, course uses similar pattern):
  ```bash
  zenml stack register customer_stack \
    -o default \
    -a default \
    -d mlflow_custom \
    -e mlflow_tracker
  ```

- Set stack:
  ```bash
  zenml stack set customer_stack
  ```

- Then, run pipeline using this stack.

### 18.3 Modifying Steps to Use MLflow

#### 18.3.1 Get Active Experiment Tracker in Train Step

- Imports:
  - `from zenml.client import Client`
  - `import mlflow`

- In `train_model` step:
  ```python
  client = Client()
  experiment_tracker = client.active_stack.experiment_tracker
  ```

- Decorator:
  ```python
  @step(experiment_tracker=experiment_tracker.name)
  def train_model(...):
      mlflow.sklearn.autolog()
      ...
  ```

- Using `mlflow.sklearn.autolog()`:
  - Automatically logs:
    - Model parameters.
    - Metrics.
    - Artifacts (model files).
    - Training details.

#### 18.3.2 Logging Metrics in Evaluation Step

- In `evaluate_model`:
  - Import:
    - `import mlflow`.
  - After computing `mse`, `r2`, `rmse`:
    ```python
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2_score", r2_score_val)
    mlflow.log_metric("rmse", rmse_val)
    ```

### 18.4 Viewing MLflow UI

- After running pipeline with MLflow:
  - To get MLflow tracking URI:
    - Use a small snippet from documentation:
      ```python
      from zenml.client import Client
      client = Client()
      print(client.active_stack.experiment_tracker.get_tracking_uri())
      ```
  - Then, in terminal:
    ```bash
    mlflow ui --backend-store-uri <printed_uri>
    ```
- Open MLflow UI in browser:
  - View:
    - Experiments.
    - Runs.
    - Parameters.
    - Metrics.
    - Artifacts (models saved as `mlflow` models).

- Example:
  - `MLflow` UI shows:
    - `mse`, `r2`, `rmse` recorded.
    - A serialized model artifact:
      - Can be used via MLflow’s `pyfunc` or `sklearn` flavors.

---

## 19. Deployment with MLflow Model Deployer & ZenML

### 19.1 Deployment Approach

- Use:
  - **MLflow Model Deployer** (local deployment).
- For cloud deployments (AWS/GCP):
  - Would prefer:
    - **Seldon Core** or other advanced tools (beyond this example).
- Here:
  - Focus on:
    - Local model deployment with MLflow.

### 19.2 Deployment & Inference Pipelines Overview

- Two key pipelines:

  1. **Continuous Deployment Pipeline**
     - Train model.
     - Evaluate.
     - Make **deployment decision** based on metric (e.g., R²).
     - Deploy (or skip) model using `MLflowModelDeployerStep`.

  2. **Inference Pipeline**
     - Load currently deployed model service.
     - Fetch input data dynamically (from dataset).
     - Send data to model service for predictions.

### 19.3 Deployment Pipeline Details (`pipelines/deployment_pipeline.py`)

#### 19.3.1 Imports

- `numpy as np`
- `pandas as pd`
- `from zenml import pipeline, step`
- `from zenml.config import DockerSettings`
- `from zenml.integrations.mlflow.steps import mlflow_model_deployer_step`
- `from src.data_cleaning import DataCleaning, DataPreprocessStrategy, DataDivideStrategy` (if needed)
- Steps:
  - `ingest_df`
  - `clean_df`
  - `train_model`
  - `evaluate_model`

#### 19.3.2 Docker Settings

- Configure pipeline-level Docker settings:
  ```python
  docker_settings = DockerSettings(required_integrations=["mlflow"])
  ```

- Use in `@pipeline`:
  ```python
  @pipeline(enable_cache=True, settings={"docker": docker_settings})
  def continuous_deployment_pipeline(minimum_accuracy: float, workers: int = 3, timeout: int = 60):
      ...
  ```

#### 19.3.3 Deployment Decision Step (`deployment_trigger`)

- Config:

  ```python
  from zenml.steps import BaseParameters

  class DeploymentTriggerConfig(BaseParameters):
      minimum_accuracy: float = 0.99  # example threshold
  ```

- Step:

  ```python
  @step
  def deployment_trigger(
      accuracy: float,
      config: DeploymentTriggerConfig
  ) -> bool:
      return accuracy >= config.minimum_accuracy
  ```

- Explanation:
  - If model’s **R² score** >= `minimum_accuracy`:
    - Deployment = `True`.
  - Else:
    - Deployment = `False`.

#### 19.3.4 Wiring Continuous Deployment Pipeline

- Inside `continuous_deployment_pipeline`:

  1. Ingest & clean:
     ```python
     df = ingest_df(data_path)
     X_train, X_test, y_train, y_test = clean_df(df)
     ```
  2. Train:
     ```python
     model = train_model(X_train, X_test, y_train, y_test, config=ModelNameConfig(...))
     ```
  3. Evaluate:
     ```python
     r2_score, rmse = evaluate_model(model, X_test, y_test)
     ```
  4. Deployment decision:
     ```python
     deploy_decision = deployment_trigger(r2_score, config=DeploymentTriggerConfig(minimum_accuracy=minimum_accuracy))
     ```
  5. MLflow Model Deployer Step:
     ```python
     mlflow_model_deployer_step(
        model=model,
        deploy_decision=deploy_decision,
        workers=workers,
        timeout=timeout
     )
     ```

- **Note**:
  - Step name must be consistent (e.g., `mlflow_model_deployer_step`).
  - If `deploy_decision` is `False`:
    - Step logs:
      - “Skipping model deployment because model quality does not match criteria.”

### 19.4 run_deployment.py – CLI to Orchestrate Pipelines

- Use `click` for CLI interface.

- Example pattern:

  ```python
  import click
  from pipelines.deployment_pipeline import continuous_deployment_pipeline, inference_pipeline

  @click.command()
  @click.option("--config", type=click.Choice(["deploy", "predict", "deploy_and_predict"]))
  @click.option("--min-accuracy", default=0.9, type=float)
  def run_deployment(config: str, min_accuracy: float):
      if config == "deploy":
          continuous_deployment_pipeline(minimum_accuracy=min_accuracy, workers=3, timeout=60)
      elif config == "predict":
          inference_pipeline(...)
      elif config == "deploy_and_predict":
          continuous_deployment_pipeline(...)
          inference_pipeline(...)
  ```

- Run from terminal:
  ```bash
  python run_deployment.py --config deploy --min-accuracy 0.5
  python run_deployment.py --config predict
  ```

### 19.5 Dealing With Deployment Errors

- Example errors encountered and resolved:

  - **Materializer not found**:
    - ZenML uses materializers to handle artifact types.
    - Warning:
      - “No materializer is registered for type LinearRegression; default pickle materializer used.”
    - Usually not fatal, but can require creating a custom materializer in more advanced use cases.

  - **Invalid settings**:
    - `@pipeline(settings={"DockerSettings": docker_settings})` is incorrect.
    - Correct usage:
      - `@pipeline(settings={"docker": docker_settings})`.

  - **Daemon not running** for MLflow deployer:
    - Could happen if:
      - Another old service is still in memory.
      - Stacks misconfigured.
    - Fix:
      - Delete / reset existing MLflow deployments or stacks.
      - Ensure correct stack is active.
      - Sometimes:
        - Restart machine.

  - **Deployment criteria not met**:
    - If `r2_score` is low:
      - Pipeline logs:
        - “Skipping model deployment because model quality does not match criteria.”
    - Quick fix for demonstration:
      - Lower `minimum_accuracy` threshold:
        - E.g., `0.5` or `0.0`.
      - Only for educational demonstration.

  - **Version mismatches**:
    - MLflow / scikit-learn:
      - Use `pip install --upgrade mlflow` or adjust `scikit-learn` version.

### 19.6 Loading Deployed Service – Prediction Service Loader Step

- Use `MLflowModelDeployer` to get running services.

- Step: `prediction_service_loader`

  ```python
  from typing import cast
  from zenml.client import Client
  from zenml.integrations.mlflow.model_deployers import MLFlowModelDeployer
  from zenml.integrations.mlflow.services import MLFlowDeploymentService

  @step(enable_cache=False)
  def prediction_service_loader(
      pipeline_name: str,
      pipeline_step_name: str,
      model_name: str = "model",
      running: bool = True,
  ) -> MLFlowDeploymentService:
      client = Client()
      mlflow_deployer = cast(
          MLFlowModelDeployer, client.active_stack.model_deployer
      )
      existing_services = mlflow_deployer.find_model_server(
          pipeline_name=pipeline_name,
          pipeline_step_name=pipeline_step_name,
          model_name=model_name,
          running=running
      )
      if not existing_services:
          raise RuntimeError(
              f"No MLflow deployment service found for pipeline {pipeline_name}, "
              f"step {pipeline_step_name}, model {model_name}"
          )
      service = existing_services[0]
      service.start(timeout=10)  # ensure service is running
      return service
  ```

### 19.7 Dynamic Data Importer & Predictor

#### 19.7.1 Data Import for Prediction (`dynamic_importer`)

- Step:
  ```python
  @step(enable_cache=False)
  def dynamic_importer() -> str:
      data = get_data_of_a_test()
      return data
  ```

- `get_data_of_a_test()` (in `src/utils/urls.py`):
  - Reads dataset.
  - Cleans using `DataPreprocessStrategy`.
  - Drops target column `review_score`.
  - Takes **first N rows** (e.g., 100).
  - Converts to JSON string:
    - `df.to_json(orient="records")`.
  - Returns JSON string.

#### 19.7.2 Predictor Step

- Step:
  ```python
  @step
  def predictor(
      service: MLFlowDeploymentService,
      data: str
  ) -> np.ndarray:
      import json
      import numpy as np
      import pandas as pd

      # ensure service is up
      service.start()

      # load JSON
      json_list = json.loads(data)
      df = pd.DataFrame(json_list)

      # convert to numpy
      arr = df.to_numpy()

      # get predictions via REST or native MLflow predict
      predictions = service.predict(arr)

      return predictions
  ```

- Can log:
  - Prediction stats:
    - Mean.
    - Std dev.

### 19.8 Inference Pipeline (`inference_pipeline`)

- Pipeline:

  ```python
  @pipeline(enable_cache=False, settings={"docker": docker_settings})
  def inference_pipeline(
      pipeline_name: str,
      pipeline_step_name: str,
  ):
      data = dynamic_importer()
      service = prediction_service_loader(
          pipeline_name=pipeline_name,
          pipeline_step_name=pipeline_step_name,
          model_name="model",
          running=True
      )
      predictions = predictor(service, data)
  ```

- Example usage:
  - Pipeline name:
    - `"continuous_deployment_pipeline"`
  - Step:
    - `"mlflow_model_deployer_step"`

- Running:
  - After `continuous_deployment_pipeline` successfully deploys:
    ```bash
    python run_deployment.py --config predict
    ```

- In ZenML UI:
  - View `inference_pipeline`:
    - See:
      - `dynamic_importer` output (test data).
      - `prediction_service_loader` output (service object).
      - `predictor` output:
        - Predictions.
        - Their stats (mean, std).

---

## 20. Streamlit Application for Single-Record Predictions

### 20.1 Purpose

- Allow user to:
  - Enter **single customer/order features** via UI.
  - Trigger prediction.
  - Use **already deployed MLflow service** via ZenML orchestration.

### 20.2 Streamlit App (`streamlit_app.py`)

- Imports:
  - `streamlit as st`
  - `pandas as pd`
  - `numpy as np`
  - The service loader functions:
    - `prediction_service_loader`
  - Config:
    - Pipeline name & step name.
    - Probably from `run_deployment.py`.

- Streamlit basic layout:
  - UI elements:
    - Input fields for each feature:
      - `feature_1`, `feature_2`, ... (representing numeric features used by the model).
    - `Predict` button.

- Logic:
  1. On load:
     - Load MLflow service using:
       - `prediction_service_loader(...)`.
  2. When user clicks **Predict**:
     - Create a single-row `pandas.DataFrame` from input fields.
     - Convert to numpy array.
     - Call:
       - `service.predict()` on this single-row.
     - Display:
       - Predicted `review_score`.

- Run:
  ```bash
  streamlit run streamlit_app.py
  ```

- Example behavior:
  - All features set to zero.
  - Predicted `review_score` ~ `4.22` (example value from instructor).
  - Confirms:
    - Deployed model is being used through MLflow service, not from local `joblib` load.

### 20.3 Integration with Pipelines

- The Streamlit app:
  - Uses:
    - The same **deployed MLflow service** as the inference pipeline.
  - Does not need:
    - To reload or retrain the model.
  - Connects:
    - To the **existing service** registered and started by `continuous_deployment_pipeline`.

---

## 21. Key Takeaways & Course Flow

- Core lessons from project:

  - **Code structuring**:
    - Use of:
      - Strategy pattern.
      - Separate steps.
      - Pipelines.
    - Readable & maintainable code.

  - **Importance of blueprinting**:
    - Start with:
      - High-level pipeline design.
      - Folder structure.
      - Class & step design.
    - Then implement details.

  - **MLOps essentials**:
    - Pipelines.
    - Steps.
    - Caching.
    - Experiment tracking (MLflow).
    - Deployment.
    - Inference.
    - Monitoring behavior in UI.

  - **Realistic complexity**:
    - In later projects:
      - More complex models.
      - More advanced data/feature handling.
      - Possibly DB-based ingestion (PostgreSQL, cloud DBs, etc.).
    - This first project:
      - Focuses on simplicity to clearly illustrate MLOps structure.

- Remainder of course:
  - Additional projects (e.g., **customer churn** or **customer channel** type tasks).
  - More advanced:
    - Tech stack variations.
    - Deployment in more complex environments.
    - Improved feature engineering.
    - Error handling patterns.

---

This Markdown document reorganizes and condenses the full lecture transcript and code walkthrough while **preserving every technical and conceptual detail** from the original text, including all examples, explanations, steps, tools, code behaviors, design choices, and error-handling discussions.