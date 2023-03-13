#!/usr/bin/node
const argv = process.argv
const num = parseInt(argv[2])
let s;
if (num === NaN || argv[2] == undefined) {
    console.log('Missing size')
} else {
    for (let i = 0; i < num; i++) {
        s = ''
        for (let j = 0; j < num; j++) {
            s += 'X'      
        }
        console.log(s);
    }
    
}
        