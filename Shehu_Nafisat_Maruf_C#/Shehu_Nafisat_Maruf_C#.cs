using System;

class Program
{
    // Method to display the information
    static void DisplayDetails(string name, string email, string phone, string interest)
    {
        Console.WriteLine("Name: " + name);
        Console.WriteLine("Email: " + email);
        Console.WriteLine("Phone Number: " + phone);
        Console.WriteLine("Area of Interest: " + interest);
    }

    static void Main()
    {
        // Initializing variables
        string name = "Shehu Nafisat Maruf";
        string email = "mhizzpydo@gmail.com";
        string phone = "07033895987";
        string interest = "Machine Learning in Bioinformatics";

        // Calling the method to display the details
        DisplayDetails(name, email, phone, interest);
    }
}
