import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from si_image_processing_lab.pipelines.image_processing.nodes import process_image

def test_process_image():
    os.makedirs("data/03_primary", exist_ok=True)
    
    process_image(
        "data/01_raw/marte.jpg",
        "data/03_primary/test_output.jpg"
    )
    
    assert os.path.exists("data/03_primary/test_output.jpg")