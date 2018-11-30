
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
// function Class2.set 0
(Class2.set)

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
    
// pop static 0
    @SP
    A=M-1
    D=M
    @Class2.vm.0
    M=D
    @SP
    M=M-1
    
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
    
// pop static 1
    @SP
    A=M-1
    D=M
    @Class2.vm.1
    M=D
    @SP
    M=M-1
    
// push constant 0
    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
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
    
// function Class2.get 0
(Class2.get)

// push static 0
    @Class2.vm.0
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    
// push static 1
    @Class2.vm.1
    D=M
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

// push constant 6
    @6
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 8
    @8
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// call Class1.set 2
// save return address

    @return_Class1.set1
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
    @7
    D=D-A
    @ARG
    M=D
    // reposition LCL
    @SP
    D=M
    @LCL
    M=D
    
    @Class1.set
    0;JMP

(return_Class1.set1)

// pop temp 0 
    @SP
    A=M-1
    D=M
    
    @5
    M=D
    
    @SP
    M=M-1
    
// push constant 23
    @23
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 15
    @15
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// call Class2.set 2
// save return address

    @return_Class2.set2
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
    @7
    D=D-A
    @ARG
    M=D
    // reposition LCL
    @SP
    D=M
    @LCL
    M=D
    
    @Class2.set
    0;JMP

(return_Class2.set2)

// pop temp 0 
    @SP
    A=M-1
    D=M
    
    @5
    M=D
    
    @SP
    M=M-1
    
// call Class1.get 0
// save return address

    @return_Class1.get3
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
    
    @Class1.get
    0;JMP

(return_Class1.get3)

// call Class2.get 0
// save return address

    @return_Class2.get4
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
    
    @Class2.get
    0;JMP

(return_Class2.get4)

// label WHILE
(WHILE)

// goto WHILE
    @WHILE
    0;JMP
// function Class1.set 0
(Class1.set)

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
    
// pop static 0
    @SP
    A=M-1
    D=M
    @Class1.vm.0
    M=D
    @SP
    M=M-1
    
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
    
// pop static 1
    @SP
    A=M-1
    D=M
    @Class1.vm.1
    M=D
    @SP
    M=M-1
    
// push constant 0
    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
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
    
// function Class1.get 0
(Class1.get)

// push static 0
    @Class1.vm.0
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    
// push static 1
    @Class1.vm.1
    D=M
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
    