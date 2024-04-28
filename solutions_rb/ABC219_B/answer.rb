strings = Array.new(3){ gets.chomp }
t = gets.chomp.chars.map{ |c| c.to_i }

ans = ''
t.each do |c|
  ans << strings[c-1]
end

puts ans
