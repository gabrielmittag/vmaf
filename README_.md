### Training (parallelize leads to errors)
```
python ./python/vmaf/script/run_vmaf_training.py \
    resource/dataset/dataset_train.py \
    resource/feature_param/vmaf_feature_all.py \
    resource/model_param/libsvmnusvr_v3.py \
    workspace/model/vmaf_vidset_model_all.pkl \
    --cache-result \
    --save-plot /mnt/results/train/vmaf_all
```
 


### Testing:

```
python ./python/vmaf/script/run_testing.py VMAF resource/dataset/dataset_val.py --save-plot /mnt/results/val/vmaf --parallelize --cache-result

python ./python/vmaf/script/run_testing.py VMAF resource/dataset/dataset_val.py --save-plot /mnt/results/val/vmaf --parallelize --cache-result --vmaf-model /mnt/repos/vmaf/workspace/model/vmaf_vidset_model_all.pkl

python ./python/vmaf/script/run_testing.py PSNR resource/dataset/dataset_val.py --save-plot /mnt/results/val/psnr --parallelize --cache-result

python ./python/vmaf/script/run_testing.py SSIM resource/dataset/dataset_val.py --save-plot /mnt/results/val/ssim --parallelize --cache-result

python ./python/vmaf/script/run_testing.py MS_SSIM resource/dataset/dataset_val.py --save-plot /mnt/results/val/ms_ssim --parallelize --cache-result
```

