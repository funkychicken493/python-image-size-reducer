from PIL import Image
import os 

dir = os.path.dirname(os.path.realpath(__file__))
input_dir = os.path.join(dir, "input")
output_dir = os.path.join(dir, "output")

RESIZE_X = 100
RESIZE_Y = 100

def main():
    for _, _, files in os.walk(input_dir):
        for file in files:
            image = Image.open(os.path.join(input_dir, file))
            resized_image = image.resize((RESIZE_X, RESIZE_Y))
            resized_image.save(os.path.join(output_dir, file))

if __name__ == "__main__":
    main()