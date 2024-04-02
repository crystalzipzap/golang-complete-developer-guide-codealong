package main

import (
	"fmt"
	"strings"
)

//create a new type of deck which is a slice of strings
type deck []string

/**
	This function does not have a receiver because there isn't anything to receive yet
*/
func newDeck() deck {
	cards := deck{}

	cardSuits := []string{"Spades", "Diamonds", "Hearts", "Clubs"}
	cardValues := []string{"Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"}

	for _, suit := range cardSuits {
		for _, value := range cardValues {
			cards = append(cards, fmt.Sprint(value, " of ", suit))
		}
	}

	cards = append(cards, "Joker 1");
	cards = append(cards, "Joker 2")
	
	return cards
}


/**
	receiver: it gives this particular type mentioned here full access to the method
	d: the actual copy of the deck we are working with is available in the function as a variable d
	deck: Every variable of type 'deck' can call this function on itself

	In JavaScript, a receiver here is similar to the keyword this. 
	By convention, a receiver is generally named by the first or second letter of the type
*/
func (d deck) print() {
	for i, card := range d {
		fmt.Println(i+1, card)
	}
}


func deal(d deck, handSize int) (deck, deck) {
	return d[:handSize], d[handSize:]
}

/**
	Receiver or arguments (TBD)
*/

func (d deck) toString() string {
	return strings.Join([]string(d), ",")
}