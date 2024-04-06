import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import cv2
import os

# Define the parameters
train_directory = 'C:\python_mini_project\dataset\data'  # Path to the directory containing the training dataset
batch_size = 32
epochs = 20
image_size = (224, 224)  # Desired image size for training
num_classes = 2 # Number of classes in your classification problem

# Create an ImageDataGenerator for data augmentation and preprocessing
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,  # Scale pixel values between 0 and 1
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
)

# Load the training dataset using the ImageDataGenerator
train_data = train_datagen.flow_from_directory(
    train_directory,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='categorical'
)

# Define the model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(image_size[0], image_size[1], 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(num_classes, activation='softmax')  # Output layer with num_classes and softmax activation
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_data, epochs=epochs)

# Capture an image using the default camera
camera = cv2.VideoCapture(0)
ret, image = camera.read()

# Check if the image is captured successfully
if ret:
    # Display the captured image
    cv2.imshow('Captured Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Preprocess the captured image for prediction
    image = cv2.resize(image, image_size)  # Resize the image to match the training image size
    image = image / 255.0  # Normalize pixel values between 0 and 1

    # Reshape the image to match the input shape of the model
    image = image.reshape(1, image_size[0], image_size[1], 3)

    # Make predictions on the image using the trained model
    predictions = model.predict(image)

    # Get the predicted class index
    predicted_class_index = tf.argmax(predictions[0]).numpy()

    # Get the class labels
    class_labels = train_data.class_indices

    # Reverse the class indices to get the class labels
    reverse_labels = dict((v, k) for k, v in class_labels.items())

    # Check if the predicted class label is present in the dataset
    predicted_class_label = reverse_labels[predicted_class_index]
    if os.path.exists(os.path.join(train_directory, predicted_class_label)):
        print('The captured image is present in the dataset.')
    else:
        print('The captured image is NOT present in the dataset.')
else:
    print('Failed to capture image.')

# Release the camera
camera.release()