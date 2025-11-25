import os
import re
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class FolderStructureInput(BaseModel):
    root_folder: str = Field(..., description="Absolute path of the root directory")
    subject: str = Field(..., description="Name of the subject (will be sanitized)")
    datetime_str: str = Field(..., description="DateTime string (will be sanitized)")


class FolderStructureOutput(BaseModel):
    success: bool
    message: str
    root_dir_path: str | None = None
    primary_dir_path: str | None = None
    toc_dir_path: str | None = None
    transcripts_dir_path: str | None = None
    blooms_summary_dir_path: str | None = None
    presentations_dir_path: str | None = None


class FolderStructureTool(BaseTool):
    name: str = "folder_structure_creation_tool"
    description: str = (
        "Creates subject-based folder structure under the given root folder. "
        "Returns the full folder structure paths in a validated JSON format."
    )
    args_schema: Type[BaseModel] = FolderStructureInput

    def sanitize(self, value: str) -> str:
        """Replace spaces with underscores and remove illegal characters."""
        value = value.replace(" ", "_")
        value = re.sub(r"[^A-Za-z0-9_]", "", value)
        return value

    def _run(self, root_folder: str, subject: str, datetime_str: str) -> dict:
        try:
            subject_safe = self.sanitize(subject)
            datetime_safe = self.sanitize(datetime_str)

            primary = f"{subject_safe}_{datetime_safe}"
            primary_dir = os.path.join(root_folder, primary)

            toc_dir = os.path.join(primary_dir, f"toc")
            transcripts_dir = os.path.join(primary_dir, f"transcripts")
            blooms_dir = os.path.join(primary_dir, f"blooms_summary")
            presentations_dir = os.path.join(primary_dir, f"presentations")

            os.makedirs(toc_dir, exist_ok=True)
            os.makedirs(transcripts_dir, exist_ok=True)
            os.makedirs(blooms_dir, exist_ok=True)
            os.makedirs(presentations_dir, exist_ok=True)

            return FolderStructureOutput(
                success=True,
                message="Folder structure created successfully.",
                root_dir_path=root_folder,
                primary_dir_path=primary_dir,
                toc_dir_path=toc_dir,
                transcripts_dir_path=transcripts_dir,
                blooms_summary_dir_path=blooms_dir,
                presentations_dir_path=presentations_dir,
            ).model_dump()

        except Exception as e:
            return FolderStructureOutput(
                success=False,
                message=f"Error creating folders: {str(e)}",
                root_dir_path=root_folder
            ).model_dump()
