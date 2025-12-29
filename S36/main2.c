#include<stdio.h>
#include<stdlib.h>

int read_cmds(FILE* fp, char*** cmds)
{
    *cmds = malloc(sizeof(char*) * 100);
    int bytes_read = 1;
    char buf[100];
    int count = 0;
    while (bytes_read > 0)
    {
        bytes_read = fscanf(fp, "%s", buf);
        if (bytes_read > 0)
        {
            int strlen = 0;
            while(buf[strlen]) strlen++;
            char* cmdbuf = malloc(strlen+1);
            int i=0;
            while(buf[i])
            {
                cmdbuf[i] = buf[i];
                i++; 
            }
            cmdbuf[i] = 0;
            (*cmds)[count] = cmdbuf;
            count++;
        }
    }
    return count;
}

void main(int argc, char** argv)
{
    if (argc != 2)
    {
        printf("Usage: \n\t program.exe <incfgfile>\n");
        return;
    }

    FILE* fp = fopen(argv[1], "r");
    int width,height;    
    char c;
    fscanf(fp, "%d%*c%d", &width, &height);

    double minx, maxx, miny, maxy;
    fscanf(fp, "%lf%*c%lf%*c%lf%*c%lf", &minx, &maxx, &miny, &maxy);
    char cmd[20];
    int zoom, steps;
    
    fscanf(fp, "%s %d:%d", cmd, &zoom, &steps);

    char** cmds;
    int count = read_cmds(fp, &cmds);
    fclose(fp);
    printf("resolution: %d * %d\n", height, width);
    printf("min/max x/y: %lf %lf %lf %lf\n", minx, miny, maxx, maxy);
    printf("first cmd: %s %d:%d\n", cmd, zoom, steps);

    printf("... plus %d more items", count);
    for(int i = 0; i<count; i++)
    {
        printf("%d %s\n", i, cmds[i]);
    }

    for(int i = 0; i<count; i++)
    {
        free(cmds[i]);
    }
    free(cmds);
    printf("done");
}


void main4()
{
    int a=5;
    double b = 2.3;
    char buf[100], buf2[100];
    FILE* fp = fopen("b.txt", "r");
    fscanf(fp, "%d%lf%s%s", &a, &b, buf, buf2);
    fclose(fp);
    printf("%d\n%lf\n%s\n%s\n", a, b, buf, buf2);
}

void main678()
{
    int a=5;
    double b = 2.3;
    FILE* fp = fopen("b.txt", "w");
    fprintf(fp, "id: %d, percentage: %lf", a, b);
    fclose(fp);
}