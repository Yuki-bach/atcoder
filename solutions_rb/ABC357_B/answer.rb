s = gets.chomp
be_upper = s.count("A-Z") > s.count("a-z")
ans = be_upper ? s.upcase : s.downcase
puts ans
