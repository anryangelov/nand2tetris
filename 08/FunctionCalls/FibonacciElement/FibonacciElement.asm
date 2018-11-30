
@256
D=A
@SP
M=D

// save return address

    @return_Sys.init0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// save LCL

    @LCL  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save ARG

    @ARG  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THIS

    @THIS  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THAT

    @THAT  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
    // reposition ARG
    @SP
    D=M
    @5
    D=D-A
    @ARG
    M=D
    // reposition LCL
    @SP
    D=M
    @LCL
    M=D
    
    @Sys.init
    0;JMP

(return_Sys.init0)
// function Main.fibonacci 0
(Main.fibonacci)

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
    
// push constant 2
    @2
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

    
    @TRUE0
    D;JLT
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
    
// if-goto IF_TRUE
    @SP
    AM=M-1
    D=M
    @IF_TRUE
    D;JNE

// goto IF_FALSE
    @IF_FALSE
    0;JMP

// label IF_TRUE          
(IF_TRUE)

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
    
// label IF_FALSE         
(IF_FALSE)

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
    
// push constant 2
    @2
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
    
// call Main.fibonacci 1  
// save return address

    @return_Main.fibonacci1
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// save LCL

    @LCL  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save ARG

    @ARG  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THIS

    @THIS  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THAT

    @THAT  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
    // reposition ARG
    @SP
    D=M
    @6
    D=D-A
    @ARG
    M=D
    // reposition LCL
    @SP
    D=M
    @LCL
    M=D
    
    @Main.fibonacci
    0;JMP

(return_Main.fibonacci1)

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
    
// push constant 1
    @1
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
    
// call Main.fibonacci 1  
// save return address

    @return_Main.fibonacci2
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// save LCL

    @LCL  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save ARG

    @ARG  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THIS

    @THIS  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THAT

    @THAT  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
    // reposition ARG
    @SP
    D=M
    @6
    D=D-A
    @ARG
    M=D
    // reposition LCL
    @SP
    D=M
    @LCL
    M=D
    
    @Main.fibonacci
    0;JMP

(return_Main.fibonacci2)

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
    // function Sys.init 0
(Sys.init)

// push constant 4
    @4
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// call Main.fibonacci 1   
// save return address

    @return_Main.fibonacci3
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// save LCL

    @LCL  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save ARG

    @ARG  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THIS

    @THIS  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THAT

    @THAT  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
    // reposition ARG
    @SP
    D=M
    @6
    D=D-A
    @ARG
    M=D
    // reposition LCL
    @SP
    D=M
    @LCL
    M=D
    
    @Main.fibonacci
    0;JMP

(return_Main.fibonacci3)

// label WHILE
(WHILE)

// goto WHILE              
    @WHILE
    0;JMP
