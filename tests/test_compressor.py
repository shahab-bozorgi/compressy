import os
from compressy import compress_to_webp

def test_compress_image():
    input_path = "tests/test.jpg"  
    output_path = "tests/output.jpg"

    compress_to_webp(input_path, output_path, quality=50, max_width=500)
    
    assert os.path.exists(output_path), "Output file was not created."
    assert os.path.getsize(output_path) < os.path.getsize(input_path), "Output file is not smaller than input."

    print("Test passed: Image compressed successfully.")
    
if __name__ == "__main__":
    test_compress_image()
