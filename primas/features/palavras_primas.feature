Feature: Palavras Primas

Scenario: One prime word with one letter
  When the word is "b"
  Then the word is prime
  
Scenario: One non prime word with one letter
  When the word is "d"
  Then the word is not prime
  
Scenario: prime words
  When the word is "ab"
  Then the word is prime
  
Scenario: prime words
  When the word is "eea"
  Then the word is prime

Scenario: non prime words
  When the word is "fd"
  Then the word is not prime
  
Scenario: prime words
  When the word is "Aaa"
  Then the word is prime
