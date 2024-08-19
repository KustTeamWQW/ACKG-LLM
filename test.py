from src.models import GenIEFlanT5PL
import os
from tqdm import tqdm

# 设置 GPU
os.environ['CUDA_VISIBLE_DEVICES'] = "7"

# 加载模型
path_to_checkpoint = "/home/ubuntu/project/SynthIE/model/models/genie_base_sc.ckpt"
model = GenIEFlanT5PL.load_from_checkpoint(checkpoint_path=path_to_checkpoint)
model.to("cuda")

# 设置模型参数
override_models_default_hf_generation_parameters = {
    "num_beams": ,
    "num_return_sequences": ,
    "return_dict_in_generate": True,
    "output_scores": True,
    "seed": ,
    "length_penalty": 
}

# 输入和输出文件路径
input_file_path = '/home/ubuntu/project/SynthIE/data/datasets/rebel.txt'
output_file_path = '/home/ubuntu/project/SynthIE/data/output/genie-sc-rebel.txt'

# 获取输入文件的总行数，便于显示进度条
total_lines = sum(1 for _ in open(input_file_path, 'r'))

# 逐行读取输入文件并处理，显示进度条
with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in tqdm(infile, total=total_lines, desc="Processing lines"):
        # 去除行末尾的换行符
        line = line.strip()
        if line:  # 确保不是空行
            # 使用模型处理该行
            output = model.sample(line,
                                  convert_to_triplets=True,
                                  return_generation_outputs=True,
                                  **override_models_default_hf_generation_parameters)
            # 获取处理后的输出
            processed_output = output['grouped_decoded_outputs'][0]
            print(processed_output)
            
            # 处理输出，将每个 tuple 转换为列表中的一个字符串
            processed_output_list = [list(item) for item in processed_output]
            
            # 将列表写入输出文件
            outfile.write(str(processed_output_list) + "\n")

print(f"处理后的输出已保存到: {output_file_path}")

