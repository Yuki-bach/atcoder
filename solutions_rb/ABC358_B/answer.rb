n, a = gets.chomp.split.map(&:to_i)
t = gets.chomp.split.map(&:to_i)

s = 0 # seconds
t.each_with_index do |time, i|
  if s <= time
    s = time + a
  else
    s += a
  end
  puts s
end
