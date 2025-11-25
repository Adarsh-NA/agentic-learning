import json
from typing import List, Dict, Any
import os

def chunk_transcripts(json_file_path: str, max_tokens: int = 250000) -> List[Dict[str, Any]]:
    """
    Reads a JSON file containing transcripts and chunks each transcript into 
    pieces of at most `max_tokens` tokens (words).
    
    Args:
        json_file_path (str): Path to the input JSON file.
        max_tokens (int): Maximum number of tokens (words) per chunk.
        
    Returns:
        List[Dict[str, Any]]: List of dicts containing video info and chunks.
    """
    def chunk_text(text: str, video_title: str ,video_url:str ,max_tokens: int) -> List[str]:
        words = text.split()
        return [{"video_title":video_title[0],"video_url":video_url[0],"chunk_number":len(words)//(max_tokens+i),"transcription_chunk":" ".join(words[i:i + max_tokens])} for i in range(0, len(words), max_tokens)]

    with open(json_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chunked_transcripts = []

    for transcript_obj in data.get("transcripts", []):
        transcript_text = transcript_obj.get("transcript", "")
        video_title = transcript_obj.get("video_title"),
        video_url = transcript_obj.get("video_url"),
        chunked_transcripts.extend(chunk_text(transcript_text,video_title,video_url, max_tokens))
        
    input_dir = os.path.dirname(json_file_path)
    output_file = os.path.join(input_dir, "chunked_transcripts.json")

    # Save chunked transcripts to JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(chunked_transcripts, f, ensure_ascii=False, indent=2)

    return chunked_transcripts

# --- Example usage ---
if __name__ == "__main__":
    input_file = "/Users/adarshna/Codes/Jupyter/17_AgenticAI/CrewAI/EdTechAutomation/agentic_learning/src/agentic_learning/outputs/FastAPI_20251123205150/transcripts/FastAPI_transcripts.json"

    chunked_data = chunk_transcripts(input_file, max_tokens=250000)
    
    # Optional: save to a new JSON file
    with open("chunked_transcripts.json", "w", encoding="utf-8") as f:
        json.dump(chunked_data, f, ensure_ascii=False, indent=2)

    # Optional: print first chunk of first video
    print(chunked_data[0]["transcription_chunk"])
