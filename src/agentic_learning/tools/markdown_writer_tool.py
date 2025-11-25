import os
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class MarkdownWriterInput(BaseModel):
    filename: str = Field(..., description="The filename (without extension) for the markdown file")
    markdowntext: str = Field(..., description="The markdown content to write into the file")

class MarkdownWriterTool(BaseTool):
    name: str = "markdown_writer_tool"
    description: str = (
        "Saves markdown content to a .md file. "
        "Provide two keys: filename and markdowntext for the markdown text. "
        "The file will be saved to the 'outputs' folder one level above this tool's directory."
    )
    args_schema: Type[BaseModel] = MarkdownWriterInput

    def _run(self, filename: str, markdowntext: str) -> dict:
        try:
            # Get folder one level above this file
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            output_dir = os.path.join(base_dir, "outputs")
            print(output_dir)
            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)

            filepath = os.path.join(output_dir, f"{filename}.md")

            # Write the markdown content
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdowntext)

            return {
                "success": True,
                "filepath": filepath,
                "message": "Markdown file saved successfully."
            }

        except Exception as e:
            return {
                "success": False,
                "filepath": None,
                "error": str(e)
            }
