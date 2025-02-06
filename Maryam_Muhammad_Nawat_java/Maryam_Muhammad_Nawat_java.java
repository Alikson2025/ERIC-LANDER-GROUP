// Method to display the information
public static void displayDetails(String name, String email, String phone, String interest) {
    System.out.println("Name: " + name);
    System.out.println("Email: " + email);
    System.out.println("Phone Number: " + phone);
    System.out.println("Area of Interest: " + interest);
}

public static void main(String[] args) {
    // Initializing variables
    String name = "Maryam Muhammad Nawat";
    String email = "maryammuhammadnawat@gmail.com";
    String phone = "07043656995";
    String interest = "Bioinformatics Tools Development";

    // Calling the method to display the details
    displayDetails(name, email, phone, interest);
}
}
