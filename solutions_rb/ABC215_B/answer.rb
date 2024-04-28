n = gets.to_i
k = 0
while 2 ** k <= n
  k += 1
end

puts k - 1

## Alternative
# n = gets.to_i
# k = (0..).bsearch{|k| 2**k > n}
# puts k - 1