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
    bw_src_dir = Path('data/comp/testA')
    color_src_dir = Path('data/comp/testB')

    bw_pictures = choices(
            list(bw_src_dir.glob('**/*.jpg')), k=10)
    color_pictures = choices(
            list(color_src_dir.glob('**/*.jpg')), k=10)

    os.makedirs('samples/bw2color', exist_ok=True)
    os.makedirs('samples/color2bw', exist_ok=True)

    bw2color_model = Path('pretrained/bw2color.pb')
    color2bw_model = Path('pretrained/color2bw.pb')

    for p in bw_pictures:
        run_inference(bw2color_model, p, Path('samples/bw2color/') / p.name)
    for p in color_pictures:
        run_inference(color2bw_model, p, Path('samples/color2bw/') / p.name)

if __name__ == '__main__':
    main()

