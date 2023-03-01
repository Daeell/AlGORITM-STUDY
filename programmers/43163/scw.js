function solution(begin, target, words) {
    var answer = 0;
    var dq = [];
    dq.push([begin, 0])

    if (!(words.find(v => v===target))){
        return answer;
    }

    while (dq.length>0){
        let [dq_word, cnt] = dq.shift();

        if (dq_word=== target){
            answer = cnt;
            break
        }

        for (let word of words){
            let check_point =0;
            for(let i =0; i<word.length;i++){
                if (dq_word[i] !== word[i]){
                    check_point++;
                }
            }
            if(check_point === 1){
                dq.push([word, cnt+1])
            }
        }
    }

    return answer;
}

console.log(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))