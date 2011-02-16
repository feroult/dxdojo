module Codebreaker
  class Game
    def initialize(output)
      @output = output
    end

    def start(code = nil)
      @code = code
      @output.puts "welcome to codebreaker"        
      @output.puts "submit a guess:"
    end

    def guess(guess)
      @output.puts "+"*exact_match_count(guess) + "-"*number_match_count(guess)
    end

    def exact_match_count(guess)
      (0..3).inject(0) do |count, index|
        count += ( exact_match?(guess, index) ? 1 : 0 )
      end
    end

    def total_match_count(guess)
      code = @code.split('')      
      count = 0
      guess.split('').each do |d|
        if code.index(d)
          count += 1
          code.delete_at(code.index(d))
        end        
      end
      count
    end

    def number_match_count(guess)
      total_match_count(guess) - exact_match_count(guess)
    end

    def exact_match?(guess, index)
      @code[index] == guess[index]
    end
  end
end
