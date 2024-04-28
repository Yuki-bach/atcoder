n = gets.chomp.to_i
s = gets.chomp.split('').map{ |e| e.to_i }
puts s.index(1).even? ? "Takahashi" : "Aoki"
