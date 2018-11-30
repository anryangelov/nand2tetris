// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

    @0
    D=!A
    @R1 // all bits are ones
    M=D
    @25026
    D=A
    @R2 // max memory address of the screen
    M=D
    @SCREEN
    D=A
    @R3 // minimum address of the screen
    M=D
    @R0 // current memory address
    M=D
(LOOP)
    @KBD
    D=M
    @BLACKENS
    D;JNE
    @WITHENS
    0;JMP
(BLACKENS)
    @R0
    D=M
    @R2
    D=D-M
    @LOOP
    D;JGT

    @R1
    D=M
    @R0
    A=M
    M=D

    @R0
    M=M+1

    @BLACKENS
    0;JMP
(WITHENS)
    @R0  // current memory address
    D=M
    @R3  // minimum memory address
    D=D-M
    @LOOP
    D;JLE

    @R0
    M=M-1

    @R0
    A=M
    M=0

    @WITHENS
    0;JMP
