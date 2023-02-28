function checkTree(b_str, start, end) {
    const par = Math.floor((start+end)/2);
    const left_c = Math.floor((start+ par -1)/2);
    const right_c = Math.floor((par+1+end)/2);

    if(start == end){
        return true;
    }

    if (b_str[par] === '0' && ((b_str[left_c]==='1') || (b_str[right_c]==='1'))){
        return false;
    }

    if (!checkTree(b_str, start, par-1)) return false;
    if (!checkTree(b_str, par+1, end)) return false;
    return true;
}

function solution(numbers) {
    var answer = [];

    for (let num of numbers){
        let bi = num.toString(2);
        let bi_len = bi.length;

        let m = bi_len.toString(2).length;
        let bi_tree = '0'.repeat(2**m-1-bi_len);
        bi_tree = bi_tree + '' + bi;

        if(checkTree(bi_tree, 0, bi_tree.length -1)){
            answer.push(1);
        } else {
            answer.push(0);
        }
    }
    return answer;
}

console.log(solution([63,111,95]))