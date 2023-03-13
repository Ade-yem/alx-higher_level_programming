#!/usr/bin/node
const argv = process.argv;
if (argv.length <= 3) {
  console.log(0);
} else {
  const arg = argv.slice(2);
  arg.sort((a, b) => b - a);
  console.log(arg[1]);
}
