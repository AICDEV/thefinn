package main

import (
	"bufio"
	"encoding/hex"
	"fmt"
	"os"
	"regexp"
	"sort"
	"strings"

	"gopkg.in/alecthomas/kingpin.v2"
)

var (
	msg = kingpin.Flag("message", "message you want to attack. (in hex)").Short('m').Required().String()
)

type charAnalyseResult struct {
	value string
	count int
}

type msgAnalyseResult struct {
	value int
	count int
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func cleanLine(s string) string {
	reg, err := regexp.Compile("[^a-zA-Z] ")
	check(err)
	s = strings.ToLower(s)
	s = reg.ReplaceAllString(s, "")

	return s
}

func processInputFile(path string) []string {
	file, err := os.Open(path)
	defer file.Close()
	check(err)

	scanner := bufio.NewScanner(file)
	res := []string{}

	for scanner.Scan() {
		res = append(res, cleanLine(scanner.Text()))
	}

	return res
}

func processContent(lines []string, bigramMap map[string]int, wordMap map[string]int) (map[string]int, map[string]int) {
	for _, line := range lines {
		words := strings.Split(line, " ")
		for _, word := range words {
			wordMap[word] = wordMap[word] + 1

			i := 0
			for i < len(word) {
				if (i + 1) < len(word) {
					bigram := word[i:(i + 2)]
					bigramMap[bigram] = bigramMap[bigram] + 1
				}
				i++
			}
		}
	}

	return bigramMap, wordMap
}

func getTopValuesFromMap(target map[string]int, top int) []charAnalyseResult {
	if top > len(target) {
		top = len(target)
	}
	values := make([]charAnalyseResult, 0, len(target))
	for key, value := range target {
		values = append(values, charAnalyseResult{key, value})
	}

	sort.SliceStable(values, func(i, j int) bool {
		return values[i].count > values[j].count
	})

	return values[:top]
}

func xor(a byte, b byte) byte {
	return a ^ b
}

func evaluateMessage(raw []byte, b byte) string {
	message := ""
	for _, rawB := range raw {
		c := string(xor(rawB, b))
		message += c
	}
	return message
}

func calcMatchScore(m string, topBigrams []charAnalyseResult, topWords []charAnalyseResult) int {
	mBigrams := make(map[string]int)
	mWords := make(map[string]int)
	score := 0

	m = cleanLine(m)

	processContent(strings.Split(m, " "), mBigrams, mWords)

	topMBigrams := getTopValuesFromMap(mBigrams, 10)
	topMWords := getTopValuesFromMap(mWords, 10)

	fmt.Println("--- evaluate message ---")

	for _, topBigram := range topBigrams {
		for _, topMBtopBigram := range topMBigrams {
			if topBigram.value == topMBtopBigram.value {
				score++
			}
		}
	}

	for _, topWord := range topWords {
		for _, topMWord := range topMWords {
			if topWord.value == topMWord.value {
				score++
			}
		}
	}
	fmt.Println("calculated score: ", score)
	return score
}

func main() {
	kingpin.Parse()

	bigrams := make(map[string]int)
	words := make(map[string]int)
	scoreList := []msgAnalyseResult{}

	refTextFiles := [2]string{"./data/the_adeventure_of_sherlock_holmes.txt", "./data/pride_and_prejudice.txt"}
	for _, file := range refTextFiles {
		fLines := processInputFile(file)
		processContent(fLines, bigrams, words)
	}

	topBigrams := getTopValuesFromMap(bigrams, 10)
	topWords := getTopValuesFromMap(words, 10)

	fmt.Println("--- generate reference values ---")
	fmt.Println(topBigrams)
	fmt.Println(topWords)
	fmt.Print("\n")

	fmt.Println("--- attack message ---")
	rawMessage, err := hex.DecodeString(*msg)
	check(err)

	for i := 0; i < 256; i++ {
		msg := evaluateMessage(rawMessage, byte(i))
		score := calcMatchScore(msg, topBigrams, topWords)
		scoreList = append(scoreList, msgAnalyseResult{i, score})
	}

	fmt.Println("top ten used keys -> try one of these")
	sort.SliceStable(scoreList, func(i, j int) bool {
		return scoreList[i].count > scoreList[j].count
	})

	for _, v := range scoreList[:10] {
		fmt.Printf("ascii int: %d \t %c \n", v.value, v.value)
	}
}
