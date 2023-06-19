import torch
import torchvision.models as models
import os
import torchvision.models as models

def save(model, name='unnamed', folder='./'):
    os.makedirs(folder + f'/models/{name}')
    torch.save(model.state_dict(), folder + f'/models/{name}/{name}_statedict.pth')
    #torch.save(model, f'{name}.pth')


def load(model, path, folder='./'):
    name = os.path.basename(path)

    model_state_dict = torch.load(folder + f'/models/{name}/{name}_statedict.pth')
    model.load_state_dict(model_state_dict)
    #model = torch.load(f'{name}.pth')

    return model