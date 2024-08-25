/*
    Eatclusive LLC
    Edited by: Simon Yang
    Edited date: 08/06/24
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

int number=0;

class Constructor {
private:
    std::string customerName;
    bool orderStatus;

public:
    // Constructor that takes a std::string and a bool
    Constructor(const std::string& str, bool b) : customerName(str), orderStatus(b) {
        // Initialization list initializes members
        std::cout << "Constructor called with string: " << customerName
            << " and bool: " << std::boolalpha << orderStatus << std::endl;
    }

    // Member function to display values
    void display() const {
        std::cout << "String: " << customerName << ", Bool: " << std::boolalpha << orderStatus << std::endl;
    }
};

std::string Appender() {
    std::string User = "ec";
    std::string uID = User + std::to_string(number);
    return uID;

}

int fileOpener()
{
    std::ifstream inputFile("Information.txt");

    if (!inputFile.is_open())
    {
    std::cerr << "Failed to open the file." << std::endl;
    return 1;
    }
    std::string line;
    while (std::getline(inputFile, line))
    {
        std::cout << line << std::endl;
    }
    inputFile.close();
    return 0;
}

int fileWriter()
{
    std::ifstream inputFile("Information.txt");
    if (!inputFile.is_open()) {
        std::cerr << "Failed to open the file for reading." << std::endl;
        return 1;
    }

    // Read the file into a vector of strings
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(inputFile, line)) {
        lines.push_back(line);
    }

    // Close the input file
    inputFile.close();

    // Modify specific lines
    if (!lines.empty()) {
        lines[0] = "Modified first line."; // Example modification
    }

    // Open the file for writing
    std::ofstream outputFile("Information.txt");
    if (!outputFile.is_open()) {
        std::cerr << "Failed to open the file for writing." << std::endl;
        return 1;
    }

    // Write the modified content back to the file
    for (const auto& modifiedLine : lines) {
        outputFile << modifiedLine << std::endl;
    }

    // Close the output file
    outputFile.close();

    return 0;
}

int main() {
    // Create an object of Constructor using the constructor
    Constructor obj("Hello, World!", true);
    // Display the values of the object
    obj.display();
    fileOpener();
    fileWriter();
    return 0;
}
