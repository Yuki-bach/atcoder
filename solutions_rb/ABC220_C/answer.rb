n = gets.chomp.to_i
a = gets.chomp.split.map{ |e| e.to_i }
x = gets.chomp.to_i

ans = n * (x / a.sum)
sum = a.sum * ans / n
while sum <= x
  sum += a[ans % n]
  ans += 1
end

puts ans
