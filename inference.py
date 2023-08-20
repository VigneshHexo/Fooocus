import os
import sys
from modules.launch_util import script_path, dir_repos
comfyui_name = 'ComfyUI-from-StabilityAI-Official'
sys.path.append(os.path.join(script_path, dir_repos, comfyui_name))

from PIL import Image
from modules.async_worker_modified import handler


task = ['small box placed in a minimal studio setup with bright light, pastel blue background',
        '',
        'ads-luxury', 
        'Speed',
        '1152×896',
        2,
        12345,
        2,
        'sd_xl_base_1.0_0.9vae.safetensors',
        'sd_xl_refiner_1.0_0.9vae.safetensors',
        'sd_xl_offset_example-lora_1.0.safetensors', 0.5,
        'None', 0.5, 'None', 0.5, 'None', 0.5, 'None', 0.5]


outputs = handler(task)
for output_num in range(task[5]):
    Image.fromarray(outputs[-1][1][output_num]).save(f'check_{output_num}.png')