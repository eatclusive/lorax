//Simon Yang
//Eatclusive LLC
//Edited on 8/24/2024


#include <iostream>
#include <unordered_map>
#include "SequentialIDGenerator.h"

// Simple hash function to hash customer IDs
size_t hashOrder(int orderID) {
    return std::hash<int>()(orderID);
}

int main() {
    SequentialIDGenerator idGen;
    std::unordered_map<int, std::vector<int>> customerOrders;

    // Step 1: Generate IDs and simulate filling in missing values
    int order1 = idGen.generateID();
    int order2 = idGen.generateID();
    int order3 = idGen.generateID();

    std::cout << "Generated Order IDs: " << order1 << ", " << order2 << ", " << order3 << std::endl;

    // Simulate finishing order 2, and removing it
    std::cout << "Order " << order2 << " completed. Removing from system.\n";
    // Simulating "deleting" by just not using this order anymore
    // In a real system, we'd remove it from the set, but we're simulating here.

    // Now generate a new order, which should fill the missing (lowest) ID.
    int newOrder = idGen.generateID();
    std::cout << "Generated new Order ID (fills gap): " << newOrder << std::endl;

    // Step 2: Hash the order values to ensure no collisions
    size_t hashOrder1 = hashOrder(order1);
    size_t hashNewOrder = hashOrder(newOrder);

    std::cout << "Hashed Order " << order1 << ": " << hashOrder1 << std::endl;
    std::cout << "Hashed New Order: " << hashNewOrder << std::endl;

    if (hashOrder1 == hashNewOrder) {
        std::cout << "Collision detected! Hashes should not be equal." << std::endl;
    }
    else {
        std::cout << "No hash collisions detected." << std::endl;
    }

    // Step 3: Same customer places a new order while their current one is being processed
    int customerID = 1;
    customerOrders[customerID].push_back(order1);  // Customer's first order

    // Customer places a second order while the first is still being processed
    int secondOrder = idGen.generateID();
    customerOrders[customerID].push_back(secondOrder);

    std::cout << "Customer " << customerID << " orders: ";
    for (int order : customerOrders[customerID]) {
        std::cout << order << " ";
    }
    std::cout << std::endl;

    return 0;
}
