package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func part1(nums []string) int {
	bigger := 0
	for i := 0; i < len(nums)-1; i++ {
		a, _ := strconv.Atoi(nums[i])
		b, _ := strconv.Atoi(nums[i+1])
		if b > a {
			bigger++
		}
	}
	return bigger
}

func part2(nums []string) int {
	bigger := 0
	prevsum := 0
	for i := 0; i < len(nums)-3; i++ {
		window := nums[i : i+3]
		wsum := 0
		for _, w := range window {
			n, _ := strconv.Atoi(w)
			wsum += n
		}
		if wsum > prevsum {
			bigger++
		}
		prevsum = wsum
	}
	return bigger
}

func main() {
	data, _ := os.ReadFile("day1.txt")
	ds := string(data)
	as := strings.Split(ds, "\n")

	fmt.Println(part1(as))
	fmt.Println(part2(as))
}
