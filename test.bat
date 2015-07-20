copy/b D:\TEMP\bis.raw+D:\TEMP\bis.raw tmp.bin
<tmp.bin "D:\Utilisateurs\FR20340\Desktop\ffmpeg-20140818-git-3c19744-win64-shared\bin\ffmpeg.exe" -y -f rawvideo -vcodec rawvideo -s 1280x720 -pix_fmt bgr24 -framerate 1/2 -i - -r 2 -an -vcodec libx264 -preset slow -pix_fmt yuv420p "D:\TEMP\output_ffmpeg2.mp4"
