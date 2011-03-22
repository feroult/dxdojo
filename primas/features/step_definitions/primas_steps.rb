When /^the word is "([^"]*)"$/ do |word|
  @word = word
end

Then /^the word is prime$/ do
  @word.prime?.should == true
end

Then /^the word is not prime$/ do
  @word.prime?.should == false
end



