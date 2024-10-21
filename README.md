# H.264 Video Converter
This script is designed to convert .mp4 or .mov video files to .mp4 format using the H.264 video codec. It supports batch processing and provides the option to preserve or remove audio from the output files.

## Features
- Converts .mp4 and .mov files to .mp4 using the H.264 codec.
- Option to preserve or remove the audio stream.
- Optimized for web streaming using +faststart.
- Supports single-file and directory-based batch conversion.

## Requirements
- FFmpeg must be installed and accessible in your system's PATH.
- Python 3.x

## Installation
### Clone the repository:

```
git clone https://github.com/jingkai27/h264-converter.git
cd h264-converter
```

Install FFmpeg if not already installed. You can check if FFmpeg is installed using:

```
ffmpeg -version
```
## Usage

### Basic Usage
Convert a single .mp4 or .mov file to .mp4 with H.264 encoding:

```
python h264_converter.py <input-file>
python h264_converter.py input_video.mp4
```

### Batch Processing
Convert all .mp4 and .mov files in a directory:

```
python h264_converter.py <input-directory>
python h264_converter.py ./videos/
```

### Additional Options
By default, the output files are saved in the same directory as the input files. You can specify a different output directory using the -o option:

```
python h264_converter.py <input-file-or-directory> -o <output-directory>
```
**Remove audio**: To remove the audio stream from the output files, use the --no-audio option:

```
python h264_converter.py <input-file-or-directory> --no-audio
```
**Examples**:
Convert a single file and keep the audio:

```
python h264_converter.py input_video.mp4
```
Convert all files in a directory, output to a different directory, and remove audio:

```
python h264_converter.py ./input_videos/ -o ./output_videos/ --no-audio
```

## Notes
**FFmpeg Installation**: Ensure that ffmpeg is installed and accessible via your system's PATH. You can check this by running ffmpeg -version in your terminal.

The CRF (Constant Rate Factor) value is set to 23, which balances quality and file size. Lower values will result in better quality but larger file sizes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.