public class Node {
	public User data;
	public Node next;
	int dfsnum;
	int backnum;
	// constructor name does not get the <T>
	public Node(User data, Node next) {
		this.data = data;
		this.next = next;
		
	}

	
	public boolean equals(Node n){
		return n.data.equals(this.data);
	}
}