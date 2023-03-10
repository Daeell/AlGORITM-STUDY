function solution(skill, skill_trees) {
    var answer = 0;
    skill = [...skill];
    
    while(skill_trees.length>0){
        let cur_skill_tree = skill_trees.shift();
        
        var arr = Array(skill.length).fill(0);
        var skill_order =0;
        let skill_cnt =0
        
        for(let i =0; i<cur_skill_tree.length;i++){
            if(skill.includes(cur_skill_tree[i])){
                skill_cnt++;
                if(arr[skill_order]===0 && skill[skill_order] === cur_skill_tree[i]){
                    arr[skill_order]=1
                    skill_order++;
                } else{
                    break;
                }
            }
        }

        
        if(arr.reduce((acc, cur) => acc+cur) === skill_cnt) {
            answer++;
        }
    }
    

    return answer;
}

console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))