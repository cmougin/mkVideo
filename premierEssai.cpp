#include <iostream>
#include <stdio.h>
#include "opencv2/opencv.hpp"
#include "opencv2/highgui/highgui.hpp"

//exemple trouvé sur https://trac.ffmpeg.org/wiki/Create%20a%20video%20slideshow%20from%20images
//	ffmpeg -framerate 1/5 -i img%03d.png -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4
//
//exemple trouvé sur http://zulko.github.io/blog/2013/09/27/read-and-write-video-frames-in-python-using-ffmpeg/
//command = [ FFMPEG_BIN,
//        '-y', # (optional) overwrite output file if it exists
//        '-f', 'rawvideo',
//        '-vcodec','rawvideo',
//        '-s', '1280x720', # size of one frame
//        '-pix_fmt', 'rgb24',
//        '-r', '24', # frames per second
//        '-i', '-', # The imput comes from a pipe
//        '-an', # Tells FFMPEG not to expect any audio
//        '-vcodec', 'mpeg'",
//        'my_output_videofile.mp4' ]
//
// exemple trouvé sur https://sites.google.com/site/linuxencoding/ffmpeg-tips
// cat $(ls -t *jpg) | ffmpeg -f image2pipe -vcodec mjpeg -r 25 -i - -i backwards.wav -vcodec libx264 -preset slow -crf 20 -threads 0 -acodec flac output.mkv
// NB:
//preset
//Sets the time that FFMPEG will take to compress the video. The slower,
//the better the compression rate. Possibilities are: ultrafast,superfast,
//veryfast, faster, fast, medium (default), slow, slower, veryslow,
//placebo.
// exemple élaboré et testé avec succès sous Linux, avec des petites images, les très grandes semblant problématiques
// cat Nov17_3?.JPG|avconv -y -c:v mjpeg -f image2pipe -framerate 1/2 -i - -an -r 24 -c:v libx264 -bitrate 3000k -pix_fmt yuv420p tmp.mp4
//
using namespace std;
using namespace cv;

int main() {
    FILE *in, *bis;

    char executable[]="D:\\Utilisateurs\\FR20340\\Desktop\\ffmpeg-20140818-git-3c19744-win64-shared\\bin\\ffmpeg.exe \
    -y -f rawvideo -vcodec rawvideo -s 1280x720 -pix_fmt bgr24 -framerate 1/2 -r 2 -i - -r 2 -an -preset veryfast -pix_fmt yuv420p \
    D:\\TEMP\\output_ffmpeg.avi";
    // -vcodec libx264

    cout << "début du programme\n";
    cout << executable << endl;
    if(!(in = popen(executable, "w"))){
        cerr << "le pOpen() s'est mal passé";
        return 1;
    }

    if (!(bis = fopen("D:\\TEMP\\bis.raw","w"))){
        cerr << "le fopen s'est mal passé";
        return 2;
    }
    Mat im = imread("D:\\Google Drive\\mes données\\photos\\TMP.JPG");
    if (im.empty()) {
        cout<< "impossible de lire l image\n";
        return -2;
    }

    Mat dst;
    unsigned aa,bb;
    for (aa=bb=0; aa<10; aa++, bb+=2) {
        Mat dst2 (im, Rect(aa, bb, 800+aa, 600+bb));
        Size size(1280, 720); // 720 rows x 1280 cols x 3 uchars => 3840 uchar par row; step=[3840, 3]
        resize(dst2, dst,size);
        imshow("en grand", dst);
        printf( "row=%d, cols=%d, step=(%d,%d).\n",dst.rows, dst.cols, dst.step[0], dst.step[1]);

        //cf. http://docs.opencv.org/opencv_tutorials.pdf
        int i,j,k=0;
        //cf. http://galaxy.eti.pg.gda.pl/katedry/kiw/pracownicy/Mariusz.Szwoch/Didactics/PiZI/opencv_tutorials.pdf
        Mat_<Vec3b> _I = dst;
        char r,g,b,d;

        for (i=0; i<dst.rows ; i++) {
            for (j=0 ; j<dst.cols ; j++) {
                //k+=fprintf(in, "%c%c%c", _I(i,j)[0], _I(i,j)[1], _I(i,j)[2]);
                b=aa*25;
                g=i*255/dst.rows;
                r=(j==dst.cols/2)?255:0; r|=j&128;
                d=fprintf(in, "%c%c%c", b,g,r);
                k+=d;
                if (d!=3) cerr << "erreur d=" << d << "\n";
            }
        }
        cout << k << " octets ecrits.\n";


        uchar *p;
        for (i=1 ; i<dst.rows ; i++) {
            for (j=0 ; j<dst.cols ; j++) {
                p = j*dst.step[1]+dst.ptr<uchar>(i);
                k+=fwrite((void*)p, dst.step[1], 1, in);
                fwrite((void*)p, 1, 3, bis);
            }
        }
        cout << k << " octets ecrits.\n";


    }
    pclose(in);
    waitKey(0);

    cout << "fin. le programme se termine normalement.";
    return 0;
}
