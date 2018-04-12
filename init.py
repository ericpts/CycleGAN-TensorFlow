#!/usr/bin/env python3
import os
import shutil
import subprocess
from random import randint, shuffle
from pathlib import Path

datasets = [apple2orange, summer2winter_yosemite, horse2zebra, monet2photo, cezanne2photo, ukiyoe2photo, vangogh2photo, maps, cityscapes, facades, iphone2dslr_flower, ae_photos]

def download_all():
    for d in datasets:
        subprocess.run(['bash', 'download_dataet.sh', d], check=True)

def make_comp():
    comp = Path('data/comp')
    if comp.exists():
        shutil.rmtree(str(comp))
    comp.mkdir()

    for d in datasets:
        dpath = Path('data') / d
        for img in dpath.glob('**/*.jpg'):
            shutil.copy(str(img), str(comp))

def partition():
    comp = Path('data/comp')
    images = list(comp.glob('*.jpg'))
    shuffle(images)

    N = len(images)
    ntest = int(N  * 0.1)
    ntrain = N - ntest

    test = images[: ntest]
    train = images[ntest: ]

    assert len(test) == ntest
    assert len(train) == ntrain

    def force_make(path: Path):
        if path.exists():
            shutil.rmtree(str(path))
        path.mkdir()

    force_make(comp / 'testA')
    force_make(comp / 'trainA')

    for f in test:
        shutil.copy(str(f), str(comp / 'testA'))
    for f in train:
        shutil.copy(str(f), str(comp / 'trainA'))

    force_make(comp / 'testB')
    force_make(comp / 'trainB')

    def conv(src: str, dst: str):
        subprocess.run(['convert', src, '-colorspace', 'Gray', dst], check=True)

    for f in test:
        conv(str(f), str(comp / 'testB' / f.name))
    for f in train:
        conv(str(f), str(comp / 'trainB' / f.name))


def main():
    download_all()
    make_comp()
    partition()

if __name__ == '__main__':
    main()
