const fs = require('fs');

let data1 = fs.readFileSync('file.txt', 'utf-8');
let lines1 = new Set(data1.split("\n"));

let data2 = fs.readFileSync('file2.txt', 'utf-8');
letlines2 = new Set(data2.split("\n"));

console.log('First set:',lines1);
console.log('Second set:',lines2);

let intersection = new Set([...lines1].filter(x =>lines2.has(x)));

if (intersection.size > 0) {
    console.log('Matches found:', intersection);
} else {
    console.log('No matches found');
}