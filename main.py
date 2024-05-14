import pydicom
import numpy as np
import matplotlib.pyplot as plt
from skimage import transform

# Load HCC_XYZ segmentation and CT (30%)
# ● Both images are loaded with PyDicom, and their corresponding headers have been studied.
# ● The slices of the CT image contain only a single acquisition.
# ● The segmentation image is resliced according to the dicom headers.
# ● The four regions of interest appear on a segmentation (i.e. label image).


def load_dicom_image(file_path):
    """
    Load DICOM image from the specified file path.
    """
    dcm = pydicom.dcmread(file_path)
    return dcm.pixel_array


def plot_images(ct_image, seg_image):
    """
    Plot CT image and segmentation image.
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(ct_image, cmap='gray')
    axes[0].set_title('CT Image')
    axes[0].axis('off')
    axes[1].imshow(seg_image, cmap='jet')  # Adjust cmap as needed for segmentation visualization
    axes[1].set_title('Resliced Segmentation')
    axes[1].axis('off')
    plt.show()

def process_images(ct_file_path, seg_file_path):
    """
    Load and process CT and segmentation images.
    """
    ct_array = load_dicom_image(ct_file_path)
    seg_array = load_dicom_image(seg_file_path)

    plot_images(ct_array, seg_array)


# Rotating MIP (20%)
# ● At least one Maximum Intensity Projection has been created.
# ● The image and the regions are both clearly identifiable: colormaps have been correctly used, alpha fusion is used.
# ● An interactive animation with at least 16 projections has been showed.

# Image coregistration (30%)
# ● A rigid motion has been implemented.
# ● Initial parameters are adequate.
# ● A loss function has been implemented.
# ● An optimizer has been successfully used to find the optimal
# parameters of a rigid motion.
# ● The correctness of the coregistration has been verified with
# visualizations.

# Thalamus region (20%)
# ● The thalamus has been loaded on the reference space.
# ● The inverse transformation has been explicitly found.
# ● The thalamus mask has been transformed back into the input
# space (i.e. the patient space).
# ● The thalamus mask has been visualized in the input space.

# temporary files, need to confirm correct ones, currently errors
ct_file_path = "HCC_006/08-06-1999-NA-ABDPEL LIVER-65146/2.000000-PRE LIVER-29453/1-01.dcm"
seg_file_path = "HCC_006/08-06-1999-NA-ABDPEL LIVER-65146/300.000000-Segmentation-58134/1-1.dcm"
process_images(ct_file_path, seg_file_path)