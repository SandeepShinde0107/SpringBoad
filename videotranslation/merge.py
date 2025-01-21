import subprocess

def merge_audio_with_video(video_path, audio_path, output_video_path):
    try:
        # FFmpeg command to merge video and translated audio, ensuring audio is included
        command = [
            'ffmpeg',
            '-i', video_path,               # Input video file
            '-i', audio_path,               # Input audio file
            '-c:v', 'libx264',              # Video codec (libx264 for video)
            '-c:a', 'aac',                  # Audio codec (AAC for audio)
            '-strict', 'experimental',      # For AAC codec compatibility
            '-map', '0:v:0',                # Use the video stream from the first input file (video)
            '-map', '1:a:0',                # Use the audio stream from the second input file (audio)
            '-shortest',                    # Ensures the output file duration matches the shortest stream
            '-y',                           # Overwrite output file if it already exists
            output_video_path              # Output file
        ]
        
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Video with translated audio saved at: {output_video_path}")
    
    except Exception as e:
        print(f"Failed to merge audio with video: {e}")

# Example usage
if __name__ == "__main__":
    video_path = "vid1.mp4"  # Input video file
    audio_path = "translated_audio.mp3"  # Translated audio file
    output_video_path = "final_video.mp4"  # Output video with translated audio

    merge_audio_with_video(video_path, audio_path, output_video_path)
