#include <xc.inc>           ; Inclui o arquivo de cabe?alho xc.inc

; Configura??es dos fus?veis do microcontrolador
CONFIG FOSC=XT              ; Oscilador de cristal
CONFIG WDTE=OFF             ; Watchdog Timer desativado
CONFIG PWRTE=ON             ; Power-up Timer ativado
CONFIG BOREN=ON             ; Brown-out Reset ativado
CONFIG LVP=OFF              ; Low-Voltage Programming desativado
CONFIG CPD=OFF              ; C?digo de prote??o de dados desativado
CONFIG WRT=OFF              ; Prote??o de grava??o desativada
CONFIG CP=OFF               ; Prote??o de c?digo desativada

#define _XTAL_FREQ 4000000  ; Define a frequ?ncia do cristal em 4 MHz

; Defini??es simb?licas para os pinos do microcontrolador
#define VERMELHO PORTB,2
#define AMARELO  PORTB,1
#define VERDE    PORTB,0
    
#define CHAVE    PORTD,0
#define CHAVE_EMER PORTD,1

; Defini??o de endere?os para vari?veis de tempo
TEMPO1 EQU 0X20
TEMPO2 EQU 0X21
TEMPO3 EQU 0X22

; Defini??o de uma se??o de c?digo
PSECT code

; Inicializa??o dos pinos de entrada e sa?da
;SAIDAS
 BANKSEL TRISB              ; Seleciona o banco que cont?m TRISB
MOVLW   00000000B          ; Configura todos os pinos do PORTB como sa?das
MOVWF   TRISB
;ENTRADAS
BANKSEL TRISD              ; Seleciona o banco que cont?m TRISD
MOVLW   11111111B          ; Configura todos os pinos do PORTD como entradas
MOVWF   TRISD

BANKSEL PORTB              ; Seleciona o banco que cont?m PORTB
CLRF PORTB                 ; Limpa todos os pinos do PORTB

; Rotina principal
MAIN:
    BTFSC CHAVE            ; Verifica o estado da chave, se for zero, pula a proxima instru??o; (pull-up resistor)
    GOTO DESLIGADA         ; Se a chave estiver desligada, vai para a rotina DESLIGADA

    BTFSS CHAVE_EMER
    GOTO EMERGENCIA
    
    ; Liga e desliga os LEDs com atrasos configur?veis
    BSF VERMELHO           ; Liga o LED vermelho //BSF - bit set
    MOVLW 20               ; Define o valor 12 para o atraso
    CALL ATRASO            ; Chama a rotina de atraso
    BCF VERMELHO           ; Desliga o LED vermelho // BCF - bit clear
    

    MOVLW 10
    CALL ATRASO
    BCF VERMELHO
    
    BSF VERDE              ; Liga o LED verde
    MOVLW 20                ; Define o valor 8 para o atraso
    CALL ATRASO            ; Chama a rotina de atraso
    BCF VERDE              ; Desliga o LED verde
    
    BSF AMARELO            ; Liga o LED amarelo
    MOVLW 10                ; Define o valor 4 para o atraso
    CALL ATRASO            ; Chama a rotina de atraso
    BCF AMARELO            ; Desliga o LED amarelo
    

    GOTO MAIN              ; Volta para o in?cio da rotina principal

; Rotina para modo emergência
EMERGENCIA:
    
    BSF AMARELO            ; Liga o LED amarelo
    MOVLW 10                ; Define o valor 4 para o atraso
    CALL ATRASO            ; Chama a rotina de atraso
    BCF AMARELO            ; Desliga o LED amarelo
    
    MOVLW 5
    CALL ATRASO 
    
    BTFSC CHAVE_EMER
    GOTO MAIN
    
; Rotina quando a chave est? desligada
DESLIGADA:
    BANKSEL PORTB          ; Seleciona o banco que cont?m PORTB
    CLRF PORTB             ; Limpa todos os pinos do PORTB
    GOTO MAIN              ; Volta para o in?cio da rotina principal

; Rotina de atraso
ATRASO:
    MOVWF TEMPO3           ; Carrega o valor em WREG para TEMPO3, que vai ser 12, 4 ou 8
			   ; neste ponto os valores 12, 4 ou 8 j? foram guardados em TEMPO3;
			   ;Ent?o agora na linha debaixo j? posso guardar o valor 250 nele;
DL0:
    MOVLW 250              ; Carrega 250 em WREG
    MOVWF TEMPO2           ; Carrega WREG para TEMPO2
DL1:	
    MOVLW 200              ; Carrega 200 em WREG
    MOVWF TEMPO1           ; Carrega WREG para TEMPO1
DL2:
    NOP                    ; Instru??o de n?o opera??o (delay); Gasta 1us
    NOP                    ; Instru??o de n?o opera??o (delay)  Gasta 1us
    DECFSZ TEMPO1,F        ; Decrementa TEMPO1 e salta se zero, o F indica que quero manipular a propria vari?vel (TEMPO1). Gasta 1us
			   ; Conta 200 vezes;
    GOTO DL2               ; Vai para DL2 se TEMPO1 n?o for zero; Gasta 2us
			   ; total de gasto de tempo = 5us
    DECFSZ TEMPO2,F        ; Decrementa TEMPO2 e salta se zero
			   ; Conta 250 vezes;
    GOTO DL1               ; Vai para DL1 se TEMPO2 n?o for zero
    DECFSZ TEMPO3,F        ; Decrementa TEMPO3 e salta se zero
			   ; Ent?o 200x250 = 50.000 x 5us = 250.000.00 x 16 vermelho = 4 segundos (vermelho)
			   ; Ent?o 200x250 = 50.000 x 5us = 250.000.00 x 16 vermelho = 1 segundos (amarelo)
			   ; Ent?o 200x250 = 50.000 x 5us = 250.000.00 x 16 vermelho = 2 segundos (verde)
    GOTO DL0               ; Vai para DL0 se TEMPO3 n?o for zero
    RETURN                 ; Retorna ? rotina de chamada

END                        ; Indica o final do c?digo