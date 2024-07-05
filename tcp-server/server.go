package main

import (
	"bufio"
	"fmt"
	"net"
	"strings"
)

func main() {
	// Listen to incoming connections + error checks
	listener, err := net.Listen("tcp", ":8080")

	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	// This waits for the function to complete before moving on
	defer listener.Close()

	fmt.Println("Server is listening on port 8080")

	for {
		// Accept incoming connections
		conn, err := listener.Accept()
		if err != nil {
			fmt.Println("Error:", err)
			continue
		}

		go handleClient(conn)
	}
}

func handleClient(conn net.Conn) {
	defer conn.Close()

	// Create a buffer to read data
	// buffer := make([]byte, 1024)

	reader := bufio.NewReader(conn)

	// Reading Client Data
	for {
		n, err := reader.ReadString('\n')
		if err != nil {
			fmt.Println("Error: ", err)
			return
		}

		fmt.Printf("Data Received: %s\n", string(n))

		// Writing to client a new message with the received message changed to uppercase letters
		newMessage := strings.ToUpper(n)

		conn.Write([]byte(newMessage + "\n"))
	}

	// Writing data back to the client
	// for {

	// }

}
