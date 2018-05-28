#!/usr/bin/env python3

import os
from pathlib import Path
from random import choices

import argparse
import subprocess

def run_inference(model: Path, in_file: Path, out_file: Path) -> None:
    print('Running inference on {}'.format(in_file))
    subprocess.run(['python3', 'inference.py',
        '--model', str(model),
        '--input', str(in_file),
        '--output', str(out_file),
        '--image_size', '256'], check=True)


def main():
    parser = argparse.ArgumentParser(description='Generate color samples from black and white pictures.')
    parser.add_argument('--nsamples', default=10, type=int, help='How many samples to generate.')
    args = parser.parse_args()

    src_dir = Path('data/comp/testA')
    pictures = choices(list(src_dir.glob('**/*.jpg')), k=args.nsamples)
    model = Path('pretrained/bw2color.pb')
    for p in pictures:
        run_inference(model, p, Path('samples/') / p.name)

if __name__ == '__main__':
    main()

