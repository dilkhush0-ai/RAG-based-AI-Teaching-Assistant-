import os
import subprocess

os.makedirs("audios", exist_ok=True)

files = os.listdir(".")

for file in files:
    if file.endswith(".mp4") and file.startswith("#"):
        tutorial_number = file.split(" [")[0][1:]
        file_name = file.split(" [")[1].split("]")[0]

        output_path = f"audios/{tutorial_number}_{file_name}.mp3"

        command = [
            "ffmpeg",
            "-i", file,
            output_path
        ]

        subprocess.run(command)

