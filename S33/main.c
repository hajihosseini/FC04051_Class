#include <stdio.h>

// typedef char* string;

struct _pair 
{
    int x;
    double y;
} w;

typedef struct _student
{
    int student_id;
    char fname[20];
    char lname[20];
    double GPA;
    int national_id;
} Student;

void print_student(struct _student s)
{
    printf("id: %d\nname: %s\nlname: %s\nGPA: %lf\nNATID: %d\n",
        s.student_id, s.fname, s.lname, s.GPA, s.national_id);
}

void inc(int x)
{
    x++;
}

void mosbat_student(struct _student* s, double inc)
{
    (*s).GPA = (*s).GPA + inc;
    s->GPA += inc;
}

void mstrcpy(char* pchsrc, char* pchtgt)
{
    int i =-1;
    while(pchsrc[++i])
        pchtgt[i] = pchsrc[i];
}

struct _student* make_student(int stdid, char* fname, char* lname, double GPA, int natid)
{
    struct _student* ps = malloc(sizeof(struct _student));
    ps->student_id= stdid;
    ps->GPA = GPA;
    ps->national_id = natid;
    mstrcpy(fname, ps->fname);
    mstrcpy(lname, ps->lname);
    return ps;
}

void main()
{
    inc(5);
    struct _student zari  = {
        .student_id = 0xffffffff,
        .fname = "AAAAAAAAAAAAAAAAAAA",
        .lname = "LLLLLLLLLLLLLLLLLLL",
        .GPA = 18.1,
        .national_id = 0xaaaaaaaa
    };
    struct _student* ali = make_student(1,"ali", "kasaei", 19.1, 2);
    print_student(*ali);
    free(ali);

    Student students[100];
    // print_student(zari);
    // mosbat_student(&zari, 0.25);
    // print_student(zari);





    // struct _student ali;

    // zari.GPA = 19;
    // // zari.fname[0] = 'B';
    // *(((char*)&zari)+4) = 'B';
    // char* zaribptr = (char*) &zari;
    // zaribptr[4] = 'B';

    // print_student(zari);

    // w.x = 1;
    // w.y = 1.1;
    // struct _pair f;

    // printf("%d, %lf", w.x, w.y);
}