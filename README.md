# Tone Click Boost

Analyzes clicked pixel color temperature to globally enhance warm or cool tones.

## Description

This project simulates a user clicking on a static image. It determines if the clicked pixel is predominantly 'warm' (more red than blue) or 'cool' (more blue than red). Based on this analysis, the script globally adjusts the image's red and blue channels to slightly enhance the identified dominant color temperature across the entire image. The original and adjusted images are saved as output files.

This script is designed to run non-interactively, making it suitable for headless environments.

## How to Run

1.  **Clone the repository (or save the files):**
    ```bash
    # If this were a repo: git clone <repo-url>
    # cd tone-click-boost
    ```

2.  **Install dependencies:**
    Ensure you have `pip` installed. Then, install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute the script:**
    ```bash
    python main.py
    ```

## Output

The script will generate two image files in the same directory:
-   `output_original_image.png`: The synthetic gradient image generated at the start.
-   `output_adjusted_*.png`: The image after global tone adjustment. The filename will indicate whether a 'warm' or 'cool' boost was applied, or if no change was made (`neutral_no_change`).