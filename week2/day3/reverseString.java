import java.util.Arrays;

import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {
    public static void reverse(char[] arrayOfChars) {
        int front = 0, back = arrayOfChars.length - 1;
        while (front < back) {
            char temporary;
                 
            temporary = arrayOfChars[front];
            arrayOfChars[front] = arrayOfChars[back];
            arrayOfChars[back] = temporary;
            
            front++;
            back--;
        }

    }
    public static void printArray(char[] ar) {
        for(int i = 0; i < ar.length; i++)
            System.out.print(ar[i] + " ");
        System.out.println("");
        
    }


















    // tests

    @Test
    public void emptyStringTest() {
        final char[] expected = "".toCharArray();
        final char[] actual = "".toCharArray();
        reverse(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void singleCharacterStringTest() {
        final char[] expected = "A".toCharArray();
        final char[] actual = "A".toCharArray();
        reverse(actual);
        assertArrayEquals(expected, actual);
    }

    @Test
    public void longerStringTest() {
        final char[] expected = "EDCBA".toCharArray();
        final char[] actual = "ABCDE".toCharArray();
        reverse(actual);
        assertArrayEquals(expected, actual);
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}