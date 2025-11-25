import subprocess
from typing import Optional

def query_graphrag(
    query: str,
    method: str = "global",
    root_path: str = r"/Users/adarshna/Codes/Jupyter/17_AgenticAI/CrewAI/EdTechAutomation/agentic_learning/src/agentic_learning/graphrag",
    timeout: Optional[int] = None,
    community_level: int = 2,
    dynamic_community_selection: bool = False
) -> str:
    """
    Run a GraphRAG query using the CLI.

    Args:
        query (str): Query string.
        method (str): global | local | drift (default: global).
        root_path (str): GraphRAG root folder path.
        timeout (int): Max seconds to wait.
        community_level (int): L2 community by default.
        dynamic_community_selection (bool): Enable dynamic global search.

    Returns:
        str: Output text from GraphRAG.
    """
    if community_level < 0:
        raise ValueError("community_level must be >= 0")

    # Build command
    command = [
        "graphrag", "query",
        "--root", root_path,
        "--method", method,
        "--query", query,
        "--community-level", str(community_level)
    ]

    if dynamic_community_selection:
        command.append("--dynamic-community-selection")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        # Raise if exit code != 0
        result.check_returncode()

        return result.stdout.strip()

    except subprocess.TimeoutExpired:
        raise TimeoutError(f"GraphRAG query timed out after {timeout} seconds.")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"GraphRAG query failed.\n"
            f"Command: {' '.join(e.cmd)}\n"
            f"STDERR: {e.stderr}"
        )

print(query_graphrag("Give 10 MCQs on Neo4j",method="global"))
