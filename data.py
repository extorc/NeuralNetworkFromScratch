import numpy as np

def get_mnist():
    with np.load(r"C:\Users\mitta\Desktop\NeuralNetworkFromScratch\data\mnist.npz") as f:
        images, labels = f["x_train"], f["y_train"]
    images = images.astype("float32") / 255
    images = np.reshape(images, (images.shape[0], images.shape[1] * images.shape[2]))
    labels = np.eye(10)[labels]
    return images, labels
