#include <stdlib.h>
#include <stdio.h>
#include <GL/freeglut.h>

// void DISPLAY();

void ABCD();

// void DISPLAY(){
// 	glClearColor(0.5, 0.5, 0.5, 0); //
// 	glMatrixMode(GL_PROJECTION);
// 	glLoadIdentity();
// 	gluOrtho2D(-20, 20, -20, 20);
// 	glMatrixMode(GL_MODELVIEW);
// 	glLoadIdentity();
// 	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	
// 	ABCD();

// 	glutSwapBuffers();
// }

void ABCD() {
    glBegin(GL_POINTS);

    float a[3] = {1, 1, 0};    
    float b[3] = {3, 1, 0};
    float c[3] = {3, 2, 0};
    float d[3] = {2, 1, 1};

/*
    [ cos  -sin  0 ]   [x]   [cos*x - sin*y + 0*z]
    [ sin   cos  0 ] x [y] = [sin*x + cos*y + 0*z]
    [ 0     0    1 ]   [z]   [sin*0 + cos*0 + 1*z]
*/

    b[0] -= a[0];
    c[0] -= a[0];
    d[0] -= a[0];

    b[1] -= a[1];
    c[1] -= a[1];
    d[1] -= a[1];

    b[2] -= a[2];
    c[2] -= a[2];
    d[2] -= a[2];

    b[0] = 0.7*b[0] - 0.7*b[1];
    b[1] = 0.7*b[0] + 0.7*b[1];
    
    c[0] = 0.7*c[0] - 0.7*c[1];
    c[1] = 0.7*c[0] + 0.7*c[1];

    d[0] = 0.7*d[0] - 0.7*d[1];
    d[1] = 0.7*d[0] + 0.7*d[1];

    b[0] += a[0];
    c[0] += a[0];
    d[0] += a[0];

    b[1] += a[1];
    c[1] += a[1];
    d[1] += a[1];

    b[2] += a[2];
    c[2] += a[2];
    d[2] += a[2];

    printf("\n");
    for (int i = 0; i < 3; i++) {
        printf("b[%d] = %f ", i, b[i]);
    }

    printf("\n");
    for (int i = 0; i < 3; i++) {
        printf("c[%d] = %f ", i, c[i]);
    }

    printf("\n");
    for (int i = 0; i < 3; i++) {
        printf("d[%d] = %f ", i, d[i]);
    }
    printf("\n");
}

int main(int argc, char** argv){
	ABCD();
	return 0;
}