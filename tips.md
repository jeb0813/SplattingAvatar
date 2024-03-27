# Env setup
pytorch3d: https://blog.csdn.net/weixin_43722052/article/details/134136571

# Training
python train_splatting_avatar.py --config configs/splatting_avatar.yaml --dat_dir <path/to/subject>  
\# for example:  
python train_splatting_avatar.py --config configs/splatting_avatar.yaml --dat_dir /path-to/bala

\# you may specify gpu id by adding CUDA_VISIBLE_DEVICES=x before calling python:  
CUDA_VISIBLE_DEVICES=0 python train_splatting_avatar.py ...

\# to disable network_gui, set ip to 'none'  
CUDA_VISIBLE_DEVICES=0 python train_splatting_avatar.py ... --ip none  

\# use SIBR_remoteGaussian_app.exe from 3DGS to watch the training  
SIBR_remoteGaussian_app.exe --path <path/to/model_path>
\# for example:  
SIBR_remoteGaussian_app.exe --path C:\SplattingAvatar\bala\output-splatting\last_checkpoint

\# it is recommended to change "FPS" to "Trackball" in the viewer  
\# you don't need to change the "path" everytime  

# Eval 
python eval_splatting_avatar.py --config configs/splatting_avatar.yaml --dat_dir <path/to/model_path>  
\# for example:  
python eval_splatting_avatar.py --config configs/splatting_avatar.yaml --dat_dir /path-to/bala/output-splatting/last_checkpoint  



# Preprocessing
使用的这个pipeline https://github.com/zhengyuf/IMavatar  

首先使用 https://github.com/PeterL1n/RobustVideoMatting 对人物和背景进行分割  
使用ffmpeg将视频保存为图片 
ffmpeg -i ./output.mp4 -q:v 2  ./images/%d.png  
然后使用DECA获得code.json，需要特别注意的是，DECA中的demo_reconstruct.py需要被覆写为IMavatar中的代码  

通过 optimize.py 将 code.json 转换为flame_param.json

已经完成预处理，但是效果不理想  

# 复现  
用自己的预处理方法跑的权重效果没有作者给的好  
尝试使用作者给的权重再跑一次  

**预训练权重** __biden  
100%|█| 350/350 [00:26<00:00, 13.04it/s, psnr=30.6284(30.7584), ssim=0.9600(0.9603), l
[done]  

用自己预处理的数据 _biden  
100%|█| 350/350 [00:26<00:00, 13.14it/s, psnr=26.2431(25.6281), ssim=0.9436(0.9375), l
[done]  

**预处理文件自训** __biden  
100%|█| 350/350 [00:26<00:00, 13.28it/s, psnr=30.4011(30.4261), ssim=0.9578(0.9588), l
[done]  

尝试用作者给的json文件做推理  
发现自己处理的视频在第一步背景去除阶段就丢帧了  


重新做了预处理和训练  
100%|█| 350/350 [00:25<00:00, 13.62it/s, psnr=26.0312(26.3907), ssim=0.9353(0.9377), l
[done]

再次尝试用作者的json做推理  
100%|█| 350/350 [00:26<00:00, 13.29it/s, psnr=25.7146(26.3334), ssim=0.9312(0.9366), l
[done]  

**再次优化预处理流程**  
100%|█| 350/350 [00:26<00:00, 13.39it/s, psnr=27.7831(27.2251), ssim=0.9457(0.9437), l
[done]  

尝试用自己训练的权重和作者给的处理过的图片做推理  
100%|█| 350/350 [00:28<00:00, 12.45it/s, psnr=23.1840(23.2462), ssim=0.9275(0.9267), l
[done]

自己训练的权重和作者给的处理过的图片、json做推理  
100%|█| 350/350 [00:27<00:00, 12.73it/s, psnr=23.8483(23.9774), ssim=0.9277(0.9326), l
[done]


自己的权重+作者的json  
100%|█| 350/350 [00:27<00:00, 12.74it/s, psnr=27.7385(27.2280), ssim=0.9429(0.9448), l
[done]  

v2版本预处理，将分割换为原始图像  
100%|█| 350/350 [00:23<00:00, 15.08it/s, psnr=27.5782(27.1278), ssim=0.9457(0.9457), lpips=



ffmpeg -framerate 25 -i ./render/%05d.png -c:v libx264 -r 25 -pix_fmt yuv420p output_video.mp4

ls -l ./ | grep "^-" | wc -l  

作者给的预训练文件的结果  
psnr_avg: 28.61068330819266   
ssim_avg: 0.9370488937411989  
lpips_avg: 0.0569037944365825  
n_gauss_avg: 309687.6  


自己train的结果  
psnr_avg: 25.584101701216262  
ssim_avg: 0.9157033726302061  
lpips_avg: 0.1232667076336099  
n_gauss_avg: 226540.45454545456  