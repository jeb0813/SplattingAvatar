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

