#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  const uniqueNumbers = [...new Set(numbers)];

  uniqueNumbers.sort((a, b) => b - a);

  if (uniqueNumbers.length > 1) {
    console.log(uniqueNumbers[1]);
  } else {
    console.log(uniqueNumbers[0]);
  }
}
