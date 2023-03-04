// PASSED

/**
 * m 길이를 가진 롤러의 시작점을 section의 원소에 맞추고,
 * 한 번 칠했을 때 같이 칠해질 수 있는 section 원소들은 무시합니다.
 * 최종적으로 칠한 횟수를 반환합니다.
 * 
 * @param {number} n 
 * @param {number} m 
 * @param {Array<number>} section 
 * @returns {number} answer
 */
function solution2(n, m, section) {
  let answer = 0;
  
  let paintable = 0;
  for (let i = 0; i < section.length; i++)
  {
      const wallNum = section[i];
      if (paintable >= wallNum)
      {
          continue;
      }
      answer++;
      paintable = wallNum + m - 1;
  }
  
  return answer;
}