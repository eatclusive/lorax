/*
    Eatclusive LLC
    Edited by: Simon Yang
    Edited date: 08/06/24
*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <functional>
#include <algorithm>

class sequentialIDGenerator {
public:
    sequentialIDGenerator() : nextID(0) {}

    int getNextID() {
        if (!freeIDs.empty()) {
            // Reuse the smallest available ID
            int reusedID = freeIDs.top();
            freeIDs.pop();
            return reusedID;
        }
        else {
            // Generate a new ID
            int newID = nextID++;
            return newID;
        }
    }

    void releaseID(int id) {
        // Add the ID back to the pool of available IDs
        freeIDs.push(id);
    }

    void assignOrderToCustomer(int customerID) {
        // Get a new ID for the order
        int orderID = getNextID();
        customerOrders[customerID].push_back(orderID);
        std::cout << "Assigned Order ID " << orderID << " to Customer ID " << customerID << std::endl;
    }

    void completeOrder(int orderID) {
        // Release the ID back to the pool
        releaseID(orderID);
        std::cout << "Completed Order ID " << orderID << std::endl;
    }

    void appendOrderToCustomer(int customerID) {
        int orderID = getNextID();
        customerOrders[customerID].push_back(orderID);
        std::cout << "Appended Order ID " << orderID << " to Customer ID " << customerID << std::endl;
    }

    void printCustomerOrders(int customerID) {
        std::cout << "Orders for Customer ID " << customerID << ": ";
        if (customerOrders.find(customerID) != customerOrders.end()) {
            for (int id : customerOrders[customerID]) {
                std::cout << id << " ";
            }
            std::cout << std::endl;
        }
        else {
            std::cout << "No orders found." << std::endl;
        }
    }

private:
    int nextID;
    std::priority_queue<int, std::vector<int>, std::greater<int>> freeIDs; // Min-heap for available IDs
    std::unordered_map<int, std::vector<int>> customerOrders; // Map customer IDs to their order IDs
};

int main() {
    sequentialIDGenerator idGen;

    // Assign orders to customers
    idGen.assignOrderToCustomer(1);
    idGen.assignOrderToCustomer(1);
    idGen.assignOrderToCustomer(2);

    // Print customer orders
    idGen.printCustomerOrders(1);
    idGen.printCustomerOrders(2);

    // Complete an order and release the ID
    idGen.completeOrder(1);

    // Append a new order to a customer
    idGen.appendOrderToCustomer(1);

    // Print customer orders again
    idGen.printCustomerOrders(1);
    idGen.printCustomerOrders(2);

    return 0;
}
