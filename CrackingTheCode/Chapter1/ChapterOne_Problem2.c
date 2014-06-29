#include <stdlib.h>
#include <stdio.h>
#include <string.h>

/**Write code to reverse a C-Style string. (C-stringmeans that “abcd” is represented as  five characters, including the null character.***/


/*Brute force solution. This function Allocates space for the same string twice, then copies the reverse contents of one copy to another.
 * Loop from end of the string starting with the null byte. Whenthe \0 is encountered,
 * it gets ignored. While the index of the result is less then the length of the copy, set the result character
 * to be the character starting from the end of the string. The inner loop breaks upon succesful insertion so that 
 * each value does not end up the same (eventually, the same character wil get copied to every index of the result in that case.
 *  
 */
char *reverseString(char *test){

    int i,j=0;
    char *str = (char *)malloc(strlen(test));
    char *result = (char *)malloc(strlen(test));
    strcpy(str,test);
    strcpy(result,test);

    for(i=strlen(str); i>=0; i--){
        if(str[i] !='\0'){
            while(j<strlen(str)){
                result[j] = str[i];
                j++;
                break;
            }
        }
    }
    return result;
}

int main(int argc, char **argv){

    char buffer[1024];
    printf("Please enter the string you want to reverse: ");
    fgets(buffer, 1024, stdin); 
    printf("The reversed result is: %s\n",reverseString(buffer));

    return 0;
}

