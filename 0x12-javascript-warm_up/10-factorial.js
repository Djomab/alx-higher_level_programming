#!/usr/bin/node

/**
 * computes and prints a factorial
 * The first argument is integer
 * Factorial of NaN is 1
 */
const firstArg = parseInt(process.argv[2], 10);

function factorial (n) {
  if (isNaN(n) || n < 2) {
    return 1;
  }

  return n * factorial(n - 1);
}

console.log(factorial(firstArg));
