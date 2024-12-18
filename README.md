
# webCamSketching

Code to sketch your face live using OpenCV.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## Introduction
`webCamSketching` is a Python project that uses OpenCV to capture images from your webcam and convert them into sketches in real-time. This can be a fun and interactive way to see yourself as a sketch.

## Features
- Real-time video capture from webcam.
- Converts video frames to sketches.
- Displays both the original and sketched video feeds.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Aurjay/webCamSketching.git
   ```
2. Navigate to the project directory:
   ```sh
   cd webCamSketching
   ```
3. Install the required dependencies:
   ```sh
   pip install opencv-python
   ```

## Usage
1. Run the main script:
   ```sh
   python main.py
   ```
2. The application will open two windows:
   - One showing the original video feed.
   - One showing the sketched version of the video feed.
3. Press `Enter` to exit the application.

## Code Explanation
The main functionality of the project is contained in the `main.py` file:
- **Import OpenCV**: 
  ```python
  import cv2
  ```
- **Define helper functions**:
  - `x_cord_contour(contour)`: Calculates the x-coordinate of the centroid of a contour.
  - `makeSquare(not_square)`: Converts an image to a square dimension by adding padding.
  - `resize_to_pixel(dimensions, image)`: Resizes the image to the specified dimensions.
  - `sketch(image)`: Converts the image to a sketch.
- **Capture video from webcam**:
  ```python
  cap = cv2.VideoCapture(0)
  cap2 = cv2.VideoCapture(1)
  ```
  - Displays the original and sketched video feeds in real-time.
- **Release resources**:
  ```python
  cap.release()
  cap2.release()
  cv2.destroyAllWindows()
  ```


## License
This project does not have a license specified.


