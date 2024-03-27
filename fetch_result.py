import os, json
path="/data/chenziang/codes/SplattingAvatar/data"

# 遍历path，获取子文件夹
subdirs= os.listdir(path)

results=dict()


# # 遍历subdirs
# for subdir in subdirs:
#     # 如果以"_"开头，则跳过
#     if subdir.startswith("_"):
#         continue

#     if subdir=="obama_adnerf":
#         continue

#     json_path= os.path.join(path, subdir,"output-splatting/last_checkpoint/eval_30000/stats.json")
#     # print(json_path)

#     # 读取json文件，将key保存到字典
#     # 这是json的一个例子
#     # {"psnr": 30.628132351466586, "ssim": 0.9599734457901546, "lpips": 0.03125369296010051, "n_gauss": 251620}
#     with open(json_path, 'r') as f:
#         data= json.load(f)
#         results[subdir]= data





# 遍历subdirs
for subdir in subdirs:
    # 如果以"_"开头且不以"__"开头
    if not (subdir.startswith("_") and not subdir.startswith("__")):
        continue

    if subdir=="obama_adnerf":
        continue

    # print(subdir)
    # continue

    json_path = os.path.join(path, subdir, "output-splatting")
    # 遍历json_path，寻找最新的文件夹，文件夹格式"@yyyymdd-hhmmss"
    subsubdirs = os.listdir(json_path)
    subsubdirs = [x for x in subsubdirs if x.startswith("@")]
    subsubdirs.sort()
    if len(subsubdirs)==0:
        raise Exception("No subsubdirs found in ", json_path)
    subsubdir= subsubdirs[-1]
    json_path = os.path.join(json_path, subsubdir, "eval_30000/stats.json")


    print(json_path)
    # continue

    # 读取json文件，将key保存到字典
    # 这是json的一个例子
    # {"psnr": 30.628132351466586, "ssim": 0.9599734457901546, "lpips": 0.03125369296010051, "n_gauss": 251620}
    with open(json_path, 'r') as f:
        data= json.load(f)
        results[subdir]= data







# 统计字典中值的平均值
psnr_sum=0
ssim_sum=0
lpips_sum=0
n_gauss_sum=0

for k,v in results.items():
    psnr_sum+=v["psnr"]
    ssim_sum+=v["ssim"]
    lpips_sum+=v["lpips"]
    n_gauss_sum+=v["n_gauss"]

print("psnr_avg:", psnr_sum/len(results))
print("ssim_avg:", ssim_sum/len(results))
print("lpips_avg:", lpips_sum/len(results))
print("n_gauss_avg:", n_gauss_sum/len(results))
