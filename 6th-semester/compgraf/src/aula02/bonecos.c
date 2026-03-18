#include <stdlib.h>
#include <stdio.h>
#include <GL/freeglut.h>
#include <math.h>
#include <stdbool.h>

void DISPLAY();

//glScalef(x, y, z);
//glRotatef(angulo, x, y, z); (coloca 1 no eixo que quer rotacionar)
//glTranslatef(x, y, z);

//glPushMatrix();
// ---- transformações ----
//desenha();
//glPopMatrix();

void DesenhaObjeto();

void DISPLAY(){
	glClearColor(0.5, 0.5, 0.5, 0); //
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-200, 200, -200, 200);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	
	glColor3f(1, 0, 0);
	glPushMatrix();
	DesenhaObjeto();
	glPopMatrix();

	glColor3f(0, 1, 0);
	glPushMatrix();
	glRotatef(30, 0, 0, 1); 
	glTranslatef(50, 25, 0);
	glScalef(0.75, 0.75, 1); 
	DesenhaObjeto();
	glPopMatrix();

	glColor3f(0, 0, 1);
	glPushMatrix();
	glRotatef(45, 0, 0, 1); 
	glTranslatef(75, 10, 0);
	glScalef(0.5, 0.5, 1); 
	DesenhaObjeto();
	glPopMatrix();

	glColor3f(0, 1, 1);
	glPushMatrix();
	glRotatef(60, 0, 0, 1); 
	glTranslatef(100, 5, 0);
	glScalef(0.3, 0.3, 1); 
	DesenhaObjeto();
	glPopMatrix();

	glutSwapBuffers();
}

void DesenhaObjeto() {
	int x, y, raio = 25;

	glBegin(GL_LINE_STRIP);
	for (x = 0; x <= 200; x++) {
		for (y = 0; y <= 200; y++) {
			if (pow(x, 2) + pow(y, 2) == pow(raio, 2)) {
				glVertex3f(x, y, 0);
			}
		}
	}
	glEnd();

	glBegin(GL_LINE_STRIP);
	for (x = 0; x <= 200; x++) {
		for (y = 0; y >= -200; y--) {
			if (pow(x, 2) + pow(y, 2) == pow(raio, 2)) {
				glVertex3f(x, y, 0);
			}
		}
	}
	glEnd();

	glBegin(GL_LINE_STRIP);
	for (x = 0; x >= -200; x--) {
		for (y = 0; y >= -200; y--) {
			if (pow(x, 2) + pow(y, 2) == pow(raio, 2)) {
				glVertex3f(x, y, 0);
			}
		}
	}
	glEnd();


	glBegin(GL_LINE_STRIP);
	for (x = 0; x >= -200; x--) {
		for (y = 0; y <= 200; y++) {
			if (pow(x, 2) + pow(y, 2) == pow(raio, 2)) {
				glVertex3f(x, y, 0);
			}
		}
	}
	glEnd();

	// pescoço
	glBegin(GL_LINE_STRIP);
	glVertex3f(0, -25, 0);
	glVertex3f(0, -50, 0);
	glEnd();

	// braço esquerdo
	glBegin(GL_LINE_STRIP);
	glVertex3f(0, -50, 0);
	glVertex3f(-25, -75, 0);
	glEnd();

	// braço direito
	glBegin(GL_LINE_STRIP);
	glVertex3f(0, -50, 0);
	glVertex3f(25, -75, 0);
	glEnd();	

	// tronco
	glBegin(GL_LINE_STRIP);
	glVertex3f(0, -50, 0);
	glVertex3f(0, -100, 0);
	glEnd();

	// perna esquerda
	glBegin(GL_LINE_STRIP);
	glVertex3f(0, -100, 0);
	glVertex3f(-25, -125, 0);
	glEnd();

	// perna direita
	glBegin(GL_LINE_STRIP);
	glVertex3f(0, -100, 0);
	glVertex3f(25, -125, 0);
	glEnd();
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