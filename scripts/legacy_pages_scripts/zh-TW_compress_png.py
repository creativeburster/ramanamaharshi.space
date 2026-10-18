#!/usr/bin/env python3
import os
from PIL import Image
import shutil

def compress_png(input_path, output_path=None, quality=95):
    """
    压缩 PNG 图片（无损压缩）
    """
    if output_path is None:
        output_path = input_path
    
    # 备份原图
    backup_path = input_path + '.bak'
    shutil.copy2(input_path, backup_path)
    
    # 打开并压缩
    img = Image.open(input_path)
    
    # 保存为优化的 PNG
    img.save(output_path, 'PNG', optimize=True)
    
    # 获取文件大小
    original_size = os.path.getsize(backup_path)
    compressed_size = os.path.getsize(output_path)
    
    return {
        'input': input_path,
        'original': original_size,
        'compressed': compressed_size,
        'saved': original_size - compressed_size,
        'percent': (1 - compressed_size/original_size)*100 if original_size > 0 else 0
    }

def compress_directory(directory):
    """
    压缩目录下所有 PNG 文件
    """
    total_original = 0
    total_compressed = 0
    results = []
    
    print(f'开始压缩 {directory} 目录下的 PNG 文件...\n')
    
    for filename in os.listdir(directory):
        if filename.lower().endswith('.png') and not filename.endswith('.bak'):
            filepath = os.path.join(directory, filename)
            try:
                result = compress_png(filepath)
                results.append(result)
                total_original += result['original']
                total_compressed += result['compressed']
                
                print(f'{filename}:')
                print(f'  原始: {result["original"]:,} 字节')
                print(f'  压缩后: {result["compressed"]:,} 字节')
                print(f'  节省: {result["saved"]:,} 字节 ({result["percent"]:.1f}%)\n')
            except Exception as e:
                print(f'压缩 {filename} 失败: {e}\n')
    
    print('总计:')
    print(f'  原始: {total_original:,} 字节')
    print(f'  压缩后: {total_compressed:,} 字节')
    print(f'  节省: {total_original - total_compressed:,} 字节 ({(1 - total_compressed/total_original)*100:.1f}%)')
    
    return results

if __name__ == '__main__':
    compress_directory('icons')
