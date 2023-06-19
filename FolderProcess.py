import argparse
parser = argparse.ArgumentParser(description='AutoRotate images and delete blury photos')
parser.add_argument('--out', type=str, default='./res', help='Loacation to folder where rotated and quality photos will be stored')
parser.add_argument('--blur', type=str, default='./blur', help='Location to folder, where blury photos will be stored')
parser.add_argument('--threshold', type=int, default=13, help='Blur threshold to determine blury images. Higher value means better quality of selection')
parser.add_argument('--device', type=str, default='cpu', help='If your GPU does not support CUDA, then choose "cpu"')
parser.add_argument('--folder', type=str, help='Folder which contains yout photos to proceed')
parser.add_argument('--model', type=str, default='./best_model_resnet50_acc99.pth', help='Location to state_dict of the model .pth')
args = parser.parse_args()

import os
import torch
from tqdm.notebook import tqdm_notebook as tqdm
from utils_lib import getmodel, blur_check, rotate, get_result, move_image_to_folder

BLURY_FOLDER = str(args.blur).replace('\\', '/')
RESULT_FOLDER = str(args.out).replace('\\', '/')
QUALITY_THRESHOLD = args.threshold
PHOTOS_PATH = str(args.folder).replace('\\', '/')
MODEL_PATH = str(args.model).replace('\\', '/')

if not os.path.exists(BLURY_FOLDER): 
    os.makedirs(BLURY_FOLDER)
if not os.path.exists(RESULT_FOLDER): 
    os.makedirs(RESULT_FOLDER)

device = torch.device("cuda")
model = getmodel.get_model(MODEL_PATH)

def proces_image(image_path):
    if blur_check.check_blury(image_path, QUALITY_THRESHOLD):
        move_image_to_folder.move_image_to_folder(image_path, BLURY_FOLDER)
    else:
        g = get_result.get_result(image_path, model, device)
        rotate.rotate(image_path, g*3, f'{RESULT_FOLDER}/')

def process_folder(folder_path):
    for filename in tqdm(os.listdir(folder_path)):
        
        if filename.endswith('.JPG'):
            image_path = os.path.join(folder_path, filename)

            proces_image(image_path)

process_folder(PHOTOS_PATH)
