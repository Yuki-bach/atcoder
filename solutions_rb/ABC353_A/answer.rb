n = gets.to_i
h = gets.split.map { |e| e.to_i }

(1...n).each do |i|
  if h[i] > h[0]
    puts i + 1
    return
  end
end

puts -1
