# LUNG GUARDIAN

## Our Model
Below is the summary of our CNN model which we have made using python and keras.

### Model for Tuberculosis & Pneumonia Classification

| Layer (type)                  | Output Shape             | Param #     |
|-------------------------------|--------------------------|-------------|
| conv2d (Conv2D)               | (None, 222, 222, 32)     | 896         |
| max_pooling2d (MaxPooling2D)  | (None, 111, 111, 32)     | 0           |
| conv2d_1 (Conv2D)             | (None, 109, 109, 64)     | 18496       |
| max_pooling2d_1 (MaxPooling2D)| (None, 54, 54, 64)       | 0           |
| conv2d_2 (Conv2D)             | (None, 52, 52, 128)      | 73856       |
| max_pooling2d_2 (MaxPooling2D)| (None, 26, 26, 128)      | 0           |
| flatten (Flatten)             | (None, 86528)            | 0           |
| dense (Dense)                 | (None, 128)              | 11075712    |

