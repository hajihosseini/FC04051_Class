#include"image_utils.h"

void main()
{
    BitMapFile  myImage;
    InitImage(&myImage, 600, 600, 2);//66, 215, 245
    myImage.bmHeader.colorIdx[0].r = 66;
    myImage.bmHeader.colorIdx[0].g = 215;
    myImage.bmHeader.colorIdx[0].b = 245; // 245, 66, 111
    myImage.bmHeader.colorIdx[1].r = 245;
    myImage.bmHeader.colorIdx[1].g = 66;
    myImage.bmHeader.colorIdx[1].b = 111;

    for(int f=0; f<200; f++)
    {
        int minx = 140 + f;
        int maxx = minx+20;
        int miny = 140;
        int maxy = 160;
        for(int i=0;i <600; i++)
            for(int j=0 ;j<600; j++)
            {
                if (i > minx  && i < maxx && j > miny && j< maxy)
                    myImage.bmData[i*300 + j] = 1;
                else
                    myImage.bmData[i*300 + j] = 0;
            }
        
        WriteBitmapFile(f, &myImage);
    }
}