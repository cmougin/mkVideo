#include <iostream>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string>
#include "opencv2/opencv.hpp"
#include "opencv2/highgui/highgui.hpp"

using namespace std;
using namespace cv;

int main(int argc, char *argv[]) {
    VideoWriter outputVideo;
    char *inputFile=NULL, *outputFile=NULL;
    int c, sizeX=720, sizeY=576, duree=1, fps=24;
    int panX, panY, panXX, panYY, panZ, panT, panZZ, panTT;
    int i, nbframes;

    panX=panY=panZ=panT=panXX=panYY=panZZ=panTT=0;
    cout << "début du nouveau programme\n";

    while ((c = getopt (argc, argv, "i:s:d:f:o:p:")) != -1) {
    switch (c)
    {
       case 'i':
         inputFile = optarg;
         break;
       case 'o':
         outputFile = optarg;
         break;
       case 'd':
         duree=atoi(optarg);
         break;
       case 'f':
           fps=atoi(optarg);
         break;
       case 's':
           cout << "'"<<optarg<<"'";
           sscanf(optarg,"%d,%d ", &sizeX, &sizeY);
         break;
       case 'p':
           cout << "'"<<optarg<<"'";
           sscanf(optarg,"%d,%d,%d,%d-%d,%d,%d,%d ", &panX, &panY, &panXX, &panYY, &panZ, &panT, &panZZ, &panTT);
         break;
       case '?':
           fprintf (stderr, "Option requires an argument.\n");
         return 1;
       default:
         abort ();
    }}
    printf("input:%s, output=%s, duree=%d, fps=%d, size=%dx%d\n",inputFile, outputFile, duree, fps, sizeX, sizeY);
    printf("pan: %d,%d,%d,%d -> %d,%d,%d,%d\n", panX, panY, panXX, panYY, panZ, panT, panZZ, panTT);

    Mat dst, im = imread(inputFile);
    if (im.empty()) {
        cout<< "impossible de lire l image\n";
        return -2;
    }

    if (remove(outputFile)!=0)
        perror("error deleting file");
    outputVideo.open(outputFile, CV_FOURCC('X','V','I','D'), fps, Size(sizeX, sizeY), true);
    if (!outputVideo.isOpened())
    {
        cout  << "Could not open the output video for write: " << outputFile << endl;
        return -1;
    }

    if (panXX==0 || panYY==0 || panZZ==0 || panTT==0) {
        cout << "pano abandonné, un paramètre est nul\n";
        return -3;
    }
// essai de génération d'une vidéo un décalant une fenetre d'un pas de 1x2 sur une image source.
    //panXX+=panX;
    //panYY+=panY;
    //panZZ+=panZ;
    //panTT+=panT;
    nbframes=fps*duree;
    printf("row=%d, cols=%d, step=(%d,%d).\n",dst.rows, dst.cols, dst.step[0], dst.step[1]);
    Size size(sizeX, sizeY); // 720 rows x 1280 cols x 3 uchars => 3840 uchar par row; step=[3840, 3]

    for (i=0; i<nbframes; i++) {
        int X, Y, W, H;
        X=panX + (panZ - panX)*i/nbframes;
        Y=panY + (panT - panY)*i/nbframes;
        W=(panXX - panX)+((panZZ - panZ) - (panXX - panX)) *i/nbframes;
        H=(panYY - panY)+((panTT - panT) - (panYY - panY)) *i/nbframes;
        //printf("(%d,%d,%d,%d)", X, Y, W, H);
        Mat dst2 (im, Rect(X, Y, W, H));
        resize(dst2, dst,size);
        //imshow("en grand", dst);
        //printf(" : ok.\n");
        outputVideo << dst;
    }
    waitKey(0);

    cout << "fin. le programme se termine normalement.";
    return 0;
}
