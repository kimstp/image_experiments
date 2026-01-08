import matplotlib.pyplot as plt
import tifffile as tiff

def print_image_info(image, description="Image"):
    print(f"{description} shape: {image.shape}")
    print(f"{description} data type: {image.dtype}")
    print(f"{description} data max: {image.max()}")
    print(f"{description} data min: {image.min()}")

def convert_tiff(input_path, output_path):
    # Read the TIFF image
    image = tiff.imread(input_path)
    print_image_info(image, "Original Image")

    # Perform any desired processing on the image
    # For example, here we just convert it to float32
    processed_image = image.astype('float32')

    # Save the processed image as a new TIFF file
    #tiff.imwrite(output_path, processed_image)
    tiff.imwrite(output_path, image, photometric='rgb', compression='zlib')

    return processed_image

if __name__ == "__main__":

    input_tiff = "/Users/kimstp/Documents/NHMD/data/DaSSCo/Herbarium/WORKHERB0001/2025-3-6/7e9-3-05-0a-11-0c-0-001-00-000-0cf7bb-00000.tif"
    output_tiff = "output/output_image.tif"

    # Convert the TIFF image
    processed_image = convert_tiff(input_tiff, output_tiff)

    print_image_info(processed_image, "Processed Image")

    # Display the processed image
    #plt.imshow(processed_image, cmap='gray')
    processed_image = processed_image / processed_image.max()
    plt.imshow(processed_image)
    plt.title("Processed TIFF Image")
    plt.axis('off')
    plt.show()