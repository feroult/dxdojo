class Fixnum
  def prime?
    qtd_divisores = 0
    1.upto(self) do |i|
      if self % i == 0
        qtd_divisores += 1
      end            
    end
    qtd_divisores <= 2
  end
end

class String
  def prime?
    sum.prime?
  end

  def sum
    @letters = ('a'..'z').to_a + ('A'..'Z').to_a
    self.split('').inject(0) do |sum, letter|
      sum += @letters.index(letter) + 1 
    end
  end
end
