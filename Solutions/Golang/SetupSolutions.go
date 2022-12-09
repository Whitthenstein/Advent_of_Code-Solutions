package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"
)

func getPuzzleInput(year string, f string) {
	file := filepath.Join("..", "..", "Inputs", year, f)
	content, err := os.ReadFile(file)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(content))
}
