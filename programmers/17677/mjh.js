// PASSED

function solution(str1, str2) {
  const dict1 = {};
  const dict2 = {};
  
  const alphabetRE = /[a-zA-Z]/;
  
  for (let i = 1; i < str1.length; i++) {
      if (!(alphabetRE.test(str1[i-1]) && alphabetRE.test(str1[i]))) {
          continue
      }
      const str = (str1[i-1] + str1[i]).toLowerCase()
      if (!dict1[str]) {
          dict1[str] = 0;
      }
      dict1[str]++;
  }
  
  for (let i = 1; i < str2.length; i++) {
      if (!(alphabetRE.test(str2[i-1]) && alphabetRE.test(str2[i]))) {
          continue
      }
      const str = (str2[i-1] + str2[i]).toLowerCase()
      if (!dict2[str]) {
          dict2[str] = 0;
      }
      dict2[str]++;
  }
  
  let interLen = 0;
  let unionLen = 0;
  
  for (let e in dict1) {
      if (dict2[e]) {
          interLen += dict1[e] - dict2[e] > 0 ? dict2[e] : dict1[e];
      } else {
          unionLen += dict1[e];
      }
  }
  
  for (let e in dict2) {
      if (dict1[e]) {
          unionLen += dict1[e] - dict2[e] > 0 ? dict1[e] : dict2[e];
      } else {
          unionLen += dict2[e];
      }
  }
  
  return interLen || unionLen ? Math.floor((interLen / unionLen) * 65536) : 65536;
}