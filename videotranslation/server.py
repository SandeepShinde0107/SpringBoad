import subprocess

def extract_audio_ffmpeg(video_path, audio_output_path):
    """
    Extracts audio from a video file using FFmpeg.

    Args:
        video_path (str): Path to the input video file.
        audio_output_path (str): Path to save the extracted audio file.
    """
    try:
        print(f"Extracting audio from {video_path}...")
        command = [
            "ffmpeg",
            "-i", video_path,       # Input file
            "-q:a", "0",            # Preserve quality
            "-map", "a",            # Select only audio
            audio_output_path       # Output file
        ]
        subprocess.run(command, check=True)
        print(f"Audio successfully extracted to {audio_output_path}")
    except subprocess.CalledProcessError as e:
        print("Error occurred while extracting audio:", e)

extract_audio_ffmpeg("vid.mp4", "output_audio1.mp3")
