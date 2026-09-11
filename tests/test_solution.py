-- PL/SQL Test Suite
SET SERVEROUTPUT ON SIZE UNLIMITED;

DECLARE
    v_output VARCHAR2(4000);
    v_num1   NUMBER := 15;
    v_num2   NUMBER := 25;
    v_sum    NUMBER;
BEGIN
    -- Test Execution
    v_sum := v_num1 + v_num2;
    
    -- Assert condition
    IF v_sum = 40 THEN
        DBMS_OUTPUT.PUT_LINE('TEST PASSED: Sum calculation is correct (15 + 25 = 40).');
    ELSE
        RAISE_APPLICATION_ERROR(-20001, 'TEST FAILED: Expected 40, but got ' || v_sum);
    END IF;
END;
/
     
