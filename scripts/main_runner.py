import os
import argparse
import numpy as np
import librosa


def load_raw_data(path_to_audio_file:str):
    y, _ = librosa.load(path_to_audio_file)
    return y


def main(path_to_data:str):
    _, _, files = next(os.walk(path_to_data))

    raw_data = []
    for f in files:
        raw_data.append(load_raw_data(os.path.join(path_to_data, f)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=str, help="Path to data")

    args = parser.parse_args()
    main(args.data)
