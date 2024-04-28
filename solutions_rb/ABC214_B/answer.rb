s, t = gets.chomp.split.map{ |e| e.to_i }
count = 0

(0..s).each do |i|
  (0..s).each do |j|
    (0..s).each do |k|
      count += 1 if i + j + k <= s && i * j * k <= t
    end
  end
end

puts count