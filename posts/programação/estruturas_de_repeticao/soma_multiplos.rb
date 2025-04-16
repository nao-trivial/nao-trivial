a = gets.chomp.to_i
b = gets.chomp.to_i
c = gets.chomp.to_i

contador = 1
soma = 0

while contador < c
  if contador % a == 0 || contador % b == 0
    soma += contador
  end
  contador += 1
end

puts soma