"""
创建临时文件夹和复制视频
"""


# import os
# path="/data/chenziang/codes/SplattingAvatar/data"

# # 遍历path，获取子文件夹
# subdirs= os.listdir(path)

# # 遍历子文件夹
# for subdir in subdirs:
#     # 如果subdir以 "_" 开头，则跳过
#     if subdir.startswith("_"):
#         continue
    
#     # 创建新的文件夹，名称为_subdir
#     new_subdir="_"+subdir
#     new_subdir_path=os.path.join(path,new_subdir)
#     os.makedirs(new_subdir_path,exist_ok=True)

#     # 将subdir下的images目录复制到new_subdir下
#     # images_path=os.path.join(path,subdir,"images")
#     # new_images_path=os.path.join(new_subdir_path,"images")
#     # os.makedirs(new_images_path,exist_ok=True)
#     # os.system("cp -r %s %s"%(images_path,new_images_path))

#     # 将subdir下的video.mp4复制到new_subdir下
#     video_path=os.path.join(path,subdir,"video.mp4")
#     new_video_path=os.path.join(new_subdir_path,"video.mp4")
#     os.system("cp %s %s"%(video_path,new_video_path))


#     # # 获取子文件夹的路径
#     # subdir_path=os.path.join(path,subdir)
#     # # 获取子文件夹中的文件
#     # files=os.listdir(subdir_path)
#     # # 遍历文件
#     # for file in files:
#     #     # 获取文件的路径
#     #     file_path=os.path.join(subdir_path,file)
#     #     # 获取文件的大小
#     #     size=os.path.getsize(file_path)
#     #     print(file_path,size)




"""
call preprocess.py
"""

import os
path="/data/chenziang/codes/SplattingAvatar/data"

# 创建一个run_train.sh文件路径
bash_path=os.path.join(os.getcwd(),"run_train.sh")


# 遍历path，获取子文件夹
subdirs= os.listdir(path)

# 遍历subdirs
for subdir in subdirs:
    # 如果subdir以 "_" 开头且不以"__"开头，继续
    if not (subdir.startswith("_") and not subdir.startswith("__")):
       continue

    # 如果subdir下存在"output-splatting"文件夹，则跳过
    output_splatting_path=os.path.join(path,subdir,"output-splatting")
    if os.path.exists(output_splatting_path):
        continue
    
    # 构建bash指令
    cmd="CUDA_VISIBLE_DEVICES=3 python train_splatting_avatar.py --config configs/splatting_avatar.yaml --ip none --dat_dir ./data/{subject}".format(subject=subdir)
    # 写入bash文件
    with open(bash_path,"a") as f:
        # 写入echo
        f.write("echo %s\n"%(subdir))
        f.write(cmd+"\n")
        # 写入wait
        f.write("wait\n")
        # 写入换行
        f.write("\n")

    
    # print(subdir)