function solution(numbers, target) {
    var answer = 0;

    function find_answer(sum_, cnt) {
        
        if (cnt === numbers.length){
            if(sum_ === target){
                answer++;
            }
            return;
        }
        cnt++;
        
        find_answer(sum_+numbers[cnt-1], cnt);
        find_answer(sum_-numbers[cnt-1], cnt);
        
        return;
    }

    find_answer(numbers[0], 1)
    find_answer(-numbers[0], 1)

    return answer;
}


console.log(solution([1, 1, 1, 1, 1], 3))