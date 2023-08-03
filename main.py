from moviepy.editor import VideoFileClip, clips_array, vfx
from moviepy.video.fx.all import crop

length = 2
inicio = 0

# Seleciona vídeo principal
clip1 = VideoFileClip("downloaded/vid1.mp4").subclip(0, 0 + length)

# Corta vídeo original na parte de cima e de baixo, pra dar espaço pro vídeo auxiliar
clip1 = crop(clip1, y1=100, y2=800)

# Seleciona vídeo auxiliar e retira áudio
clip2 = VideoFileClip("satisfying/completo2.mp4").subclip(inicio, inicio + length).without_audio()

# Redimensiona largura do vídeo pra ficar igual do primeiro vídeo
clip2 = clip2.fx(vfx.resize, width=576)

# Combina clipes 
combined = clips_array([[clip1], [clip2]])

# Exporta vídeo editado
combined.write_videofile("edited/test.mp4")