#include <GL/freeglut.h>
#include <stdio.h>
#include <math.h>

void estrela() {
    
    glBegin(GL_LINE_LOOP);
    glColor3ub(255, 255, 255);
    
    glVertex2i(-12, -22); // ponta esquerda embaixo
    glVertex2i(-7, -10); // em cima ponta esquerda embaixo
    glVertex2i(-18, 0); // ponta esquerda meio

    glVertex2i(-5, 0); // meio esquerda meio
    glVertex2i(0, 15);  // ponta em cima
    glVertex2i(5, 0); // meio direita meio

    glVertex2i(18, 0); //ponta direita meio
    glVertex2i(7, -10); // em cima ponta direita embaixo
    glVertex2i(12, -22); // ponta direita embaixo

    glVertex2i(0, -15); //cu

    glEnd();

}

void desenha_estrelas() {
    glPushMatrix();
    glScalef(0.1, 0.1, 1);
    estrela();
    glPopMatrix();

    glPushMatrix();
    glScalef(0.1, 0.1, 1);
    glTranslatef(-200, -200, 0);
    estrela();
    glPopMatrix();

    glPushMatrix();
    glScalef(0.1, 0.1, 1);
    glTranslatef(-400, -200, 0);
    estrela();
    glPopMatrix();

    glPushMatrix();
    glScalef(0.1, 0.1, 1);
    glTranslatef(-300, -0, 0);
    estrela();
    glPopMatrix();

    glPushMatrix();
    glScalef(0.1, 0.1, 1);
    glTranslatef(200, -400, 0);
    estrela();
    glPopMatrix();

    glPushMatrix();
    glScalef(0.1, 0.1, 1);
    glTranslatef(300, -50, 0);
    estrela();
    glPopMatrix();

    glPushMatrix();
    glScalef(0.1, 0.1, 1);
    glTranslatef(-20, -150, 0);
    estrela();
    glPopMatrix();

    glPushMatrix();
    glScalef(0.1, 0.1, 1);
    glTranslatef(200, 100, 0);
    estrela();
    glPopMatrix();

    glPushMatrix();
    glScalef(0.1, 0.1, 1);
    glTranslatef(-180, 490, 0);
    estrela();
    glPopMatrix();
}

void circulo() {
    float raio = 75;
    glBegin(GL_POLYGON);
    glColor3ub(40,22, 111);
    float theta = 0.0f;
    while (theta < 2.0f * 3.1415926f) {
        float x = raio * cosf(theta);
        float y = raio * sinf(theta);
        glVertex2f(x, y);
        theta += 0.1f; // Incremento do ângulo
    }
    glEnd();
}

void faixa() {

    glBegin(GL_LINE_STRIP);

    glColor3ub(255, 255, 255);
    float raio = 75;
    float theta = 0.0f;
    while (theta < 2.0f * 3.1415926f) {
        float x = raio * cosf(theta);
        float y = raio * sinf(theta);
        if (abs(x) <= abs(70.99f) && abs(y) <= abs(150.0f) && y >= 0)
            glVertex2f(x, y);
        theta += 0.1f; // Incremento do ângulo
    }

    glEnd();

}

void DISPLAY(){
	glClearColor(0, 0.59, 0.22, 0);
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-200, 200, -200, 200);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    // losango
    glBegin(GL_POLYGON);
        glColor3ub(255, 215, 0);
        glVertex2i(-150, 0);
        glVertex2i(0, 150);
        glVertex2i(150, 0);
        glVertex2i(0, -150);
    glEnd();

    circulo();

    desenha_estrelas();

    for (float i = 0; i < 10; i += 0.5) {
        glPushMatrix();
        glScalef(1.05, 0.99, 1);
        glTranslatef(0, -45+i, 0);
        faixa();
        glPopMatrix();
    }


	glutSwapBuffers();
}

int main (int argc, char** argv) {
    glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(1000, 700);
	glutInitWindowPosition(400, 200);
	glutCreateWindow("Aula #4 do Freire BB ;)");;
	glutDisplayFunc(DISPLAY);
	glutMainLoop();
	return 0;

}
