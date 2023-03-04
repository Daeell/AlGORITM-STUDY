// PASSED

/**
 * 현재 위치에서 direction으로 진행했을 때 방문 가능한 좌표이면 경로를 방문처리 합니다.
 * 방문처리를 위한 routes객체의 key는 '위치x, 위치y, 위치2x, 위치2y' 형식의 문자열입니다.
 * 숫자가 작은 위치가 앞쪽에 오도록 경로 문자열을 만들기 때문에 중복 경로를 체크할 수 있습니다.
 * 
 * @param {string} dirs 
 * @returns {number} Object.keys(routes).length
 */
function solution(dirs) {
  const routes = {};
  const position = [0, 0];
  const newPosition = [0, 0];
  
  for (let i = 0; i < dirs.length; i++)
  {
      const direction = dirs[i];
      
      switch (direction)
      {
          case 'U':
              if (position[1]+1 > 5) continue;
              
              newPosition[1] = position[1]+1;
              routes[position[0] + ',' + position[1] + ',' + newPosition[0] + ',' + newPosition[1]] = 1;
              position[0] = newPosition[0];
              position[1] = newPosition[1];
              
              break;
              
          case 'D':
              if (position[1]-1 < -5) continue;
              
              newPosition[1] = position[1]-1;
              routes[newPosition[0] + ',' + newPosition[1] + ',' + position[0] + ',' + position[1]] = 1;
              position[0] = newPosition[0];
              position[1] = newPosition[1];
              
              break;
              
          case 'L':
              if (position[0]-1 < -5) continue;
              
              newPosition[0] = position[0]-1;
              routes[newPosition[0] + ',' + newPosition[1] + ',' + position[0] + ',' + position[1]] = 1;
              position[0] = newPosition[0];
              position[1] = newPosition[1];
              
              break;
              
          case 'R':
              if (position[0]+1 > 5) continue;
              
              newPosition[0] = position[0]+1;
              routes[position[0] + ',' + position[1] + ',' + newPosition[0] + ',' + newPosition[1]] = 1;
              position[0] = newPosition[0];
              position[1] = newPosition[1];
              
              break;
      }
  }
  
  return Object.keys(routes).length;
}