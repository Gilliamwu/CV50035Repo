"# CV50035Repo" 
## Key functionalities:
CNN with TF.ipynb : visualization of CNN we have used. 

Video Generation.ipynb : how we extract frames, apply model and output a video.

Sliding Window.ipynb : shows result of performing rolling window on a frame

Filter Preview.ipynb : Testing of combination of every filters.

Filters Models.ipynb : Testing the accuracy of combination of every filters and models.

Result_Example_adaptivethreshold.mov: Example of video output.

## Structure
/filters:

Contains all the models we have tried to implemented. Gabor, invariant Gabor, Otsu, and all morphological filters (blackhat, tophat, gradient and 2gradients). Ipython notebook is attached for reference and .py file contains all the cleaned code.


/helper:

Formatted code to get images from specific location, rename every files in certain folder, rolling_window to apply sliding window on images, shade_area to highlight crack on video and util with useful functions.

/preprocessing:

Contains functions that do shadow reudction for filters.

/models:

Contains some models we tried.

video.py: util code to extract frames from video, and generate video out of frames.
