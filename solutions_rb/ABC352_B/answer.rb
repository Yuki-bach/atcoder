s = gets.chomp.split("")
t = gets.chomp.split("")
s_i = 0
t_i = 0
ans = []

while s_i < s.length
  if s[s_i] == t[t_i]
    ans << t_i + 1
    s_i += 1
  end
  t_i += 1
end

puts ans.join(" ")