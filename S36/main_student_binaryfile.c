#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#pragma pack(push, 1)
typedef struct _Student
{
    int id;
    char name[20];
    int ssn;
    int credits;
} Student;

#pragma pack(pop)

int main()
{
    Student stds[4] =
    {
        {
            .id = 1,
            .name = "ali",
            .ssn = 123,
            .credits = 17
        },
        {
            .id = 2,
            .name = "pari",
            .ssn = 124,
            .credits = 17
        },
        {
            .id = 3,
            .name = "mari",
            .ssn = 125,
            .credits = 17
        },
        {
            .id = 4,
            .name = "zari",
            .ssn = 126,
            .credits = 17
        }
    };
    FILE* fp = fopen("students.bin", "wb");
    int size = 4;
    fwrite(&size, sizeof(int), 1, fp);
    fwrite(stds, sizeof(Student), size ,fp);
    fclose(fp);
}



void main2()
{
    FILE* fp = fopen("students.bin", "rb");
    int size = -1;
    fread(&size, sizeof(int), 1, fp);
    Student* ps = malloc(size * sizeof(Student));
    fread(ps, sizeof(Student), size, fp);
    fclose(fp);
    Student* it = ps;
    for(int i=0; i<size; i++)
    {
        // it->id;
        // it++;
        printf("%d\n%s\n%d\n%d\n", 
            ps[i].id, 
            ps[i].name, 
            ps[i].ssn, 
            ps[i].credits);
    }
    free(ps);
}