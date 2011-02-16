Feature: Codebreaker starts game

  In order to start breaking codes
  As a codebreaker
  I want to start playing the game

Scenario: starts the game
  Given I am not playing yet
  When I start the game
  Then I should see "welcome to codebreaker"
  And I should see "submit a guess:"
