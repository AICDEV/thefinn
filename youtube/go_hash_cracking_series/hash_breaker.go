package main

import (
	"bufio"
	"crypto/md5"
	"crypto/sha512"
	"encoding/hex"
	"fmt"
	"log"
	"os"

	"gopkg.in/alecthomas/kingpin.v2"
)

type hashMessage struct {
	calcHash string
	raw      string
}

var (
	hash     = kingpin.Flag("hash", "the hash that you want to break").Short('h').Required().String()
	hashType = kingpin.Flag("type", "the type of hash you want to attack. for examle md5 or sha512").Short('t').Required().String()
	wordlist = kingpin.Flag("wordlist", "path to the wordlist you want to use").Short('w').Required().String()
)

func readWordlist() []string {
	list, err := os.Open(*wordlist)

	if err != nil {
		log.Fatalf("unable to load wordlist: %v", err)
	}

	defer list.Close()

	words := []string{}

	scanner := bufio.NewScanner(list)

	for scanner.Scan() {
		words = append(words, scanner.Text())
	}

	return words
}

func isHashCracked(calculatedHash string, raw string) {
	fmt.Println("process: ", calculatedHash, "raw: ", raw)

	if *hash == calculatedHash {
		fmt.Println("hash is broken")
		fmt.Println("hash: ", calculatedHash, " ===> ", raw)
		os.Exit(0)
	}
}

func calcHash(s string, c chan hashMessage) {
	sumHex := ""

	switch *hashType {
	case "md5":
		sum := md5.Sum([]byte(s))
		sumHex = hex.EncodeToString(sum[:])

	case "sha512":
		sum := sha512.Sum512([]byte(s))
		sumHex = hex.EncodeToString(sum[:])

	default:
		log.Fatal("unsupported hash type")
		os.Exit(1)
	}

	c <- hashMessage{sumHex, s}
}

func processWordlist() {

	c := make(chan hashMessage)

	for _, word := range readWordlist() {
		go calcHash(word, c)
	}

	for hm := range c {
		isHashCracked(hm.calcHash, hm.raw)
	}

}

func main() {
	fmt.Println("hashbreaker")

	kingpin.Parse()
	processWordlist()
}
