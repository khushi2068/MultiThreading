import cv2

def convert_to_gray(input_path, output_path):
    try:
        # Load image
        img = cv2.imread(input_path)
        if img is None:
            print(f"Error: Unable to load image '{input_path}'.")
            return
        
        # Convert to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Write grayscale image
        cv2.imwrite(output_path, gray_img)
        print(f"Image '{input_path}' converted to grayscale and saved as '{output_path}'")
    except Exception as e:
        print(f"Error while processing image '{input_path}': {e}")

if __name__ == "__main__":
    input_path = "./input_images/marvel.png"
    output_path = "output_image_gray.jpg"

    convert_to_gray(input_path, output_path)
