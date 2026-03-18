#include <stdlib.h>
#include <stdio.h>
#include <GL/freeglut.h>

void DISPLAY();

void DISPLAY(){
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
    gluPerspective(45, 1, 0, 15);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
    gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0);
    glClear(GL_COLOR_BUFFER_BIT);
	
	glutSolidSphere(5, 5, 10);

    glutSwapBuffers();
}


int main(int argc, char** argv){
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(600, 600);
	glutInitWindowPosition(400, 200);
	glutCreateWindow("Aula #3 do Freire BB ;)");;
	glutDisplayFunc(DISPLAY);
	glutMainLoop();
    return 0;
}