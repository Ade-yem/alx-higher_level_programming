#!/usr/bin/node
const fs = require('fs');
try {
  const a = fs.readFileSync(process.argv[2], 'utf8');
  console.log(a);
} catch (e) {
  console.log(e);
}
