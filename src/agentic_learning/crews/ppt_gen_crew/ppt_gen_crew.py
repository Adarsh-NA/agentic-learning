from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from agentic_learning.tools.create_ppt_from_json_tool import CreatePPTFromJsonTool
from dotenv import load_dotenv
load_dotenv()
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class PptGenCrew():
    """PptGenCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def json_ppt_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['json_ppt_generator_agent'], # type: ignore[index]
            verbose=True
        )
    @agent
    def ppt_generation_from_json_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ppt_generation_from_json_agent'], # type: ignore[index]
            tools = [CreatePPTFromJsonTool()],
            verbose=True
        )


    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def generate_jsonppt_from_toc_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_jsonppt_from_toc_task'], # type: ignore[index]
        )

    @task
    def generate_ppt_from_json_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_ppt_from_json_task'], # type: ignore[index]
        )


    @crew
    def crew(self) -> Crew:
        """Creates the PptGenCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
