# Technical quality

## Load HCC_XYZ segmentation and CT (30%)
- [x] Both images are loaded with PyDicom, and their corresponding headers have been studied.
- [x] The slices of the CT image contain only a single acquisition.
- [x] The segmentation image is resliced according to the dicom headers.
- [x] The four regions of interest appear on a segmentation (i.e. label image).

## Rotating MIP (20%)
- [x] At least one Maximum Intensity Projection has been created.
- [x] The image and the regions are both clearly identifiable: colormaps have been correctly used, alpha fusion is used.
- [x] An interactive animation with at least 16 projections has been showed.

## Image coregistration (30%)
- [ ] A rigid motion has been implemented.
- [ ] Initial parameters are adequate.
- [ ] A loss function has been implemented.
- [ ] An optimizer has been successfully used to find the optimal parameters of a rigid motion.
- [ ] The correctness of the coregistration has been verified with visualizations.

## Thalamus region (20%)
- [ ] The thalamus has been loaded on the reference space.
- [ ] The inverse transformation has been explicitly found.
- [ ] The thalamus mask has been transformed back into the input space (i.e. the patient space).
- [ ] The thalamus mask has been visualized in the input space.

# Documentation

## Document
- [x] Written expression is correct and accurate.
- [ ] Covers all the objectives.
- [x] Shows figures of images/ROIs when necessary.
- [x] Includes discussions on why certain approaches were preferred over others.
- [x] Includes a relevant discussion of the findings and shortcomings of the project.

## Code
- [x] Is publicly accessible
- [x] It contains a Readme and is easy to follow