#!/usr/bin/env python
from random import randint
import json
from pydantic import BaseModel
import sys
from crewai.flow import Flow, listen, start
from datetime import datetime
from agentic_learning.crews.initialiser_crew.initialiser_crew import InitialiserCrew
from agentic_learning.crews.subject_research_crew.subject_research_crew import SubjectResearchCrew
from agentic_learning.crews.blooms_summary_crew.blooms_summary_crew import BloomsSummaryCrew
from agentic_learning.tools.text_chunker_tool import chunk_transcripts
from agentic_learning.crews.ppt_gen_crew.ppt_gen_crew import PptGenCrew
from crewai.flow.persistence import persist
import os
from pathlib import Path

# Store in project directory
project_root = Path(__file__).parent
storage_dir = project_root / "crewai_storage"

os.environ["CREWAI_STORAGE_DIR"] = str(storage_dir)


class AgenticLearningState(BaseModel):
    subject: str = ''
    duration: int = 1
    root_folder: str = ''
    primary_dir_path: str = ''
    transcript_path: str = ''
    transcripts_dir_path: str = ''
    toc_path: str = ''
    toc_dir_path: str = ''
    blooms_summary_dir_path: str = ''
    presentations_dir_path: str = ''

@persist()
class AgenticLearningFlow(Flow[AgenticLearningState]):

    @start()
    def initialize_agantic_learning(self, crewai_trigger_payload: dict = None):
        print('Started initialization')
        self.state.subject = sys.argv[1]
        self.state.duration = int(sys.argv[2])
        self.state.root_folder = r"/Users/adarshna/Codes/Jupyter/17_AgenticAI/CrewAI/EdTechAutomation/agentic_learning/src/agentic_learning/outputs"

        result = (
            InitialiserCrew()
            .crew()
            .kickoff(inputs={
                "root_folder": self.state.root_folder,
                "subject": self.state.subject,
                "datetime_str": datetime.now().strftime("%Y%m%d%H%M%S")
            })
        )

        data = json.loads(result.raw)
        self.state.primary_dir_path = data['primary_dir_path']
        self.state.toc_dir_path = data['toc_dir_path']
        self.state.transcripts_dir_path = data['transcripts_dir_path']
        self.state.blooms_summary_dir_path = data['blooms_summary_dir_path']
        self.state.presentations_dir_path = data['presentations_dir_path']

    @listen(initialize_agantic_learning)
    def generate_toc_transcription(self, crewai_trigger_payload: dict = None):
        print(f"Generating TOC and Transcribing best videos on {self.state.subject}")
        result = (
            SubjectResearchCrew()
            .crew()
            .kickoff(inputs={
                "subject": self.state.subject,
                "duration": self.state.duration,
                "toc_dir_path": self.state.toc_dir_path,
                "transcripts_dir_path": self.state.transcripts_dir_path
            })
        )

        print("-------------------------------------------------------------")
        print(result.tasks_output[-2].raw)
        print("-------------------------------------------------------------")

        self.state.transcript_path = json.loads(result.raw)["transcript_path"]
        self.state.toc_path = f"{self.state.toc_dir_path}/{self.state.subject}__{self.state.duration}hrs__toc.md"
    
    @listen(generate_toc_transcription)
    def ppt_gen_crew(self, crewai_trigger_payload: dict = None):
        print(f"Generating ppt on {self.state.subject}")
        result = (
            PptGenCrew()
            .crew()
            .kickoff(inputs={
                "subject": self.state.subject,
                "duration": self.state.duration,
                "toc_path": self.state.toc_path,
                "presentations_dir_path": self.state.presentations_dir_path
            })
        )


    @listen(ppt_gen_crew)
    def generate_blooms_summary(self, crewai_trigger_payload: dict = None):
        print("Generating Blooms Summary")
        blooms_summary_results = []

        for chunk in chunk_transcripts(json_file_path=self.state.transcript_path):
            chunk.update({"blooms_summary_dir_path": self.state.blooms_summary_dir_path})
            blooms_summary_results.append(
                BloomsSummaryCrew().crew().kickoff(inputs=chunk)
            )

        print("Generated Blooms Summary Result", blooms_summary_results)

    @listen(generate_blooms_summary)
    def succesfulcompletion(self):
        print("Flow completed successfully")


if __name__ == "__main__":
    # debug_blooms_only = "--debug-blooms" in sys.argv
    # debug_ppt_only = "--debug-ppt" in sys.argv
    # debug_toc_only = "--debug-toc" in sys.argv  # NEW FLAG

    flow = AgenticLearningFlow()
    flow.state.subject = sys.argv[2] if len(sys.argv) > 2 else "Python"
    flow.state.duration = int(sys.argv[3]) if len(sys.argv) > 3 else 4

    # if debug_toc_only:
    #     print("🔎 Debug Mode: Running ONLY TOC + Transcription generation")

    #     # Inject Subject & Duration from CLI for consistency
    #     flow.state.subject = sys.argv[2] if len(sys.argv) > 2 else "Python"
    #     flow.state.duration = int(sys.argv[3]) if len(sys.argv) > 3 else 4

    #     # Initialize folder structure
    #     flow.initialize_agantic_learning()

    #     # Execute only the TOC + transcript step
    #     flow.generate_toc_transcription()

    #     print("\n--- Debug Output ---")
    #     print(f"TOC: {flow.state.toc_path}")
    #     print(f"Transcripts: {flow.state.transcript_path}")
    #     print("-------------------")

    # elif debug_blooms_only:
    #     # ✂️ (unchanged)
    #     flow.state.transcript_path = (
    #         "/Users/.../transcripts/LLM Finetuning_transcripts.json"
    #     )
    #     flow.state.blooms_summary_dir_path = (
    #         "/Users/.../blooms_summary"
    #     )
    #     flow.generate_blooms_summary()

    # elif debug_ppt_only:
    #     # ✂️ (unchanged)
    #     flow.state.subject = "ML OPS"
    #     flow.state.duration = 8
    #     flow.state.toc_path = (
    #         "/Users/adarshna/Codes/Jupyter/17_AgenticAI/CrewAI/EdTechAutomation/agentic_learning/src/agentic_learning/outputs/ML_OPS_20251125070757/toc/ML OPS_toc.md"
    #     )
    #     flow.state.presentations_dir_path = (
    #         "/Users/adarshna/Codes/Jupyter/17_AgenticAI/CrewAI/EdTechAutomation/agentic_learning/src/agentic_learning/outputs/ML_OPS_20251125070757/presentations"
    #     )
    #     flow.ppt_gen_crew()

    # else:
        # Normal full flow
    flow.kickoff()
