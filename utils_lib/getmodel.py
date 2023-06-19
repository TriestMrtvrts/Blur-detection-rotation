import torch
import torch.nn as nn
import torchvision.models as models

def get_model(path):
    model = models.resnet50(weights=None)
    n_inputs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(n_inputs, 1024),
        nn.ReLU(),
        nn.Dropout(p=0.4),
        nn.Linear(1024, 1024),
        nn.ReLU(),
        nn.Dropout(p=0.4),
        nn.Linear(1024, 2)
    )

    model_state_dict = torch.load(path, map_location=torch.device('cuda'))
    model.load_state_dict(model_state_dict)

    device = torch.device("cuda")

    model.to(device)
    model.eval()

    return model