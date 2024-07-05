package main

import (
	"bufio"
	"fmt"
	"net"
	"time"
)

func moveTopStepper() string {
	return "moveTop"
}

func moveBottomStepper() string {
	return "moveBottom"
}

func main() {
	// Connecting to the server
	conn, err := net.Dial("tcp", "127.0.0.1:8080")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer conn.Close()

	for {
		// Send a data to the server
		fmt.Fprintf(conn, "Hello world!\n")

		// Listen for a reply from the server
		msg, err := bufio.NewReader(conn).ReadString('\n')
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		fmt.Print("Message from server: " + msg)

		time.Sleep(2 * time.Second)
	}
}
