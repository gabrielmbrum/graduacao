#include <stdlib.h>
#include <stdio.h>
#include <GL/freeglut.h>

void DISPLAY();

void DISPLAY(){
	glClearColor(1, 0, 1, 1); //
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-200, 200, -200, 200);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glutSwapBuffers();
}

int main(int argc, char** argv){
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(960, 540);
	glutInitWindowPosition(400, 200);
	glutCreateWindow("Aula #1 do Freire BB ;)");;
	glutDisplayFunc(DISPLAY);
	glutMainLoop();
	return 0;
}