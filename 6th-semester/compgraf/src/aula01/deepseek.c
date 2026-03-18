#include <stdlib.h>
#include <stdio.h>
#include <GL/freeglut.h>
#include <math.h>

float angle = 0.0f;

void display();
void update(int value);

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // Fundo gradiente
    glBegin(GL_QUADS);
        glColor3f(0.2f, 0.2f, 0.8f);  // Azul escuro
        glVertex2f(-200, -200);
        glVertex2f(200, -200);
        glColor3f(0.8f, 0.2f, 0.2f);  // Vermelho escuro
        glVertex2f(200, 200);
        glVertex2f(-200, 200);
    glEnd();

    // Triângulo giratório
    glPushMatrix();
    glRotatef(angle, 0.0f, 0.0f, 1.0f);
    glBegin(GL_TRIANGLES);
        glColor3f(1.0f, 1.0f, 0.0f);  // Amarelo
        glVertex2f(0.0f, 100.0f);
        glColor3f(0.0f, 1.0f, 0.0f);  // Verde
        glVertex2f(-86.6f, -50.0f);
        glColor3f(1.0f, 0.0f, 1.0f);  // Magenta
        glVertex2f(86.6f, -50.0f);
    glEnd();
    glPopMatrix();

    // Quadrado pulsante
    float pulse = sin(angle * 0.0174533) * 20 + 40;
    glColor3f(0.0f, 1.0f, 1.0f);  // Ciano
    glRectf(-pulse, -pulse, pulse, pulse);

    glutSwapBuffers();
}

void update(int value) {
    angle += 1.0f;
    if(angle > 360) angle -= 360;
    
    glutPostRedisplay();
    glutTimerFunc(16, update, 0);  // ~60 FPS
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(960, 540);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("OpenGL Divertido!");
    
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-200, 200, -200, 200);
    glMatrixMode(GL_MODELVIEW);
    
    glutDisplayFunc(display);
    glutTimerFunc(25, update, 0);  // Inicia a animação
    
    glutMainLoop();
    return 0;
}
