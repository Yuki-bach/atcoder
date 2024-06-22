n = gets.chomp
non_zero = n.gsub(/0+\z/, '')
puts non_zero == non_zero.reverse ? 'Yes' : 'No'
