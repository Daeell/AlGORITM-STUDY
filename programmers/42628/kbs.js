const solution = (operations) => {
    let answer = [];
    for (let i = 0; i < operations.length; i++) {
      const num = Number(operations[i].substring(2));
      switch (operations[i].substring(0, 1)) {
        case "I":
          answer.push(num);
          answer.sort((a, b) => {
            return a - b;
          });
          break;
        case "D":
          if (num === 1) {
            answer.pop();
          } else {
            answer.shift();
          }
          break;
      }
    }
        return answer.length ? [answer[answer.length - 1], answer[0]] : [0, 0];
    }