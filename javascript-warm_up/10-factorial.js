#!/usr/bin/node
function factorial(n) {
  let i = 1;
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = process.argv[2];
const n = parseInt(arg);

if (isNaN(n)) {
  console.log('1');
} else {
  console.log(factorial(n));
}
