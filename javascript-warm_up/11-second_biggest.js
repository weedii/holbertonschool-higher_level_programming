#!/usr/bin/node
const arr = process.argv.slice(2).map(n => n);

if (arr.length < 2) {
  console.log('0');
} else {
  arr.sort((a, b) => b - a);
  console.log(arr[1]);
}
