import torch
from torchvision.transforms import functional as F
from PIL import Image
import os
from resize import resize
import random

class CustomRotationDataset(torch.utils.data.Dataset):
    def __init__(self, folder_path, transform_shakal=None, transform_norm=None, shakal_prob=0.3):
        self.folder_path = folder_path

        self.transform_bad = transform_shakal
        self.transform_norm = transform_norm

        self.image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]
        self.shakal_prob = shakal_prob
        
    def __len__(self):
        return len(self.image_files)
    
    def __getitem__(self, idx):
        image_path = os.path.join(self.folder_path, self.image_files[idx])
        image = Image.open(image_path)
        #image = resize(image_path)
        
        label = random.randint(0, 1)
        degree = 270*label
        rotated_image = F.rotate(image, degree)
        
        if self.transform_bad and self.transform_norm:
            prob = random.random()
            if prob < self.shakal_prob:
                rotated_image = self.transform_bad(rotated_image)
            else:
                rotated_image = self.transform_norm(rotated_image)
        
        return rotated_image, label