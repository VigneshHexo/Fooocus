# import os
# import sys
from modules.launch_util import repo_dir, git_clone, script_path, dir_repos


# comfy_repo = os.environ.get('COMFY_REPO', "https://github.com/comfyanonymous/ComfyUI")
# comfy_commit_hash = os.environ.get('COMFY_COMMIT_HASH', "2bc12d3d22efb5c63ae3a7fc342bb2dd16b31735")


# comfyui_name = 'ComfyUI-from-StabilityAI-Official'
# git_clone(comfy_repo, repo_dir(comfyui_name), "Inference Engine", comfy_commit_hash)
# sys.path.append(os.path.join(script_path, dir_repos, comfyui_name))


from PIL import Image
from modules.async_worker_modified import handler


task = ['small box placed in a minimal studio setup with bright light, pastel blue background',
        '',
        'ads-luxury', 
        'Speed',
        '1152×896',
        2,
        12345,
        'sd_xl_base_1.0_0.9vae.safetensors',
        'sd_xl_refiner_1.0_0.9vae.safetensors',
        'sd_xl_offset_example-lora_1.0.safetensors', 0.5,
        'None', 0.5, 'None', 0.5, 'None', 0.5, 'None', 0.5]


outputs = handler(task)
for output_num in range(task[5]):
    Image.fromarray(outputs[-1][1][output_num]).save(f'check_{output_num}.png')