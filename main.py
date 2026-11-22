import cv2
import numpy as np
import random
import os

def generate_test_image(width=300, height=200):
    """
    Generates a synthetic test image: a horizontal gradient from blue to red.
    This image is used as the 'static image' for the project.
    """
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for x in range(width):
        # Create a gradient from pure blue (left) to pure red (right)
        blue_val = int(255 * (1 - x / (width - 1)))
        red_val = int(255 * (x / (width - 1)))
        img[:, x, 0] = blue_val  # Blue channel
        img[:, x, 2] = red_val   # Red channel
        # Green channel remains 0, creating a clear blue-to-red spectrum.
    return img

def main():
    print("Starting Color Tone Click Boost project...")

    # 1. Generate a test image (acting as the "static image")
    original_image = generate_test_image()
    height, width, _ = original_image.shape
    print(f"Generated test image: {width}x{height} pixels.")

    # Save the original image for comparison
    original_output_filename = "output_original_image.png"
    cv2.imwrite(original_output_filename, original_image)
    print(f"Original image saved as {original_output_filename}")

    # 2. Simulate a user click by picking a random pixel
    click_x = random.randint(0, width - 1)
    click_y = random.randint(0, height - 1)
    print(f"\nSimulated click at coordinates: ({click_x}, {click_y})")

    # 3. Analyze the clicked pixel's color temperature
    clicked_pixel_bgr = original_image[click_y, click_x]
    b, g, r = clicked_pixel_bgr
    print(f"Clicked pixel BGR value: ({b}, {g}, {r})")

    dominant_temp = "neutral"
    if r > b:
        dominant_temp = "warm"
    elif b > r:
        dominant_temp = "cool"

    print(f"Detected dominant temperature at clicked pixel: {dominant_temp.capitalize()}")

    # 4. Globally adjust the image based on the identified dominant temperature
    adjusted_image = original_image.copy()
    output_filename_prefix = "output_adjusted"
    
    if dominant_temp != "neutral":
        # Convert image to float for arithmetic operations
        adjusted_image_float = original_image.astype(np.float32)

        # Define adjustment parameters
        boost_amount = 25  # How much to boost the dominant color channel
        reduce_amount = 10 # How much to reduce the opposing color channel

        if dominant_temp == "warm":
            # Enhance red, slightly reduce blue
            adjusted_image_float[:, :, 2] += boost_amount  # Boost Red
            adjusted_image_float[:, :, 0] -= reduce_amount # Reduce Blue
            print(f"Adjusting image: Boosting warm tones (Red +{boost_amount}, Blue -{reduce_amount}).")
            output_filename = f"{output_filename_prefix}_warm_boost.png"
        elif dominant_temp == "cool":
            # Enhance blue, slightly reduce red
            adjusted_image_float[:, :, 0] += boost_amount  # Boost Blue
            adjusted_image_float[:, :, 2] -= reduce_amount # Reduce Red
            print(f"Adjusting image: Boosting cool tones (Blue +{boost_amount}, Red -{reduce_amount}).")
            output_filename = f"{output_filename_prefix}_cool_boost.png"
        
        # Clip pixel values to the valid [0, 255] range and convert back to uint8
        adjusted_image = np.clip(adjusted_image_float, 0, 255).astype(np.uint8)
    else:
        print("No dominant color temperature detected (Red == Blue). No global adjustment applied.")
        output_filename = f"{output_filename_prefix}_neutral_no_change.png"

    # 5. Save the adjusted (or unchanged) image
    cv2.imwrite(output_filename, adjusted_image)
    print(f"Adjusted image saved as {output_filename}")

    print("\nProject completed successfully.")

if __name__ == "__main__":
    main()