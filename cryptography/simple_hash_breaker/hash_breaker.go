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

var (
	hash     = kingpin.Flag("hash", "hash you want to attack").Short('h').String()
	wordlist = kingpin.Flag("wordlist", "path to wordlist you want to process").Short('w').Required().String()
	hashType = kingpin.Flag("type", "typ of your hash. either md5 or sha512").Short('t').Required().String()
)

func isCracked(calculatedHash string, raw string) {
	if *hash == calculatedHash {
		fmt.Println("\n \nhash cracked !!!")
		fmt.Printf("%v \t || \t %v \n", raw, calculatedHash)
		os.Exit(0)
	}
}

func processWordlist() {
	list, err := os.Open(*wordlist)

	if err != nil {
		log.Fatalf("unable to load wordlist: %v", err)
	}

	defer list.Close()

	scanner := bufio.NewScanner(list)

	for scanner.Scan() {
		scannerText := scanner.Text()
		data := []byte(scannerText)

		switch *hashType {
		case "md5":
			sum := md5.Sum(data)
			sumHex := hex.EncodeToString(sum[:])
			fmt.Printf("process: %v \t\t %v \n", scannerText, sumHex)

			isCracked(sumHex, scannerText)

		case "sha512":
			sum := sha512.Sum512(data)
			sumHex := hex.EncodeToString(sum[:])
			fmt.Printf("process: %v \t\t %v \n", scannerText, sumHex)

			isCracked(sumHex, scannerText)

		default:
			log.Fatal("unsupported hash type")
			os.Exit(1)
		}
	}
}

func main() {
	fmt.Printf("attacking hash: %v \n", *hash)

	kingpin.Parse()
	processWordlist()
}
