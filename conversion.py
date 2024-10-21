import subprocess
import os
import sys
import argparse

def is_ffmpeg_installed():
    """Check if ffmpeg is installed and accessible."""
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def convert_to_mp4_h264(input_path, output_path, preserve_audio=True):
    """
    Convert a video file to MP4 with H.264 video codec using ffmpeg.

    :param input_path: Path to the input video file (.mp4 or .mov)
    :param output_path: Path to the output .mp4 file
    :param preserve_audio: Whether to keep the audio stream
    """
    # Build FFmpeg command
    command = [
        'ffmpeg',
        '-i', input_path,          # Input file
        '-c:v', 'libx264',         # Video codec: H.264
        '-preset', 'fast',         # Encoding speed
        '-crf', '23',              # Quality (lower is better; range: 0-51)
    ]

    if preserve_audio:
        # Use AAC for audio codec
        command += ['-c:a', 'aac', '-b:a', '192k']
    else:
        # Remove audio
        command += ['-an']

    # Additional options
    command += [
        '-movflags', '+faststart', # Optimize for web streaming
        output_path
    ]

    try:
        print(f"Converting '{input_path}' to '{output_path}'...")
        subprocess.run(command, check=True)
        print(f"Successfully converted '{input_path}' to '{output_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def process_file(file_path, output_dir, preserve_audio):
    """
    Process a single video file.

    :param file_path: Path to the input video file
    :param output_dir: Directory where the output file will be saved
    :param preserve_audio: Whether to keep the audio stream
    """
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = os.path.join(output_dir, f"{base_name}_h264.mp4")
    convert_to_mp4_h264(file_path, output_file, preserve_audio)

def main():
    parser = argparse.ArgumentParser(description="Convert MP4 or MOV files to MP4 with H.264 video codec.")
    parser.add_argument('input', help="Path to input file or directory containing video files.")
    parser.add_argument('-o', '--output', help="Output directory. Defaults to input file's directory.", default=None)
    parser.add_argument('--no-audio', action='store_true', help="Remove audio from the output files.")
    args = parser.parse_args()

    input_path = args.input
    output_dir = args.output
    preserve_audio = not args.no_audio

    if not is_ffmpeg_installed():
        print("FFmpeg is not installed or not found in PATH. Please install FFmpeg and try again.")
        sys.exit(1)

    if os.path.isfile(input_path):
        if not input_path.lower().endswith(('.mp4', '.mov')):
            print("Input file must be a .mp4 or .mov file.")
            sys.exit(1)
        if not output_dir:
            output_dir = os.path.dirname(input_path)
        os.makedirs(output_dir, exist_ok=True)
        process_file(input_path, output_dir, preserve_audio)
    elif os.path.isdir(input_path):
        files = [f for f in os.listdir(input_path) if f.lower().endswith(('.mp4', '.mov'))]
        if not files:
            print("No .mp4 or .mov files found in the specified directory.")
            sys.exit(1)
        if not output_dir:
            output_dir = input_path
        os.makedirs(output_dir, exist_ok=True)
        for file in files:
            full_path = os.path.join(input_path, file)
            process_file(full_path, output_dir, preserve_audio)
    else:
        print("The input path must be a valid file or directory.")
        sys.exit(1)

if __name__ == "__main__":
    main()
