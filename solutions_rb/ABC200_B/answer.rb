n, k = gets.chomp.split

k.to_i.times do
  if n.to_i % 200 == 0
    n = (n.to_i / 200).to_s
  else
    n += "200"
  end
end

puts n