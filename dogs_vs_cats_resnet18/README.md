# Dogs vs Cats CNN Classifier

**Deep Learning Assignment**

This project implements a binary image classifier using transfer learning with ResNet18 to distinguish between dogs and cats. The implementation uses PyTorch with comprehensive data augmentation, training monitoring, and evaluation metrics.

---

## 📁 Repository Structure

```
Day3_Assignment_YourName/
├── train.py                # Complete training script
├── evaluate.py             # Evaluation script
├── best_model.pth          # Saved model weights
├── training_curves.png     # Loss and accuracy plots
├── confusion_matrix.png    # Confusion matrix
└── README.md               # Report of the project along with instructions
```

---

## 🚀 Features

- Transfer learning with pre-trained ResNet18 architecture
- Comprehensive data augmentation pipeline for training
- Real-time loss and accuracy tracking during training
- Automatic model checkpointing (saves best validation accuracy)
- Learning rate scheduling with ReduceLROnPlateau
- Confusion matrix visualization for evaluation
- Sample predictions display (correct and incorrect)
- GPU acceleration with automatic fallback to CPU

---

## 🛠️ Requirements

The following Python libraries are required:

```bash
pip install torch torchvision matplotlib numpy scikit-learn seaborn
```

---

## ▶️ How to Run

### Training

1. Ensure your dataset is organized in the required folder structure
2. Open a terminal and navigate to the project directory
3. Run the training script:

```bash
python train.py
```

4. The script will:
   - Load and augment training data
   - Train the model for 10 epochs
   - Save the best model as `best_model.pth`
   - Generate training curves

### Evaluation

After training is complete:

```bash
python evaluate.py
```

This will:
- Load the trained model
- Evaluate on the test set
- Display test accuracy
- Generate confusion matrix
- Show sample predictions

---

## 🖼️ Output

### Training Phase

**Console Output:**
```
Initializing Data Loaders...
Training samples: 400
Validation samples: 50
Using device: cuda

Starting training...
Epoch [1/10]
 Train Loss: 0.2341, Train Acc: 91.23%
 Val Loss: 0.1876, Val Acc: 93.45%
Saved best model with val_acc: 93.45%
```

**Generated Files:**
- `best_model.pth` - Saved model weights
- `training_curves.png` - Loss and accuracy plots over epochs

### Evaluation Phase

**Console Output:**
```
Device: cuda
Model weights loaded successfully.
Starting inference...
Test Set Accuracy: 94.67%
```

**Generated Files:**
- `confusion_matrix.png` - Classification confusion matrix
- Sample prediction visualizations displayed on screen

---

## 📊 Model Architecture

### Transfer Learning Approach

- **Base Model:** ResNet18 (pre-trained on ImageNet)
- **Frozen Layers:** All convolutional layers
- **Custom Classifier:** Final fully connected layer
  - Input: 512 features
  - Output: 2 classes (cats, dogs)

### Hyperparameters

| Parameter | Value |
|-----------|-------|
| Input Size | 224×224×3 |
| Batch Size | 32 |
| Learning Rate | 0.001 |
| Optimizer | Adam |
| Loss Function | CrossEntropyLoss |
| Epochs | 10 |
| Scheduler | ReduceLROnPlateau (patience=3) |

---

## ⚙️ Data Augmentation

### Training Transforms

- Resize to 256×256
- Random crop to 224×224
- Random horizontal flip
- Random rotation (±15°)
- Color jitter (brightness, contrast, saturation, hue)
- Random affine transformation (translation)
- ImageNet normalization

### Validation/Test Transforms

- Resize to 256×256
- Center crop to 224×224
- ImageNet normalization

---

## 📌 Key Implementation Details

### Model Checkpointing

The training script automatically saves the model with the best validation accuracy:

```python
if val_acc > best_val_acc:
    best_val_acc = val_acc
    torch.save(model.state_dict(), 'best_model.pth')
```

### Learning Rate Scheduling

ReduceLROnPlateau reduces learning rate when validation loss plateaus:

```python
scheduler = optim.lr_scheduler.ReduceLROnPlateau(
    optimizer, mode='min', patience=3, factor=0.5
)
```

### Visualization

Both scripts include comprehensive visualization:
- **Training:** Loss and accuracy curves
- **Evaluation:** Confusion matrix and sample predictions with denormalization

---

## 📈 Results

| Metric | Accuracy |
|--------|----------|
| Training Accuracy | 90.75% |
| Validation Accuracy | 99.00% |
| Test Accuracy | 96.00% |

This indicates that there was no overfitting in the model. The lower training accuracy is due to the number of data augmentation methods used and due to the smaller nature of the dataset to optimize for limited compute power.

---

## 👤 Author

Diyaansh K
Day 3 Assignment - Computer Vision