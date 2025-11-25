from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path
import yt_dlp
import os
from youtube_transcript_api.proxies import WebshareProxyConfig


def run(subject: str) -> dict:
    print(f"🔍 Searching and filtering YouTube videos for: {subject}")

    query = f"ytsearch20:{subject}"

    ydl_opts = {
        'quiet': True,
        'extract_flat': False,
        'skip_download': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)

    videos = info.get("entries", [])

    # Convert search subject to individual lowercase words
    subject_words = subject.lower().split()

    # Filtering:
    # 1️⃣ Duration >= 50 minutes (3000 sec)
    # 2️⃣ Title must contain ALL words from subject
    filtered_videos = []
    for v in videos:
        title = v.get("title", "").lower()
        if v.get("duration", 0) >= 3000 and all(word in title for word in subject_words):
            filtered_videos.append(v)

    # Sort by highest views & take top 5
    filtered_videos = sorted(
        filtered_videos,
        key=lambda x: x.get("view_count", 0),
        reverse=True
    )[:5]

    if not filtered_videos:
        return {"success": False, "message": "No matching long videos found.", "file_path": None}

    transcript_output = []

    for video in filtered_videos:
        video_id = video["id"]
        duration = video.get("duration", 0)
        views = video.get("view_count", 0)
        url = f"https://www.youtube.com/watch?v={video_id}"

        try:
            transcript = YouTubeTranscriptApi(
                proxy_config=WebshareProxyConfig(
                    proxy_username="vwvcppyi",
                    proxy_password="rghunqai3bar",
                )
            ).fetch(video_id)
            text = " ".join([t.text for t in transcript])
        except Exception as e:
            text = str(e)

        transcript_output.append(
            f"TITLE: {video['title']}\n"
            f"VIEWS: {views}\n"
            f"DURATION: {duration//60} minutes\n"
            f"URL: {url}\n\n{text}\n\n{'='*80}\n"
        )

    # Output
    current_file = Path(__file__).resolve()
    output_dir = current_file.parent.parent / "outputs"
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / f"{subject}_long_videos.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(transcript_output)

    print(f"📁 Saved transcripts to: {output_path}")

    return {
        "success": True,
        "message": "Filtered transcripts saved successfully.",
        "file_path": str(output_path),
    }

run("Java")


