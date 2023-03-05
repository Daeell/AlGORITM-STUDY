function solution(numbers) {
    var answer = '';

    var str_num = numbers.map((x)=>{
        return x.toString();
    })
    
    str_num.sort((a,b) =>{
        let temp1 = a.concat(b);
        let temp2 = b.concat(a);
        if(temp2>temp1) return 1;
        else if (temp2<temp1) return -1;
        else return 0;
    })
    
    let count = str_num.filter(x => x==='0').length;
    if (str_num.length === count){
        answer ='0';
    } else{
        answer = str_num.join("")
    }
    

    return answer;
}

console.log(solution([0,0,0,0]))


// 1 2 3 4 5 6 11 실패

// function solution(numbers) {
//     var answer = '';

//     var str_num = numbers.map((x)=>{
//         return x.toString();
//     })
    
//     str_num.sort((a,b) =>{
//         if (b[0] > a[0]){
//             return 1;
//         } else if(b[0] < a[0]){
//             return -1;
//         } else{
//             if(b.length === a.length){
//                 let i=1;
//                 while(true){
//                     if (b[i] > a[i]){
//                         return 1;
//                     } else if(b[i] < a[i]){
//                         return -1;
//                     } else{
//                         return 0;
//                     }
//                 }
//             } else{
//                 if(b.length> a.length){
//                     for(let i=0;i<a.length;i++){
//                         if (b[i] > a[i]){
//                             return 1;
//                         } else if(b[i] < a[i]){
//                             return -1;
//                         }
//                     }
//                     for(let i=a.length; i<b.length;i++){
//                         if(b[i]>a[a.length-1]){
//                             return 1;
//                         } else if(b[i]<a[a.length-1]){
//                             return -1;
//                         }
//                     }
//                 } else{
//                     for(let i=0;i<b.length;i++){
//                         if (b[i] > a[i]){
//                             return 1;
//                         } else if(b[i] < a[i]){
//                             return -1;
//                         }
//                     }
//                     for(let i=b.length; i<a.length;i++){
//                         if(b[b.length-1]>a[i]){
//                             return 1;
//                         } else if(b[b.length-1]<a[i]){
//                             return -1;
//                         }
//                     }
//                 }
                
//             }
//         }
        
//     })
    
//     answer = str_num.join("")

//     return answer;
// }


// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // numbers_len은 배열 numbers의 길이입니다.
// char* solution(int numbers[], size_t numbers_len) {
//     // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
// 	char** number = (char**)malloc(numbers_len);
// 	for (int c = 0; c < numbers_len; c++)
// 	{
// 		number[c] = (char*)malloc(numbers_len);
// 		memset(number[c], 0, numbers_len);
// 	}

	
	
// 	for (int a = 0; a < numbers_len; a++)
// 	{
// 		sprintf(number[a], "%d", numbers[a]);
// 		printf("numbers : %d number : %c \n", numbers[a],number[a][1]);
// 	}

// 	char* temp = (char*)malloc(numbers_len);
// 	char* temp2 = (char*)malloc(numbers_len);
// 	char* temp3 = (char*)malloc(numbers_len);
// 	char* answer = (char*)malloc(numbers_len);
// 	memset(answer, 0, numbers_len);
	
// 	int i, j;
// 	int k = 0;
// 	int l = 0;

// 	for (i = 0; i < numbers_len; i++)
// 	{
// 		for (j = 0; j < numbers_len; j++)
// 		{
			
// 			if (strlen(number[i]) > strlen(number[j]))
// 				l = strlen(number[i]);
// 			else
// 				l = strlen(number[j]);
						
// 			while (number[i][k] == number[j][k])
// 			{
// 				printf("k : %d L : %d, number i : %c, number j : %c \n", k, l, number[i][k], number[j][k]);
// 				if (number[i][k]== NULL)
// 				{
// 					if (number[j][k] > number[i][k - 1])
// 					{
// 						temp = number[j];
// 						number[j] = number[i];
// 						number[i] = temp;

// 						printf("ik NULL %s \n",number[i]);
// 					}
// 				}
// 				else if (number[j][k] == NULL)
// 				{
// 					if (number[i][k] > number[j][k - 1])
// 					{
// 						temp = number[i];
// 						number[i] = number[j];
// 						number[j] = temp;

// 						printf("jk NULL %s \n",number[i]);
// 					}
// 				}
// 				/*else if (number[i][k] == NULL && number[i][k] == NULL)
// 				{
// 					temp = number[i];
// 					number[i] = number[j];
// 					number[j] = temp;

// 					printf("both NULL %s \n",number[i]);
// 				}*/
// 				k++;

// 				if (k> l)
// 					break;
// 			}

			

// 			if (number[i][k] > number[j][k])
// 			{
// 				temp = number[i];
// 				number[i] = number[j];
// 				number[j] = temp;
// 			}

// 			k = 0;
// 		}
// 	}

	
	
// 	for (int a = 0; a < numbers_len; a++)
// 		strcat(answer, number[a]);


// 	printf("\n answer : %s \n", answer);
	
	
// 	return answer;
// }