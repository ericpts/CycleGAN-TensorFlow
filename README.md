# CycleGAN-TensorFlow
An implementation of CycleGan using TensorFlow (work in progress).

Original paper: https://arxiv.org/abs/1703.10593

## Results on test data

### black and white -> colorized

| Input | Output |
|-------|--------|
|![black and white](samples/input_sample.jpg) | ![colorized](samples/output_sample.jpg)|


## Environment

* TensorFlow 1.0.0
* Python 3.6.0


## Preparing

See the `colab_notebook.ipynb` notebook for a google colab demo.

* Run init.py to download the datasets.
```bash
$ python3 init.py
```

* Write the dataset to tfrecords

```bash
$ python3 build_data.py
```

Check `$ python3 build_data.py --help` for more details.

## Training

```bash
$ python3 train.py
```

If you want to change some default settings, you can pass those to the command line, such as:

```bash
$ python3 train.py  \
    --X=data/tfrecords/black.tfrecords \
    --Y=data/tfrecords/colored.tfrecords
```


Check TensorBoard to see training progress and generated images.

```
$ tensorboard --logdir checkpoints/${datetime}
```

If you halted the training process and want to continue training, then you can set the `load_model` parameter like this.

```bash
$ python3 train.py --load_model 20170602-1936
```

Here are some funny screenshots from TensorBoard when training orange -> apple:


### Notes

## Export model
You can export from a checkpoint to a standalone GraphDef file as follow:

```bash
$ python3 export_graph.py --checkpoint_dir checkpoints/${datetime} \
                          --XtoY_model bw2color.pb \
                          --YtoX_model color2bw.pb \
                          --image_size 256
```


## Inference
After exporting model, you can use it for inference. For example:

```bash
python3 inference.py --model pretrained/bw2color.pb \
                     --input input_sample.jpg \
                     --output output_sample.jpg \
                     --image_size 256
```

## Pretrained models
My pretrained models are available [here](https://drive.google.com/open?id=1RbNyb1hLzsehIxhIQ3hKWDEsWuIxGT89)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## References

* CycleGAN paper: https://arxiv.org/abs/1703.10593
* Official source code in Torch: https://github.com/junyanz/CycleGAN
