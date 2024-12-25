import argparse
import tensorflow as tf
import numpy as np

# Function to parse arguments
def parse_args():
    parser = argparse.ArgumentParser(description="Model Prediction")
    parser.add_argument('--math', type=int, required=True, help="First feature input")
    parser.add_argument('--reading', type=int, required=True, help="Second feature input")
    parser.add_argument('--writing', type=int, required=True, help="Third feature input")
    
    return parser.parse_args()

# Load the model
def load_model():
    model = tf.keras.models.load_model('model_3b.h5')  # Replace with your model's path
    return model

# Main function to handle predictions
def make_prediction(model, input_data):
    # Make prediction
    output = model.predict(input_data)
    predicted_classes = np.argmax(output, axis=-1)
    if predicted_classes == 0:
        print("Weekly Study Hours: 5-10")
    elif predicted_classes == 1:
        print("Weekly Study Hours: < 5")
    elif predicted_classes == 2:
        print("Weekly Study Hours: > 10")

if __name__ == "__main__":
    # Parse command line arguments
    args = parse_args()
    
    # Prepare the input data as a NumPy array (single prediction)
    input_data = np.array([[args.math, args.reading, args.writing]])  # Shape: (1, 3)
    
    # Load the model
    model = load_model()
    
    # Make predictions
    make_prediction(model, input_data)