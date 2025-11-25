from typing import Type, Optional, List
from pydantic import BaseModel, Field, HttpUrl
from crewai.tools import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
import yt_dlp
import json
from pathlib import Path


class YouTubeToolInput(BaseModel):
    subject: str = Field(..., description="Search subject/topic")
    transcripts_dir_path: str = Field(..., description="Directory where transcripts should be saved")


class VideoTranscript(BaseModel):
    video_title: str
    video_duration: Optional[int]
    video_url: str
    views: Optional[int]
    transcript: str


class YouTubeTranscriptOutput(BaseModel):
    subject: str
    transcripts: List[VideoTranscript]


class YouTubeTool(BaseTool):
    name: str = "youtube_tool"
    
    description: str = "Search YouTube for most watched long (>50 mins) videos on topic, "\
        "extract transcripts, save JSON file inside transcripts_dir_path, "\
        "return success status and saved path"
    
    args_schema: Type[BaseModel] = YouTubeToolInput

    def _run(self, subject: str, transcripts_dir_path: str) -> dict:
        print(f"📡 Searching YouTube for: {subject}")

        try:
            transcripts_dir = Path(transcripts_dir_path)
            transcripts_dir.mkdir(parents=True, exist_ok=True)

            # Search top 20 videos
            query = f"ytsearch20:{subject}"
            ydl_opts = {
                'quiet': True,
                'skip_download': True,
                'cachedir': False,
                'extractor_args': {'youtube': ['player_client=default']},
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)

            videos = info.get("entries", [])
            subject_words = subject.lower().split()

            # Filter relevant long videos
            filtered = [
                v for v in videos
                if v.get("duration", 0) >= 3000
                and all(word in v.get("title", "").lower() for word in subject_words)
            ]

            filtered = sorted(
                filtered,
                key=lambda x: x.get("view_count", 0),
                reverse=True
            )[:3]


            print('Searched videos')
            print([f"{v.get("title")}:,https://www.youtube.com/watch?v={v["id"]}"for v in videos])
            print('Filtered videos')
            print([f"{v.get("title")}:,https://www.youtube.com/watch?v={v["id"]}"for v in filtered])
            transcripts_list = []

            for v in filtered:
                video_id = v["id"]
                url = f"https://www.youtube.com/watch?v={video_id}"
                print(f"Extracting transcript from: {url}")
                try:
                    transcript_data = YouTubeTranscriptApi(
                        proxy_config=WebshareProxyConfig(
                            proxy_username="vwvcppyi",
                            proxy_password="rghunqai3bar",
                        )
                    ).fetch(video_id)
                    text = " ".join(t.text for t in transcript_data)
                except Exception:
                    text = "Transcript not available"

                transcripts_list.append(
                    VideoTranscript(
                        video_title=v.get("title", "Unknown Title"),
                        video_duration=v.get("duration"),
                        video_url=url,
                        views=v.get("view_count"),
                        transcript=text
                    ).dict()
                )

            output = YouTubeTranscriptOutput(
                subject=subject,
                transcripts=transcripts_list
            ).dict()

            output_file = transcripts_dir / f"{subject}_transcripts.json"

            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(output, f, indent=2, ensure_ascii=False)

            print(f"📁 Saved transcripts: {output_file}")

            return {
                "success": True,
                "message": "Transcripts saved successfully",
                "transcript_path": str(output_file)
            }

        except Exception as err:
            return {
                "success": False,
                "message": str(err),
                "transcript_path": None
            }
