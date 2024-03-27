echo _marcel
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_marcel
wait

echo _bala
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_bala
wait

echo _wojtek_1
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_wojtek_1
wait

echo _person_0004
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_person_0004
wait

echo _obama
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_obama
wait

echo _nf_01
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_nf_01
wait

echo _obama_adnerf
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_obama_adnerf
wait

echo _yufeng
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_yufeng
wait

echo _malte_1
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_malte_1
wait

echo _nf_03
CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/_nf_03
wait

