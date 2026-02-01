import torch
import torch.nn as nn
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import os

def evaluate_model():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Device: {device}")

    test_transforms = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    test_dir = '/dataset/test'
    
    if not os.path.exists(test_dir):
        print(f"Error: Could not find dataset at {test_dir}")
        return

    test_dataset = datasets.ImageFolder(test_dir, transform=test_transforms)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=True)
    class_names = test_dataset.classes
    print(f"Classes found: {class_names}")

    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, 2)
    
    model_path = 'best_model.pth'
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path, map_location=device))
        print("Model weights loaded successfully.")
    else:
        print(f"Error: '{model_path}' not found")
        return

    model.to(device)
    model.eval()

    all_preds = []
    all_labels = []
    correct_examples = []
    incorrect_examples = []

    print("Starting evaluation.")
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, preds = torch.max(outputs, 1)

            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

            for i in range(len(labels)):
                current_pred = preds[i].item()
                current_label = labels[i].item()
                
                if len(correct_examples) < 5 and current_pred == current_label:
                    correct_examples.append((images[i].cpu(), current_pred, current_label))
                
                elif len(incorrect_examples) < 5 and current_pred != current_label:
                    incorrect_examples.append((images[i].cpu(), current_pred, current_label))

    correct_count = sum([p == l for p, l in zip(all_preds, all_labels)])
    accuracy = 100 * correct_count / len(all_labels)
    print(f"Test Set Accuracy: {accuracy:.2f}%")


    cm = confusion_matrix(all_labels, all_preds)
    
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png')
    print("Confusion matrix saved to 'confusion_matrix.png'")
    plt.show()

    def denormalize(img):
        mean = torch.tensor([0.485, 0.456, 0.406]).view(3, 1, 1)
        std = torch.tensor([0.229, 0.224, 0.225]).view(3, 1, 1)
        return img * std + mean

    def plot_examples(examples, title):
        if not examples:
            print(f"No examples available for: {title}")
            return
            
        n_examples = len(examples)
        fig, axes = plt.subplots(1, n_examples, figsize=(3 * n_examples, 3))
        if n_examples == 1: axes = [axes]
        
        fig.suptitle(title, fontsize=16)
        
        for i, (img, pred, label) in enumerate(examples):
            img = denormalize(img)
            img = torch.clamp(img, 0, 1)
            axes[i].imshow(img.permute(1, 2, 0))
            axes[i].axis('off')
            axes[i].set_title(f"True: {class_names[label]}\nPred: {class_names[pred]}", 
                              color=('green' if pred==label else 'red'))
        plt.tight_layout()
        plt.show()

    plot_examples(correct_examples, "Correct Predictions (Sample)")
    plot_examples(incorrect_examples, "Incorrect Predictions (Sample)")

if __name__ == "__main__":
    evaluate_model()