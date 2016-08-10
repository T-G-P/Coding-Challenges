
public class User {
	/**
     * Name of User
     */
    String name;

    /**
     * Name of User's school.
     */
    String school; //if school is null, they are not a student

    public User(String name, String school){

        this.name = name;
        this.school = school;
        
    }
    
    public boolean equals(User u){
    	return u.name.equals(this.name);
    }

}
