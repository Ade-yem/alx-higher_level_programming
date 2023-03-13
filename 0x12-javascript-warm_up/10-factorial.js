#!/usr/bin/node
const argv = process.argv;
function factorial (num) {
  if (!num || num === 0 || num === 1) return 1;
  return (num * factorial(num - 1));
}

console.log(factorial(parseInt(argv[2])));
