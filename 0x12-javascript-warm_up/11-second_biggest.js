#!/usr/bin/node

const args = process.argv.slice(2).map(Number).filter(n => !isNaN(n));
if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
