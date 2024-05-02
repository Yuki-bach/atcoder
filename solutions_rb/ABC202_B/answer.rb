s = gets.chomp
s_reversed = s.reverse
ans = s_reversed.tr('01689', '01986')
puts ans