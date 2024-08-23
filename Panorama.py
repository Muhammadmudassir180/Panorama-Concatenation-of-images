import cv2
import numpy as np
import os
import glob


def crop_black_borders(image, threshold=20):

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold to get the mask of black areas
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
        cropped_image = image[y:y+h, x:x+w]
        return cropped_image

    return image


def concatenate_images(images, max_images_in_row=5):

    rows = []
    temp_row = []
    image_count = len(images)
    counter = 0

    for i in range(image_count):
        temp_row.append(images[i])

        # counter += 1
        print("iiiii", i)
        # print("counter", counter)

        if (i+1) % max_images_in_row == 0:
            # print("i+1", i+1)
            # Ensure all images in temp_row have the same height
            heights = [img.shape[0] for img in temp_row]
            if len(set(heights)) > 1:
                print("Inconsistent heights detected, resizing...")
                target_height = min(heights)
                temp_row = [cv2.resize(
                    img, (img.shape[1], target_height)) for img in temp_row]

            rows.append(cv2.hconcat(temp_row))
            temp_row = []

    if temp_row:
        heights = [img.shape[0] for img in temp_row]
        if len(set(heights)) > 1:
            print("Inconsistent heights detected, resizing...")
            target_height = min(heights)
            temp_row = [cv2.resize(img, (img.shape[1], target_height))
                        for img in temp_row]

        rows.append(cv2.hconcat(temp_row))

    widths = [row.shape[1] for row in rows]
    if len(set(widths)) > 1:
        target_width = min(widths)
        rows = [cv2.resize(row, (target_width, row.shape[0])) for row in rows]

    final_image = cv2.vconcat(rows, 1000)

    return final_image


def remove_edges(image, kernel_size=5):

    return cv2.bilateralFilter(image, 10, 10, 100)


def create_panorama_from_folder(folder_path):
    images = []
    counter = 0

    file_list = sorted([f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.png'))],
                       key=lambda x: int(os.path.splitext(x)[0]))

    file_paths = [os.path.join(folder_path, f) for f in file_list]
    print("folder_path", file_paths)
    for image in file_paths:
        img = cv2.imread(image)
        # counter += 1
        img = crop_black_borders(img)
        img = cv2.resize(img, (120, 60))
        images.append(img)
        # cv2.imshow("Images", img)

    if not images:
        print("No images found in the folder.")
        return None

    first_image = images[0]
    target_size = (first_image.shape[1], first_image.shape[0])

    panorama = concatenate_images(images)
    smoothed_panorama = remove_edges(panorama)

    # Show the final panorama
    cv2.imshow("Panorama", smoothed_panorama)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return smoothed_panorama


folder_path = 'path to your folder images'
create_panorama_from_folder(folder_path)
