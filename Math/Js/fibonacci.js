const prompt = require('prompt-sync')(); // Usar a função prompt() diretamente

function calcularFibonacciJS() {
    const input = prompt("Digite um número inteiro:");
    const numero = parseInt(input);
  
    if (isNaN(numero) || !Number.isInteger(numero) || numero < 0) {
      console.log("Entrada inválida. Por favor, digite um número inteiro não negativo.");
      return;
    }
  
    const fibonacci = [0, 1];
    for (let i = 2; i <= numero; i++) {
      fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    }
  
    console.log(`Sequência de Fibonacci até ${numero}: ${fibonacci.slice(0, numero + 1).join(', ')}`);
  }
  
  calcularFibonacciJS();
  