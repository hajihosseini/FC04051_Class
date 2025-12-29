#include "image_utils.h"

static int mandelbrot_escape(double cr, double ci, int max_iter)
{
    double zr = 0.0, zi = 0.0; // z = 0
    int n = 0;

    // while |z|^2 <= 4 and n < max_iter
    while ((zr * zr + zi * zi) <= 4.0 && n < max_iter)
    {
        // z = z^2 + c
        // (zr + i zi)^2 = (zr^2 - zi^2) + i(2*zr*zi)
        double zr_new = zr * zr - zi * zi + cr;
        double zi_new = 2.0 * zr * zi + ci;
        zr = zr_new;
        zi = zi_new;
        n++;
    }
    return n;
}

static void iter_to_rgb1(int n, int max_iter,
                         unsigned char *r, unsigned char *g, unsigned char *b)
{
    // Map iteration count n (0..I) to 0..255 (integer-only)
    unsigned char t = (unsigned char)((n * 255) / max_iter);

    if (n == max_iter)
    {
        *r = *g = *b = 0; // inside set -> black
    }
    else
    {
        *r = t;                              // red ramps up
        *g = (unsigned char)((t * 5) & 255); // wrap-around green
        *b = (unsigned char)(255 - t);       // blue ramps down
    }
}

void main()
{
    const int W = 800, H = 600, I = 200;
    double xmin = -2.5, xmax = 1.0;
    double spanx = xmax - xmin;
    double ymin = -1.25, ymax = 1.25;
    double spany = ymax - ymin;

    for (int s = 0; s < 50; s++)
    {
        spanx = spanx * 0.9;
        spany = spany * 0.9;
        double cx = xmin + spanx/2;
        double cy = ymin + spany/2;
        xmin = cx - spanx/2;
        ymin = cy - spany/2;
        xmax = xmin + spanx;
        ymax = ymin + spany;

        BitMapFile myImage;
        InitImage(&myImage, H, W, I);
        for (int i = 0; i < I; i++)
        {
            iter_to_rgb1(i, I,
                         &(myImage.bmHeader.colorIdx[i].r),
                         &(myImage.bmHeader.colorIdx[i].g),
                         &(myImage.bmHeader.colorIdx[i].b));
        }

        for (int py = 0; py < H; py++)
        {
            double ci = ymin + (ymax - ymin) * (double)py / (double)(H - 1);

            for (int px = 0; px < W; px++)
            {
                double cr = xmin + (xmax - xmin) * (double)px / (double)(W - 1);

                int n = mandelbrot_escape(cr, ci, I);
                myImage.bmData[py * W + px] = n;
            }
        }
        WriteBitmapFile(s, &myImage);
    }
}