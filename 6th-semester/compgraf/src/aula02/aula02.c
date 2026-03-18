#include <stdlib.h>
#include <stdio.h>
#include <GL/freeglut.h>

void DISPLAY();

void DesenhaJamaica();

void DesenhaQuadrados();

void DesenhaX();

void DesenhaPontos();

void DesenhaCirculo();

void DISPLAY(){
	glClearColor(0.5, 0.5, 0.5, 0); //
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-200, 200, -200, 200);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	
	DesenhaJamaica();

	glutSwapBuffers();
}

// dist euclid = (x1 - x2)² + (y1 - y2)²

void DesenhaPontos() {
	glColor3f(1, 1, 1);
	glBegin(GL_POINTS);
	for (int x = -200; x <= 200; x += 2) 
	for (int y = -200; y <= 200; y += 2) 
		glVertex3f(x, y, 0);
	glEnd();
}

void DesenhaQuadrados() {
	int x=200, y=200;
	glColor3f(1, 1, 1);
	do {
		glBegin(GL_LINE_LOOP);
		glVertex3f(-x, y, 0);
		glVertex3f(x, y, 0);
		glVertex3f(x, -y, 0);
		glVertex3f(-x, -y, 0);
		glEnd();
		x -= 5;
		y -= 5;
	} while (x >= 0);
}

void DesenhaJamaica() {
	int x=5, y=5;
	glColor3f(0, 1, 0);
	do {
		glBegin(GL_LINE_LOOP);
		glVertex3f(x, y, 0);
		glVertex3f(-x, y, 0);
		glVertex3f(x, -y, 0);
		glVertex3f(-x, -y, 0);
		glEnd();
		x += 5;
		y += 5;
	} while (x <= 200);

	x = y = 5;
	glColor3f(0, 0, 0);
	do {
		glBegin(GL_LINE_LOOP);
		glVertex3f(x, y, 0);
		glVertex3f(x, -y, 0);
		glVertex3f(-x, y, 0);
		glVertex3f(-x, -y, 0);
		glEnd();
		x += 5;
		y += 5;
	} while (x <= 200);
}

void DesenhaX() {
	int x=5, y=5;
	glColor3f(1, 1, 1);
	do {
		glBegin(GL_POINTS);
		glVertex3f(x, y, 0);
		glVertex3f(-x, y, 0);
		glVertex3f(x, -y, 0);
		glVertex3f(-x, -y, 0);
		glEnd();
		x += 5;
		y += 5;
	} while (x <= 200);
}


int main(int argc, char** argv){
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(400, 400);
	glutInitWindowPosition(400, 200);
	glutCreateWindow("Aula #2 do Freire BB ;)");;
	glutDisplayFunc(DISPLAY);
	glutMainLoop();
	return 0;
}