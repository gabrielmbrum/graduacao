#include <GL/glut.h>

void renderText() {
    glColor3f(1.0, 1.0, 1.0); // Cor branca
    glRasterPos2f(-0.5, 0.0);  // Posição do texto
    
    char* str = "Hello World!";
    for (char* c = str; *c != '\0'; c++) {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, *c);
    }
}

int main () {
	renderText();
