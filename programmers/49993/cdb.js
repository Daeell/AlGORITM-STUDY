const skill = "CBD";
["C", "B", "D"];
const skill_trees = ["BACDE", "CBADF", "AECB", "BDA"];

function solution(skill, skill_trees) {
  let answer = 0;
  for (let item of skill_trees) {
    let flag = true;
    let skills = skill.split("");
    for (let str of item.split("")) {
      if (skills.includes(str)) {
        if (skills[0] === str) {
          skills.shift();
        } else {
          flag = false;
          break;
        }
      }
    }
    if (flag === true) {
      answer += 1;
    }
  }
  return answer;
}

console.log(solution(skill, skill_trees));

// shift(): 첫 번째 요소를 제거하고, 제거된 요소를 반환
