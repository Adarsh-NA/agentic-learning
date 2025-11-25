from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List, Dict, Any
from pydantic import BaseModel, Field
import re
import json
from dotenv import load_dotenv
load_dotenv()
from agentic_learning.tools.merge_blooms_jsons_tool import MergeBloomsJsonTool


# ------------------------------
# Sanitization function
# ------------------------------
def sanitize_json(raw_text: str, fallback_field="observations") -> dict:
    """
    Clean LLM output before passing to Pydantic.
    - Remove control characters (\x00-\x1F)
    - Escape backslashes
    - Remove trailing commas
    - Attempt JSON load, fallback to wrapping text in list under fallback_field
    """
    if not raw_text:
        return {}
    
    # Remove control characters
    cleaned = re.sub(r'[\x00-\x1F]+', '', raw_text)
    # Escape backslashes
    cleaned = cleaned.replace('\\', '\\\\')
    # Remove trailing commas
    cleaned = re.sub(r',(\s*[\]}])', r'\1', cleaned)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {fallback_field: [cleaned]}


# ------------------------------
# Safe Pydantic Models
# ------------------------------

class SafeUnderstandingOutput(BaseModel):
    key_terms: List[str] = Field(default_factory=list)
    definitions: List[str] = Field(default_factory=list)
    analogies: List[str] = Field(default_factory=list)
    reflection_questions: List[str] = Field(default_factory=list)

    @classmethod
    def model_validate_json(cls, raw_text):
        sanitized = sanitize_json(raw_text, fallback_field="key_terms")
        return super().model_validate(sanitized)


class SafeRememberOutput(BaseModel):
    mnemonics: List[str] = Field(default_factory=list)
    flashcards: List[str] = Field(default_factory=list)
    story: str = Field(default="")
    acronyms: List[str] = Field(default_factory=list)

    @classmethod
    def model_validate_json(cls, raw_text):
        sanitized = sanitize_json(raw_text, fallback_field="mnemonics")
        return super().model_validate(sanitized)


class SafeAnalyseOutput(BaseModel):
    observations: List[str] = Field(default_factory=list)
    comparisons: List[str] = Field(default_factory=list)
    references: List[str] = Field(default_factory=list)
    insights: List[str] = Field(default_factory=list)
    concept_hierarchy: str = Field(default="")

    @classmethod
    def model_validate_json(cls, raw_text):
        sanitized = sanitize_json(raw_text, fallback_field="observations")
        return super().model_validate(sanitized)


class SafeEvaluateOutput(BaseModel):
    advantages: List[str] = Field(default_factory=list)
    disadvantages: List[str] = Field(default_factory=list)
    improvements: List[str] = Field(default_factory=list)
    opinion: str = Field(default="")

    @classmethod
    def model_validate_json(cls, raw_text):
        sanitized = sanitize_json(raw_text, fallback_field="advantages")
        return super().model_validate(sanitized)


class SafeApplyOutput(BaseModel):
    wh_questions: List[str] = Field(default_factory=list)
    mcq: List[str] = Field(default_factory=list)
    scenario_questions: List[str] = Field(default_factory=list)

    @classmethod
    def model_validate_json(cls, raw_text):
        sanitized = sanitize_json(raw_text, fallback_field="wh_questions")
        return super().model_validate(sanitized)


class SafeCreateOutput(BaseModel):
    projects: List[str] = Field(default_factory=list)
    perspectives: List[str] = Field(default_factory=list)
    applications: List[str] = Field(default_factory=list)

    @classmethod
    def model_validate_json(cls, raw_text):
        sanitized = sanitize_json(raw_text, fallback_field="projects")
        return super().model_validate(sanitized)




# ------------------------------
# Crew class
# ------------------------------

@CrewBase
class BloomsSummaryCrew():
    """BloomsSummaryCrew crew implementing Bloom's taxonomy-based summarization"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # --- Agents ---
    @agent
    def full_summarisation_agent(self) -> Agent:
        return Agent(config=self.agents_config['full_summarisation_agent'], verbose=True)

    @agent
    def understanding_agent(self) -> Agent:
        return Agent(config=self.agents_config['understanding_agent'], verbose=True)

    @agent
    def remember_agent(self) -> Agent:
        return Agent(config=self.agents_config['remember_agent'], verbose=True)

    @agent
    def analyse_agent(self) -> Agent:
        return Agent(config=self.agents_config['analyse_agent'], verbose=True)

    @agent
    def evaluate_agent(self) -> Agent:
        return Agent(config=self.agents_config['evaluate_agent'], verbose=True)

    @agent
    def apply_agent(self) -> Agent:
        return Agent(config=self.agents_config['apply_agent'], verbose=True)

    @agent
    def create_agent(self) -> Agent:
        return Agent(config=self.agents_config['create_agent'], verbose=True)

    # @agent
    # def combine_agent(self) -> Agent:
    #     return Agent(config=self.agents_config['combine_agent'], tools = [MergeBloomsJsonTool()],verbose=True)

    # @agent
    # def json_to_markdown_agent(self) -> Agent:
    #     return Agent(config=self.agents_config['json_to_markdown_agent'],verbose=True)

    # # --- Tasks ---
    @task
    def full_summarisation_task(self) -> Task:
        return Task(
            config=self.tasks_config['full_summarisation_task'],
            verbose=False
        )
    
    @task
    def understanding_task(self) -> Task:
        return Task(
            config=self.tasks_config['understanding_task'],
            # output_json=SafeUnderstandingOutput,
            verbose=False
        )

    @task
    def remember_task(self) -> Task:
        return Task(
            config=self.tasks_config['remember_task'],
            # output_json=SafeRememberOutput,
            verbose=False
        )

    @task
    def analyse_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyse_task'],
            # output_json=SafeAnalyseOutput,
            verbose=False
        )

    @task
    def evaluate_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluate_task'],
            # output_json=SafeEvaluateOutput,
            verbose=False
        )

    @task
    def apply_task(self) -> Task:
        return Task(
            config=self.tasks_config['apply_task'],
            # output_json=SafeApplyOutput,
            verbose=False
        )

    @task
    def create_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_task'],
            # output_json=SafeCreateOutput,
            verbose=False
        )

    # @task
    # def combine_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['combine_task'],
    #         verbose=False
    #     )

    # @task
    # def json_to_markdown_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['json_to_markdown_task'],
    #         verbose=False
    #     )

    # --- Crew ---
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=False
        )
