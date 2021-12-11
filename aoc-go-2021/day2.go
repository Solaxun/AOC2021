package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func parseinput(input string) [][]string {
	var result [][]string
	for _, instr := range strings.Split(input, "\n") {
		result = append(result, strings.Split(instr, " "))
	}
	return result
}

func part1(instr_pairs [][]string) int {
	var horizontal, depth int
	for _, ipair := range instr_pairs {
		dir, amt := ipair[0], ipair[1]
		num, _ := strconv.Atoi(amt)

		switch dir {
		case "forward":
			horizontal += num
		case "up":
			depth -= num
		case "down":
			depth += num
		}
	}

	return depth * horizontal
}

func part2(instr_pairs [][]string) int {
	var horizontal, depth, aim int
	for _, ipair := range instr_pairs {
		dir, amt := ipair[0], ipair[1]
		num, _ := strconv.Atoi(amt)

		switch dir {
		case "forward":
			horizontal += num
			depth += aim * num
		case "up":
			aim -= num
		case "down":
			aim += num
		}
	}
	return depth * horizontal
}

func main() {
	data, _ := os.ReadFile("day2.txt")
	ds := string(data)
	instr_pairs := parseinput(ds)
	p1 := part1(instr_pairs)
	p2 := part2(instr_pairs)
	fmt.Println(p1, p2)
}
