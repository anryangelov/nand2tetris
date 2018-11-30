
// function SimpleFunction.test 2
(SimpleFunction.test)

    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push local 0
    @0
    D=A
    @LCL
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// push local 1
    @1
    D=A
    @LCL
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
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
    
// not
    @SP
    A=M-1  // address of the operand
    D=!M  // the value
    M=D

// push argument 0
    @0
    D=A
    @ARG
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
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
    
// push argument 1
    @1
    D=A
    @ARG
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
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
    
// return
    // R13 (temp var) = LCL
    @LCL
    D=M
    @R13
    M=D
    // R14 (temp var) = retAddr
    @5
    A=D-A
    D=M
    @R14
    M=D
    // reposition return value for caller
    @SP
    A=M-1
    D=M
    @ARG
    A=M
    M=D
    // restore the caller's SP
    @ARG
    D=M+1
    @SP
    M=D
    // restore the caller's THAT
    @R13
    AM=M-1
    D=M
    @THAT
    M=D
    // restore the caller's THIS
    @R13
    AM=M-1
    D=M
    @THIS
    M=D
    // restore the caller's ARG
    @R13
    AM=M-1
    D=M
    @ARG
    M=D
    // restore the caller's LCL
    @R13
    AM=M-1
    D=M
    @LCL
    M=D
    @R14
    A=M
    0;JMP
    
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
