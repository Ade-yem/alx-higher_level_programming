#!/usr/bin/node
const argv = process.argv
function factorial(num) {
    if (!num) return 1;
    return (num * factorial(num - 1))
}
console.log(factorial(parseInt(argv[2])))
