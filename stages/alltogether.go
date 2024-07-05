package main

import (
	"errors"
	"fmt"
)

type userInfo struct {
	name          string
	orderNum      uint8
	numberOfBoxes uint16

	// start  / end for each stage
	stageFlag string
}

// Global queue for all of the stages
var globalOrderQueue []userInfo

type systemCheck struct {
	ordersInSystem uint16
}

func orderQueue(orders []userInfo, system *systemCheck) error {

	// -- list of the orders on a GUI and show the queue list and order information

	// init struct and error check
	// var smallOrders, mediumOrders, largeOrders []orderinfo

	for _, order := range orders {
		// Check if the current order exceeds the limit
		if system.ordersInSystem+order.numberOfBoxes > 30 {
			return errors.New("Enqueuing orders exceeds the limit of 30")
		}
		// Update the count of the orders
		system.ordersInSystem += order.numberOfBoxes
		// Append the order to a global queue
		globalOrderQueue = append(globalOrderQueue, order)
	}
	return nil
	// this requires holding about 30 orders to catagorize
	// in small medium and large orders
	// small - 0 to 10 boxes
	// medium - 10 to 20 boxes
	// large - 20 to 30 boxes

	// the update the stage flag
	// ordersInSystem
	//preppingStage()
}

// Simulates processing each order through prep and harvest stages,
// and removing the order from the global order queue while updating the system state
func processOrders(system *systemCheck) {
	for len(globalOrderQueue) > 0 {
		// Get the 1st order
		order := globalOrderQueue[0]
		// Dequeue the global order queue
		globalOrderQueue = globalOrderQueue[1:]

		// Prepping the order
		order.stageFlag = "prepStage"
		preppingStage(&order)

		// Harvesting the order
		order.stageFlag = "harvestStage"
		harverstStage(&order)

		// Archiving the order
		order.stageFlag = "archiveStage"
		archiveStage(&order)

		// Update the count of orders in the system
		system.ordersInSystem -= order.numberOfBoxes
	}
}

func preppingStage(order *userInfo) {

	// Wireless Hardware Communication
	// we need to set a flag for the tcp server to pick up the order
	// and begin the order, tcp server will notify prep stage its began

	// dw rn -- update some gui framework with working order

	fmt.Printf("Prepping order: %+v\n", *order)
	// Simulate connection with the TCP
	//return
}

func harverstStage(order *userInfo) {

	// Wireless Hardware Communication
	// we need to set a flag for the tcp server to pick up the order
	// and begin the order, tcp server will notify prep stage its began

	// dw rn -- update some gui framework with working order
	fmt.Printf("Harvesting order: %+v\n", *order)
	// Simulate connection with the TCP
	//return
}

func archiveStage(order *userInfo) {

	// Wireless Hardware Communication
	// we need to set a flag for the tcp server to pick up the order
	// and begin the order, tcp server will notify prep stage its began

	// dw rn -- update some gui framework with working order

	fmt.Printf("Archiving order: %+v\n", *order)
	// talk to database that the order has been completed
	//return
}

// growing
// harvesting
// archive order -- apprend to

func main() {
	orders := []userInfo{
		{"Khulan", 1, 5, ""},
		{"Hangal", 2, 11, ""},
		{"Faizan", 5, 3, ""},
		{"Taite", 1, 1, ""},
	}

	system := systemCheck{ordersInSystem: 0}

	err := orderQueue(orders, &system)

	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	// Process all of the orders
	processOrders(&system)
}
