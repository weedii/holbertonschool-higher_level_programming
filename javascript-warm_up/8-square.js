#!/usr/bin/node
const arg = process.argv[2]
const size = parseInt(arg)

if (isNaN(size) || arg === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      console.log('X');
    }
  }
}