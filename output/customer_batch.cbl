       IDENTIFICATION DIVISION.
       PROGRAM-ID. CUSTOMERBATCH.

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.

       FILE-CONTROL.
           SELECT INPUT-FILE ASSIGN TO "input.dat".
           SELECT VIP-FILE ASSIGN TO "vip.dat".
           SELECT NORMAL-FILE ASSIGN TO "normal.dat".

       DATA DIVISION.

       FILE SECTION.

       FD INPUT-FILE.
       01 INPUT-REC.
           05 CUST-ID      PIC 9(5).
           05 NAME         PIC X(20).
           05 BALANCE      PIC 9(7)V99.

       FD VIP-FILE.
       01 VIP-REC          PIC X(40).

       FD NORMAL-FILE.
       01 NORMAL-REC       PIC X(40).

       WORKING-STORAGE SECTION.

       01 EOF-FLAG PIC X VALUE 'N'.
       01 COUNT-VIP PIC 9(5) VALUE 0.
       01 COUNT-NORMAL PIC 9(5) VALUE 0.

       PROCEDURE DIVISION.

       MAIN-PARA.

           OPEN INPUT INPUT-FILE
           OPEN OUTPUT VIP-FILE
           OPEN OUTPUT NORMAL-FILE

           PERFORM UNTIL EOF-FLAG = 'Y'

               READ INPUT-FILE
                   AT END
                       MOVE 'Y' TO EOF-FLAG
                   NOT AT END
                       PERFORM PROCESS-REC
               END-READ

           END-PERFORM

           DISPLAY "VIP COUNT: " COUNT-VIP
           DISPLAY "NORMAL COUNT: " COUNT-NORMAL

           CLOSE INPUT-FILE
           CLOSE VIP-FILE
           CLOSE NORMAL-FILE

           STOP RUN.

       PROCESS-REC.

           IF BALANCE > 10000
               MOVE INPUT-REC TO VIP-REC
               WRITE VIP-REC
               ADD 1 TO COUNT-VIP
           ELSE
               MOVE INPUT-REC TO NORMAL-REC
               WRITE NORMAL-REC
               ADD 1 TO COUNT-NORMAL
           END-IF.
