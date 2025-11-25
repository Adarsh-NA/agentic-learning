from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from agentic_learning.tools.youtube_tool import YouTubeTool
from agentic_learning.tools.markdown_writer_tool import MarkdownWriterTool
from pydantic import BaseModel, HttpUrl
from typing import List, Optional

from dotenv import load_dotenv
load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

from typing import List
from pydantic import BaseModel, Field


class TopicItem(BaseModel):
    topic: str = Field(..., description="The name of the Topic / Module")
    subtopics: List[str] = Field(
        ..., description="List of bullet-point subtopics under this topic"
    )
    duration: str = Field(
        ..., description="Time allocated in hours, formatted as a string (e.g., '2')"
    )

class GenerateTOCOutput(BaseModel):
    subject: str = Field(..., description="The subject for which the TOC is designed")
    total_duration: str = Field(
        ..., description="Total duration allocated for the entire training program"
    )
    toc: List[TopicItem] = Field(
        ..., description="List of topics with subtopics and allocated duration"
    )


class VideoTranscript(BaseModel):
    video_title: str
    video_duration: Optional[int]  # Some APIs may not provide this reliably
    video_url: HttpUrl
    views: Optional[int]  # Some APIs may not provide this reliably
    transcript: str

class YouTubeTranscriptOutput(BaseModel):
    subject: str
    transcripts: List[VideoTranscript]

class YouTubeToolResponse(BaseModel):
    success: bool
    message: str
    transcript_path: Optional[str] = None
    
@CrewBase
class SubjectResearchCrew():
    """SubjectResearchCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
   
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def toc_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['toc_researcher'], # type: ignore[index]
            verbose=True,
        )
    
    @agent
    def toc_formatter(self) -> Agent:
        return Agent(
            config=self.agents_config['toc_formatter'], # type: ignore[index]
            verbose=True,
        )

    @agent
    def youtube_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['youtube_scraper'], # type: ignore[index]
            verbose=True,
            tools = [YouTubeTool()],
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def generate_toc(self) -> Task:
        return Task(
            config=self.tasks_config['generate_toc'], # type: ignore[index]
            output_json= GenerateTOCOutput
        )

    @task
    def format_toc(self) -> Task:
        return Task(
            config=self.tasks_config['format_toc'], # type: ignore[index]
        )

    @task
    def collect_transcripts(self) -> Task:
        return Task(
            config=self.tasks_config['collect_transcripts'], # type: ignore[index]
            output_json=YouTubeToolResponse
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SubjectResearchCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
