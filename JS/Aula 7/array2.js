// Iterando Arrays (Percorrendo Arrays)
//              0          1        2       3         4
const nomes = ["Maria", "Pedro", "Aline", "João", "Ricardo"];

// For Básico
console.log("For Básico");
for (let i = 0; i < nomes.length; i++) {
  console.log(`- ${nomes[i]}`);
}

// For Of
console.log("For Of");
for (let nome of nomes) {
  console.log(`- ${nome}`);
}

// For Each
console.log("For Each");
nomes.forEach((nome) => console.log(`- ${nome}`));
