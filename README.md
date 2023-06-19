# Blur-detection-rotation
Created with KirDesktop
If you are a photographer, then you may face a problem when you need to manually rotate wrongly rotated photos and delete blurry photos. This solution does all the work for you!

My solution automatically moves blurry photos and then rotates photos to the right angle
Approximate accuracy is 98% (for unique photos)

# How to use

1. Clone the repository
2. You can delete the "TRAIN" folder if you don't care about how the model has been trained
3. Download the required libraries by running the following command:
```
pip install -r requirements.txt
```
4. IMPORTANT: Download the model from: https://drive.google.com/file/d/1GjUsPt6uMCjfQwy7GKgKaK-ojjMhKIcr/view?usp=sharing
5. Start the program as follows:
```
   python FolderProcess.py --folder C:\Photos\MY_FOLDER --device cpu --out C:\Good_Photos --blur C:\Bad_Photos --threshold 13 --model ./best_model_resnet50_acc99.pth', help='Location to state_dict of the model .pth
```

## Arguments:
```
   --device ("cpu" or "cuda", default="cpu"): If your GPU does not support CUDA, then choose "cpu"
   --threshold (default=13): Blur threshold to determine blury images. Higher value means better quality of selection
   --out: Loacation to folder where rotated and quality photos will be stored
   --blur: Location to folder, where blury photos will be stored
   --folder: Folder which contains yout photos to proceed
   --model: Location to state_dict of the model .pth
```

## WARNING
If you have CUDA support on your GPU, you should install the required PyTorch library version [here](https://pytorch.org/get-started/locally/)

## Dataset
The model has been trained on a dataset of 10,000 images. These images were taken from public sources and include a variety of subjects such as people, buildings, landscapes, animals, trees, forests, cars, and more.
