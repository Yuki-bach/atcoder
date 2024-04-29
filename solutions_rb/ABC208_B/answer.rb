p = gets.to_i
cur = 0
ans = 0

(1..10).reverse_each do |i|
  coin = (1..i).inject(1, :*)
  num = (p - cur) / coin
  cur += coin * num
  ans += num
end

puts ans