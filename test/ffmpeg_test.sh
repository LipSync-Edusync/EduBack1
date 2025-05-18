#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 input.mp4 output.wav"
    exit 1
fi

# Assign arguments to variables
MP4_FILE="$1"
WAV_FILE="$2"

# Run FFmpeg command
ffmpeg -i "$MP4_FILE" -vn -acodec pcm_s16le -ar 44100 -ac 2 "$WAV_FILE" -y

# Check if the conversion was successful
if [ $? -eq 0 ]; then
    echo "Conversion successful: $MP4_FILE -> $WAV_FILE"
else
    echo "Conversion failed!"
    exit 1
fi
