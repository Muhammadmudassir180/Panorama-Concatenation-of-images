# Panorama Image Concatenation and Smoothing

This project provides a Python-based tool for creating a panorama by concatenating images from a specified folder. The script handles images in numerical order, ensuring no gaps between them, and applies filters to smooth the edges for a seamless panoramic image. Additionally, it includes functionality to crop out black regions from images before concatenation.

## Features

- **Image Concatenation**: Combines multiple images horizontally and vertically into a single panoramic image.
- **Edge Smoothing**: Applies Gaussian blur and feather blending techniques to remove harsh edges, creating a seamless panorama.
- **Automatic Image Cropping**: Crops out black regions from images before concatenation.
- **Numerical Sorting**: Ensures images are processed in the correct numerical order, avoiding issues with lexicographical sorting.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Matplotlib

You can install the required Python packages using:

```bash
pip install opencv-python numpy matplotlib
```

## Usage

### 1. Set Up Your Folder

Ensure your images are stored in a single folder, with filenames as numbers (e.g., 1.jpg, 2.jpg, ..., 63.jpg).

## 2. Run the Script

```bash
python panaroma.py
```

## 3. Customization

Max Images Per Row: Modify the max_images_in_row parameter in concatenate_images() to adjust the number of images concatenated horizontally.
Edge Smoothing: Adjust the feather_amount parameter in remove_edges() to control the extent of the edge smoothing effect.
Example

Place 63 images named 1.jpg to 40.jpg in the captured_images folder and run the script. The final panorama will be displayed and can be saved as needed

## Contribution

Contributions are welcome! Feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
