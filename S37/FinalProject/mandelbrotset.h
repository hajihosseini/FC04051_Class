#ifndef __MANDELBROTSET_H__
#define __MANDELBROTSET_H__

#include"defs.h"
#include<math.h>


int get_mbs_iter(double x, double y)
{
    // TODO
    return 0;
}

void hsv_to_rgb(int hue, int min, int max, COLORINDEX* p)
{
    // TODO
}

void UpdateImageData(ImageState* state)
{
    for(int x=0; x<state->width; x++)
        for(int y=0; y<state->height; y++)
        {
            // x,y => dx,dy
            // dx,dy => rx, ry
            // rx = nx * cos(state->angle) + ny * sin(state->angle);
            // ry = -nx * sin(state->angle) + ny * cos(state->angle);

            // int iter = get_mbs_iter(rx, ry);
            // state->bmFileData.bmData[y * state->width + x] = iter;
        }
        
    for(int i=0; i<256; i++)
    {
        int hue = (int) ((i / 255)/360);
        hsv_to_rgb(hue, 100, 100, &(state->bmFileData.bmHeader.colorIdx[i]));
    }
}

void ChangeCenter(ImageState* state, double newcx, double newcy, int steps)
{
    // TODO

    for(int i=0;i<steps; i++)
    {
        // TODO
        UpdateImageData(state);
        WriteBitmapFile(state->image_count++, & state->bmFileData);
    }
}

void ChangeZoom(ImageState* state, double zoom, int steps)
{
    // TODO
    for(int i=0; i<steps; i++)
    {
        // TODO
        UpdateImageData(state);
        WriteBitmapFile(state->image_count++, & state->bmFileData);
    }
}

void ChangeRotation(ImageState* state, double angle, int steps)
{
    // TODO
    double angle_step = angle / steps;
    for(int i=0; i<steps; i++)
    {
        state->angle += angle_step;
        UpdateImageData(state);
        WriteBitmapFile(state->image_count++, & state->bmFileData);
    }
}

void Hold(ImageState* state, int steps)
{
    // TODO
    for(int i=0; i<steps; i++)
    {
        //TODO
        WriteBitmapFile(state->image_count++, & state->bmFileData);
    }
}

#endif