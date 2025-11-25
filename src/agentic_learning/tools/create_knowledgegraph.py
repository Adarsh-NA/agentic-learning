import os
import yaml
import asyncio
import subprocess
from pathlib import Path
from graphrag.config.load_config import load_config
import graphrag.api as api
from dotenv import load_dotenv
load_dotenv()
# ------------------------------
# Step 1: Initialize GraphRAG
# ------------------------------
def initialize_graphrag(root_folder: Path):
    """
    Runs 'graphrag init' to create prompts, settings.yaml, and folder structure.
    """
    if not root_folder.exists():
        root_folder.mkdir(parents=True)

    subprocess.run(
        ["graphrag", "init", "--root", str(root_folder)],
        check=True
    )
    print("✅ GraphRAG initialized.")


# ----------------------------------
# Step 2: Update settings.yaml
# ----------------------------------
import yaml
from pathlib import Path
import os

def update_settings_yaml(root_folder: Path, input_folder: Path, output_folder: Path):
    """Simplest safe updater for GraphRAG settings.yaml"""

    settings_file = root_folder / "settings.yaml"

    with open(settings_file, "r") as f:
        config = yaml.safe_load(f)

    # --- Update input folder ---
    if "input" in config:
        if "storage" in config["input"]:
            config["input"]["storage"]["base_dir"] = str(input_folder)
        else:
            config["input"]["storage"] = {"type": "file", "base_dir": str(input_folder)}

    # --- Update output folder ---
    if "output" in config:
        config["output"]["base_dir"] = str(output_folder)
    else:
        config["output"] = {"type": "file", "base_dir": str(output_folder)}

    # --- Update OpenAI models to lightweight ones (avoid rate limits) ---
    config["models"]["default_chat_model"]["model"] = "gpt-4o-mini"
    config["models"]["default_embedding_model"]["model"] = "text-embedding-3-small"

    # --- Set OpenAI API KEY ---
    openai_key = os.getenv("OPENAI_API_KEY", "")
    config["models"]["default_chat_model"]["api_key"] = openai_key
    config["models"]["default_embedding_model"]["api_key"] = openai_key

    # --- Reduce load to avoid rate limits ---
    config["models"]["default_chat_model"]["temperature"] = 0
    config["models"]["default_chat_model"]["max_tokens"] = 1500
    config["models"]["default_chat_model"]["concurrent_requests"] = 1
    config["models"]["default_chat_model"]["requests_per_minute"] = 1000
    config["models"]["default_chat_model"]["tokens_per_minute"] = 10000

    # Embedding model throttling
    config["models"]["default_embedding_model"]["concurrent_requests"] = 1
    config["models"]["default_embedding_model"]["requests_per_minute"] = 1000
    config["models"]["default_embedding_model"]["tokens_per_minute"] = 10000

    # --- Write back updated settings.yaml ---
    with open(settings_file, "w") as f:
        yaml.dump(config, f, sort_keys=False)

    print("✅ settings.yaml updated successfully")

# -------------------------------------------
# Step 3: Run Indexing using Python API
# -------------------------------------------
async def run_indexing(root_folder: Path):
    """
    Loads the updated settings.yaml and runs GraphRAG indexing.
    """
    config = load_config(root_folder)
    print("🚀 Running GraphRAG indexing...\n")

    result = await api.build_index(config=config)

    for wf in result:
        print(f"✔ Workflow: {wf.workflow} | Errors: {wf.errors}")

# ------------------------------------
# Main Function Orchestrator
# ------------------------------------
def build_graphrag_pipeline(input_folder, root_folder, output_folder):
    """
    Master function
    """
    input_folder = Path(input_folder).resolve()
    root_folder = Path(root_folder).resolve()
    output_folder = Path(output_folder).resolve()

    print(f"📥 Input Folder: {input_folder}")
    print(f"📂 Root Folder:  {root_folder}")
    print(f"📦 Output Folder:{output_folder}\n")

    initialize_graphrag(root_folder)
    update_settings_yaml(root_folder, input_folder, output_folder)
    asyncio.run(run_indexing(root_folder))

    print("\n🎉 Done! Artifacts stored in:", output_folder)


# ------------------------------------
# Run Script
# ------------------------------------

if __name__ == "__main__":

    input_dir = "/Users/adarshna/Codes/Jupyter/17_AgenticAI/CrewAI/EdTechAutomation/agentic_learning/src/agentic_learning/outputs/neo4j"
    root_dir = "/Users/adarshna/Codes/Jupyter/17_AgenticAI/CrewAI/EdTechAutomation/agentic_learning/src/agentic_learning/graphrag"
    output_dir = "/Users/adarshna/Codes/Jupyter/17_AgenticAI/CrewAI/EdTechAutomation/agentic_learning/src/agentic_learning/outputs/graphs"

    (build_graphrag_pipeline(input_dir, root_dir, output_dir))