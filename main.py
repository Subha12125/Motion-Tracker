import cv2 as cv

# Use 0 for webcam or provide a video file path
video =  cv.VideoCapture(0)  
# If you want to use a video file, uncomment the next line and provide the file path
video = cv.VideoCapture('vid1.mp4')

subtractor = cv.createBackgroundSubtractorMOG2(20, 50)
while True:
    # Read a frame from the video
    ret , frame = video.read()

    if ret:
        mask  = subtractor.apply(frame) # Apply background subtraction
        cv.imshow('Mask', mask) # Show the mask
        
        if cv.waitKey(5) == ord('X' or 'x'):
            break
    else:
        video =  cv.VideoCapture('vid1.mp4')  # Restart the video if it ends

cv.destroyAllWindows()
video.release()  # Release the video capture object