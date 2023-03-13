const argv = process.argv;
let a = 0;
while (argv[a] !== undefined) {
  a++;
}
if (!argv[2]) {
  console.log('No argument');
} else {
  for (let i = 2; i < a; i++) {
    console.log(argv[i]);
  }
}
