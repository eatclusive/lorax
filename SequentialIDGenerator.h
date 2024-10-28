//Simon Yang
//Eatclusive LLC
//Edited on 8/24/2024

#pragma once
// SequentialIDGenerator.h
#ifndef SEQUENTIAL_ID_GENERATOR_H
#define SEQUENTIAL_ID_GENERATOR_H

#include <set>
#include <stdexcept>

class SequentialIDGenerator {
private:
    std::set<int> idContainer;  // Container to store and keep IDs sorted automatically
    int nextAvailableID;        // Tracks the next available ID

public:
    // Constructor to initialize the first ID value
    SequentialIDGenerator() : nextAvailableID(1) {}

    // Function to generate and store a unique customer ID
    int generateID() {
        // Check if the current ID exists in the container
        while (idContainer.find(nextAvailableID) != idContainer.end()) {
            ++nextAvailableID;
        }

        // Store the unique ID in the container
        idContainer.insert(nextAvailableID);

        // Return the unique customer ID
        return nextAvailableID++;
    }

    // Function to check if a given ID exists in the container
    bool customerIDExists(int id) const {
        return idContainer.find(id) != idContainer.end();
    }

    // Function to get all the IDs (for any potential usage)
    std::set<int> getIDs() const {
        return idContainer;
    }
};

#endif // SEQUENTIAL_ID_GENERATOR_H
