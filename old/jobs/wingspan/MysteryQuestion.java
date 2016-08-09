package com.wingspan.interview;

/**
 * Add comments to the method below without changing any of the code so as to
 * indicate what is happening in a meaningful sense. Write a summary comment
 * above the method itself that explains what the method does and provides any
 * other useful notes regarding its use or behavior that you feel are relevant.
 */
public class MysteryQuestion {

    /*This method takes in a string whose length should be 9 characters. It then loops through the string an
     * appends certain characters depending on its index. If the index is 0, 3, or 6, it adds '(','-', or ').
     * Otherwise, it checks the string for either a digit or a character. If it's a digit, it simply adds that index of
     * the string to the dynamically allocated buffer.
     * If it's a character, some manipulation is done to the character by subtracting 'a' (97 in decimal
     * from the character and then casting this integer as a cha and  storing this in a temporary variable.
     * Afterward, a second character is initialized and some integer is calculated by taking the integer
     * cast of 2 which is 50 and then taking 1/3 of whatever c1 is and adding it to 50, and then  casting
     * it as a char and storing it as the variable c2. This is then appended to the result string which gets
     * returned at the end.
     */

	public static String function(String s) {   //function that takes in a string
		if (s == null || s.length() != 9) {     //if the string is null or it's length is not equal to 9
			throw new RuntimeException();       //exit and throw exception
		}

		StringBuffer sb = new StringBuffer();   //create a dynamically allocated string
		for (int i = 0; i < 9; i++) {           //loop from 0 to 8
			if (i == 0) {                       //if the counter is zero insert a '('
				sb.append('(');
			} else if (i == 3) {                //if the count is 3, insert a ')'
				sb.append(')');
			} else if (i == 6) {                //if the count is 6, insert a '-'
				sb.append('-');
			}

			char c = s.charAt(i);               //get the character at this from the string being passed in and store it
			if (Character.isDigit(c)) {         //if the character at this index is a digit, add it to the buffer
				sb.append(c);
			} else if (Character.isLetter(c)) { //if the character is a letter:
                //subtract the ascii value of 'a' from the lowercase version of this char and store it in var c1
                //cast this intger as a char
				char c1 = (char) (Character.toLowerCase(c) - 'a');

                //take the character 2, cast it as an int, and
                //then add this to whatever character/3,
                //and then store this as a char as var c2
				char c2 = (char) (((int) '2') + (c1 / 3));

				sb.append(c2);                  //add c2 to the string buffer
			} else {                            //if the character is non alphanumeric or a (,-,), exit
				throw new RuntimeException();
			}
		}

		return sb.toString();                   //return the string buffer as a string object.
	}
}
