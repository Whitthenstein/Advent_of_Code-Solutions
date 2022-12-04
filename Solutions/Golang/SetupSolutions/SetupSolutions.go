package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func GetPuzzleInput() {
	file := filepath.Join("..", "..", "..", "Inputs", "")
	content, err := os.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(content))
}
