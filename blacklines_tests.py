from skimage.io import imread, imsave
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import hashlib



if __name__ == "__main__":
    # filename to test
    #filename = "/Users/kimstp/Documents/NHMD/data/DaSSCo/Herbarium/Black_lines/WORKHERB0002/7e9-5-06-0b-2e-10-1-001-01-000-004b40-00000.tif"
    filename = "/Users/kimstp/Documents/NHMD/data/DaSSCo/Herbarium/WORKHERB0001/2025-3-6/7e9-3-05-0a-11-0c-0-001-00-000-0cf7bb-00000.tif"

    # Calculate the MD5 hash of the image
    with open(filename, "rb") as f:
        file_hash_source = hashlib.md5(f.read())
    checksum = file_hash_source.hexdigest()
    print(f"MD5 checksum of the image: {checksum}")



    # Load the image
    image = imread(filename)

    # Check if the image is loaded correctly
    if image is None:
        print("Failed to load the image.")
    else:
        print("Image loaded successfully.")
        print(f"Image shape: {image.shape}")
        print(f"Image data type: {image.dtype}")


    # Create fake black lines
    image[5500:5502, :] = 0  # Set a small region to black

    # Save the modified image
    blackline_filename = filename.replace(".tif", "_blacklines.tif")
    imsave(blackline_filename, image)

    # Calculate the MD5 hash of the modified image
    with open(blackline_filename, "rb") as f:
        file_hash_blackline = hashlib.md5(f.read())
    checksum_blackline = file_hash_blackline.hexdigest()
    print(f"MD5 checksum of the modified image: {checksum_blackline}")



    # Display the modified images
    plt.figure()
    plt.imshow(img_as_float(image))

    plt.show()
