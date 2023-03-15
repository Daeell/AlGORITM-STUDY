// PASSED

function solution(record) {
  const answer = [];
  
  const logger = [];
  const userInfo = {};
  
  record.map((v) => {
      const [command, id, nickname] = v.split(' ');
      if (command === 'Enter') {
          logger.push([command, id]);
          userInfo[id] = nickname;
      }
      else if (command === 'Leave') {
          logger.push([command, id]);
      }
      else {
          userInfo[id] = nickname;
      }
  });
  
  logger.map(([command, id]) => {
      answer.push(userInfo[id] + '님이 ' + (command === 'Enter' ? '들어왔습니다.' : '나갔습니다.'));
  });
  
  return answer;
}