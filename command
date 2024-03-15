source activate splatting

CUDA_VISIBLE_DEVICES=1 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir /data3/chenziang/_dataset/IMavatar/biden


CUDA_VISIBLE_DEVICES=1 python eval_splatting_avatar.py --config configs/splatting_avatar.yaml --dat_dir ./data/biden/ --pc_dir ./data/biden/output-splatting/@20240315-110159/point_cloud/iteration_30000/

