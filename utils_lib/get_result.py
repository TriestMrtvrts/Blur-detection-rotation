import torch
import torchvision.transforms as transforms
from utils_lib import resize

def get_result(path, model, device):
    out_trans = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    image = resize.resize(path)
    image = out_trans(image).unsqueeze(0)

    image = image.to(device)
    model.eval()

    with torch.no_grad():
        out = model(image)
    
    return torch.argmax(out)