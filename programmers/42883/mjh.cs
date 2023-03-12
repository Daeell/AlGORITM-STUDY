// PASSED

using System;

public class Solution {
    public string solution(string number, int k) {
        char[] answer = new char[number.Length];
        char[] answer2 = new char[number.Length-k];
        int ptr = 0;
        
        for (int i = 0; i < number.Length; i++)
        {
            while (k > 0 && ptr > 0 && answer[ptr-1] < number[i])
            {
                ptr--;
                k--;
            }
            answer[ptr] = number[i];
            ptr++;
        }
        
        for (int i = 0; i < answer2.Length; i++) {
            answer2[i] = answer[i];
        }
        string answer3 = new string(answer2);
        
        return answer3;
    }
}
