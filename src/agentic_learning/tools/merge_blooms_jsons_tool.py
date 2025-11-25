from typing import Type, Optional, Dict, Any
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from pathlib import Path
import json
import glob

class MergeBloomsJsonInput(BaseModel):
    blooms_summary_dir_path: str = Field(..., description="Directory containing chunk JSON files")
    video_title: str = Field(..., description="Video title prefix used in file names")
    video_url: Optional[str] = Field(None, description="URL of the video")

class MergeResult(BaseModel):
    success: bool
    message: str
    final_output_path: Optional[str] = None
    markdown_output_path: Optional[str] = None
    merged_chunk_count: int = 0

class MergeBloomsJsonTool(BaseTool):
    name: str = "merge_bloom_outputs_tool"

    description: str = (
        "Reads multiple Bloom taxonomy chunk JSON files from blooms_summary_dir_path "
        "that match the pattern: video_title_*_*.json\n"
        "Merges them into a single JSON by combining fields. If the same field exists "
        "in multiple files, their values are appended. Saves the final JSON as: "
        "{blooms_summary_dir_path}/{video_title}_combined.json and also generates a Markdown version."
    )

    args_schema: Type[BaseModel] = MergeBloomsJsonInput

    def _run(self, blooms_summary_dir_path: str, video_title: str, video_url: Optional[str] = None) -> dict:
        try:
            base_dir = Path(blooms_summary_dir_path)
            base_dir.mkdir(parents=True, exist_ok=True)

            suffix_order = ["condensed", "understand", "remember", "analyze", "eval", "apply", "create"]

            files = []
            for suffix in suffix_order:
                matched_files = sorted(base_dir.glob(f"{video_title}_*{suffix}*.json"))
                files.extend(matched_files)

            if not files:
                return MergeResult(
                    success=False,
                    message="No chunk output files found to merge",
                    final_output_path=None,
                    markdown_output_path=None,
                    merged_chunk_count=0
                ).dict()

            merged_data: Dict[str, Any] = {
                "title": video_title,
                "url": video_url if video_url else ""
            }

            # Track if summary has been set
            summary_set = False

            for f in files:
                try:
                    with open(f, "r", encoding="utf-8") as infile:
                        data = json.load(infile)

                    # Summary field
                    if not summary_set:
                        summary = data.get("summary")
                        if summary:
                            merged_data["summary"] = summary
                            summary_set = True

                    # Merge other fields
                    for key, value in data.items():
                        if key in ["title", "url", "summary"]:
                            continue
                        if key not in merged_data:
                            merged_data[key] = value
                        else:
                            if isinstance(merged_data[key], str) and isinstance(value, str):
                                merged_data[key] += "\n" + value
                            elif isinstance(merged_data[key], list):
                                if isinstance(value, list):
                                    merged_data[key].extend(value)
                                else:
                                    merged_data[key].append(value)
                            else:
                                merged_data[key] = str(merged_data[key]) + "\n" + str(value)

                except Exception as e:
                    print(f"Failed to read {f}: {e}")
                    continue

            # Write merged JSON
            final_output_path = base_dir / f"{video_title}_combined.json"
            with open(final_output_path, "w", encoding="utf-8") as outfile:
                json.dump(merged_data, outfile, indent=2, ensure_ascii=False)

            # Generate Markdown from merged JSON
            markdown_output_path = base_dir / f"{video_title}_combined.md"
            with open(markdown_output_path, "w", encoding="utf-8") as md_file:
                md_file.write(f"# {merged_data.get('title', '')}\n\n")
                if merged_data.get("url"):
                    md_file.write(f"**URL:** {merged_data['url']}\n\n")
                if merged_data.get("summary"):
                    md_file.write(f"## Summary\n{merged_data['summary']}\n\n")

                for key, value in merged_data.items():
                    if key in ["title", "url", "summary"]:
                        continue
                    md_file.write(f"## {key.replace('_', ' ').title()}\n")
                    if isinstance(value, list):
                        for item in value:
                            md_file.write(f"- {item}\n")
                    else:
                        md_file.write(f"{value}\n")
                    md_file.write("\n")

            return MergeResult(
                success=True,
                message="Merged successfully and Markdown generated",
                final_output_path=str(final_output_path),
                markdown_output_path=str(markdown_output_path),
                merged_chunk_count=len(files)
            ).dict()

        except Exception as err:
            return MergeResult(
                success=False,
                message=str(err),
                final_output_path=None,
                markdown_output_path=None,
                merged_chunk_count=0
            ).dict()
