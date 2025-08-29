#include <GL/freeglut.h>
#include <stdio.h>

int n;
int i;
int *x, *y;
float r, g, b;

void DISPLAY(){
	glClearColor(0, 0, 0, 1);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-200, 200, -200, 200);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
    
    glBegin(GL_POLYGON);
        glColor3f(r, g, b);
        for (i = 0; i < n; i++) {
            glVertex2i(x[i], y[i]);
        }
    glEnd();
	
	glutSwapBuffers();
}

int main (int argc, char** argv) {

    
    printf("insira o numero de vertices:\n");
    scanf("%d", &n);

    x = (int *) malloc (n * sizeof(int));
    y = (int *) malloc (n * sizeof(int));

    printf("insira os vertices (x y):\n");
    for (i = 0; i < n; i++) {
        scanf("%d %d", &x[i], &y[i]);
    }

    printf("insira a cor (r g b):\n");
    scanf("%f %f %f", &r, &g, &b);


    glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(960, 540);
	glutInitWindowPosition(400, 200);
	glutCreateWindow("Aula #4 do Freire BB ;)");;
	glutDisplayFunc(DISPLAY);
	glutMainLoop();
	return 0;

}
