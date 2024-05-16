n, k = gets.chomp.split.map {|e| e.to_i }
a = gets.chomp.split.map { |e| e.to_i }

i = 0
cnt = 0
cur = k

while i < n do
  if cur >= a[i]
    cur -= a[i]
    i += 1
  else
    cur = k
    cnt += 1
  end
end

puts cnt + 1