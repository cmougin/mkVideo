#include <iostream>
#include <stdio.h>
#include <string>
#include "opencv2/opencv.hpp"
#include "opencv2/highgui/highgui.hpp"

//
using namespace std;
using namespace cv;

int premiermain(int argc, char *argv[]) {
    unsigned aa,bb;
    VideoWriter outputVideo;

    cout << "début du nouveau programme\n";
    cout << argc << argv[1] << argv[2];
        Mat dst, im = imread(argv[1]);
    if (im.empty()) {
        cout<< "impossible de lire l image\n";
        return -2;
    }

    outputVideo.open(argv[2], CV_FOURCC('D','I','V','X'), 24, Size(1280,720), true);
    if (!outputVideo.isOpened())
    {
        cout  << "Could not open the output video for write: " << argv[2] << endl;
        return -1;
    }

    for (aa=bb=0; aa<10; aa++, bb+=2) {
        Mat dst2 (im, Rect(aa, bb, 800+aa, 600+bb));
        Size size(1280, 720); // 720 rows x 1280 cols x 3 uchars => 3840 uchar par row; step=[3840, 3]
        resize(dst2, dst,size);
        imshow("en grand", dst);
        printf( "row=%d, cols=%d, step=(%d,%d).\n",dst.rows, dst.cols, dst.step[0], dst.step[1]);
        outputVideo << dst;
    }
    waitKey(0);

    cout << "fin. le programme se termine normalement.";
    return 0;
}
