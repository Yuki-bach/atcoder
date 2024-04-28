numList = gets.chomp.split("").map{ |e| e.to_i}

if numList.uniq.size == 1
  puts "Weak"
else
  is_consecutive = true
  (1...4).each do |i|
    # 現在の数字の次の数字を計算 (9 の次は 0)
    expected_next = (numList[i-1] + 1) % 10
    if numList[i] != expected_next
      is_consecutive = false
      break
    end
  end

  puts is_consecutive ? "Weak" : "Strong"
end