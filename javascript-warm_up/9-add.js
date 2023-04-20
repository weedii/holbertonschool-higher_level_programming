#!/usr/bin/node
function add(a, b) {
    let sum = a + b;
    console.log(sum);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  add(num1, num2);
}
