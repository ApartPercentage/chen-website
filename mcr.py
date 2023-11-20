import torch
from torchvision import transforms
from PIL import Image
from transformers import pipeline


# Load your pre-trained model
def load_model_and_predict(model_path, image):
    '''try:
      # Load the model
      model = torch.load(model_path)

      # Ensure the model is in evaluation mode
      model.eval()

      # Now you can use the 'model' for making predictions
      print("Model loaded successfully!")

    except Exception as e:
      print(f"Error loading the model: {e}")'''
    pipe = pipeline('image-classification', model = model_path)
    results = pipe(image)
    score = results[0]['score']
    label = results[0]['label']
    return score, label
  
