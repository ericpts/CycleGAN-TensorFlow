#!/bin/bash

DATASETS=(\
    apple2orange\
    summer2winter_yosemite\
    horse2zebra\
    monet2photo\
    cezanne2photo\
    ukiyoe2photo\
    vangogh2photo\
    maps\
    cityscapes\
    facades\
    iphone2dslr_flower\
    ae_photos\
    )

for i in ${DATASETS[@]}; do
    if [ ! -e data/$i ]; then
        bash download_dataset.sh $i &
    fi
done

wait

cd data
rm -rf comp
mkdir comp

for i in ${DATASETS[@]}; do
    find "$i" -name "*.jpg" -type f -exec cp {} comp \;
done

