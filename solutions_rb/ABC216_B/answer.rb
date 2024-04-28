n = gets.to_i
s = Array.new(n){ gets.chomp }
puts s.uniq.size == n ? 'No' : 'Yes'