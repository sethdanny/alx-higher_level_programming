#!/usr/bin/node
const factorial = (n) => {
  if (n < 0) {
    return -1;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return (n * factorial(n - 1));
  }
};
console.log(factorial(Number(process.argv[2])));
