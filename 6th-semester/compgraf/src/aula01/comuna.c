#include <stdlib.h>
#include <stdio.h>
#include <GL/freeglut.h>
#include <math.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // Fundo vermelho (tradicional)
    glColor3f(0.8f, 0.0f, 0.0f);
    glBegin(GL_QUADS);
        glVertex2f(-200, -200);
        glVertex2f(200, -200);
        glVertex2f(200, 200);
        glVertex2f(-200, 200);
    glEnd();
    
    // Martelo (parte superior)
    glColor3f(1.0f, 1.0f, 1.0f);  // Branco
    glLineWidth(5.0f);
    
    // Cabo do martelo
    glBegin(GL_LINES);
        glVertex2f(-50, 30);
        glVertex2f(50, 30);
    glEnd();
    
    // Cabeça do martelo
    glBegin(GL_QUADS);
        glVertex2f(50, 50);
        glVertex2f(80, 50);
        glVertex2f(80, 10);
        glVertex2f(50, 10);
    glEnd();
    
    // Foice (parte curva)
    // Desenhamos a foice usando um arco
    glBegin(GL_LINE_STRIP);
        for(float angle = -45.0f; angle <= 135.0f; angle += 5.0f) {
            float rad = angle * 3.14159f / 180.0f;
            float x = 100.0f * cos(rad);
            float y = 100.0f * sin(rad);
            glVertex2f(x - 30, y - 30);
        }
    glEnd();
    
    // Parte reta da foice
    glBegin(GL_LINES);
        glVertex2f(-30, -30);
        glVertex2f(40, -120);
    glEnd();
    
    // Estrela (opcional)
    glColor3f(1.0f, 1.0f, 1.0f);
    glBegin(GL_POLYGON);
        glVertex2f(0, 120);  // Ponto superior
        glVertex2f(-30, 80); // Ponto inferior esquerdo
        glVertex2f(-15, 80); 
        glVertex2f(0, 50);   // Ponto central inferior
        glVertex2f(15, 80);
        glVertex2f(30, 80);  // Ponto inferior direito
    glEnd();
    
    glutSwapBuffers();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 800);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Simbolo Comunista");
    
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(-200, 200, -200, 200);
    glMatrixMode(GL_MODELVIEW);
    
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
