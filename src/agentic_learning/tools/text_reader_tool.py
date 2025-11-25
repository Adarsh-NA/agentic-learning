import os
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class TextReaderInput(BaseModel):
    file_path: str = Field(
        ..., 
        description="The full path of the text file to read."
    )

class TextReaderTool(BaseTool):
    name: str = "text_reader_tool"
    description: str = (
        "Reads and returns the content of a text/markdown file. "
        "Provide the full file path using the key 'file_path'."
    )
    args_schema: Type[BaseModel] = TextReaderInput

    def _run(self, file_path: str) -> dict:
        try:
            # Validate file existence
            if not os.path.exists(file_path):
                return {
                    "success": False,
                    "content": None,
                    "error": f"File not found: {file_path}"
                }

            # Read file content
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            return {
                "success": True,
                "content": content,
                "message": "File read successfully."
            }

        except Exception as e:
            return {
                "success": False,
                "content": None,
                "error": str(e)
            }
