import pandas as pd
import matplotlib.pyplot as plt

# Load the MNIST CSV data into a DataFrame
mnist_data = pd.read_csv('C:\Users\princ\Desktop\Hackathon\archive.zip')

# Select the image pixel columns
image_pixels = mnist_data.iloc[:, 1:]

# Plot multiple images in a single figure
fig, axes = plt.subplots(nrows=5, ncols=5, figsize=(10, 10))

for i, ax in enumerate(axes.flat):
    # Reshape the pixel values to a 28x28 image
    image = image_pixels.iloc[i].values.reshape(28, 28)
    ax.imshow(image, cmap='gray')
    ax.axis('off')  

plt.tight_layout()
plt.show()
