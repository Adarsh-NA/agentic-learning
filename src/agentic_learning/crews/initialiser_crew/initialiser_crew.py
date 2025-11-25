from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from agentic_learning.tools.folder_structure_tool import FolderStructureTool
from pydantic import BaseModel, Field

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

class FolderStructureOutput(BaseModel):
    success: bool
    message: str
    root_dir_path: str | None = None
    primary_dir_path: str | None = None
    toc_dir_path: str | None = None
    transcripts_dir_path: str | None = None
    blooms_summary_dir_path: str | None = None
    presentations_dir_path: str | None = None


@CrewBase
class InitialiserCrew():
    """InitialiserCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def folder_structure_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['folder_structure_agent'], # type: ignore[index]
            verbose=True,
            tools = [FolderStructureTool()]
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task


    @task
    def create_folder_structure_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_folder_structure_task'], # type: ignore[index]
            output_json=FolderStructureOutput,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the InitialiserCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
