Given /^I am not playing yet$/ do  
end

When /^I start the game$/ do
  game = Codebreaker::Game.new(output)
  game.start
end

Then /^I should see "([^"]*)"$/ do |msg|
  output.messages.should include(msg)  
end


Given /^the secret code is "([^"]*)"$/ do |code|
  @game = Codebreaker::Game.new(output)
  @game.start(code)
end

When /^I submit a guess "([^"]*)"$/ do |guess|
  @game.guess(guess)
end

Then /^the mark should be "([^"]*)"$/ do |mark|
  output.messages.should include(mark)
end


class Output
  def messages
    @messages ||= []
  end
  
  def puts(msg)
    messages << msg
  end
end

def output
  @output ||= Output.new
end
