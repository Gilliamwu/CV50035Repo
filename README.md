"# CV50035Repo" 
## Key functionalities:
CNN with TF.ipynb : visualization of CNN we have used. 

video generation clean version with filters.ipynb: how we extract frames, apply model and output a video.

Filter Preview.ipynb : Testing of combination of every filters.

FiltersModels.ipynb : Testing the accuracy of combination of every filters and models.


## Structure
Filters:

Contains all the models we have tried to implemented. Gabor, invariant Gabor, Otsu, and all morphological filters (blackhat, tophat, gradient and 2gradients). Ipython notebook is attached for reference and .py file contains all the cleaned code.


Helpers:

Formatted code to get images from specific location, rename every files in certain folder, rolling_window to apply sliding window on images, shade_area to highlight crack on video and util with useful functions.

Preprocessing:

It contains functions that do shadow reudction for filters.

video.py: util code to extract frames from video, and generate video out of frames.
