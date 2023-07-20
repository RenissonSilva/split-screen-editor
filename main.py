from moviepy.editor import VideoFileClip, clips_array
from moviepy.video.fx.all import crop

length = 2
inicio = 0

clip1 = VideoFileClip("downloaded/vid1.mp4").subclip(0, 0 + length)
clip2 = VideoFileClip("satisfying/2.mp4").subclip(inicio, inicio + length).without_audio()

# (w, h) = clip2.size
# clip2 = crop(clip2, width=574)

combined = clips_array([[clip1, clip2]])

combined.write_videofile("edited/test.mp4")