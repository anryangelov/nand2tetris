
@256
D=A
@SP
M=D
// push constant 17
    @17
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 17
    @17
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// eq
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE0
    D;JEQ
    D=0
    @FALSE0
    0;JMP
(TRUE0)
    D=-1
(FALSE0)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 17
    @17
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 16
    @16
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// eq
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE1
    D;JEQ
    D=0
    @FALSE1
    0;JMP
(TRUE1)
    D=-1
(FALSE1)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 16
    @16
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 17
    @17
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// eq
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE2
    D;JEQ
    D=0
    @FALSE2
    0;JMP
(TRUE2)
    D=-1
(FALSE2)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 892
    @892
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 891
    @891
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// lt
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE3
    D;JLT
    D=0
    @FALSE3
    0;JMP
(TRUE3)
    D=-1
(FALSE3)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 891
    @891
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 892
    @892
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// lt
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE4
    D;JLT
    D=0
    @FALSE4
    0;JMP
(TRUE4)
    D=-1
(FALSE4)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 891
    @891
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 891
    @891
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// lt
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE5
    D;JLT
    D=0
    @FALSE5
    0;JMP
(TRUE5)
    D=-1
(FALSE5)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 32767
    @32767
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 32766
    @32766
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// gt
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE6
    D;JGT
    D=0
    @FALSE6
    0;JMP
(TRUE6)
    D=-1
(FALSE6)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 32766
    @32766
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 32767
    @32767
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// gt
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE7
    D;JGT
    D=0
    @FALSE7
    0;JMP
(TRUE7)
    D=-1
(FALSE7)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 32766
    @32766
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 32766
    @32766
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// gt
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE8
    D;JGT
    D=0
    @FALSE8
    0;JMP
(TRUE8)
    D=-1
(FALSE8)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 57
    @57
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 31
    @31
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 53
    @53
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// add
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M+D

    

    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 112
    @112
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// sub
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    

    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// neg
    @SP
    A=M-1  // address of the operand
    D=-M  // the value
    M=D

// and
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M&D

    

    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push constant 82
    @82
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// or
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M|D

    

    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// not
    @SP
    A=M-1  // address of the operand
    D=!M  // the value
    M=D

(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
