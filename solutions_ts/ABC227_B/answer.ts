import * as fs from "fs";

let inputs = "";
let inputArray: string[];
let currentIndex = 0;

function next() {
  return inputArray[currentIndex++];
}
function nextNum() {
  return +next();
}
// JavaScriptのnumber型は2^53(≒9*10^15)以上の数を正確に表すことができない。
function nextBigInt() {
  return BigInt(next());
}
function nexts(length: number) {
  const arr = [];
  for(let i = 0; i < length; ++i) arr[i] = next();
  return arr;
}
function nextNums(length: number) {
  const arr = [];
  for(let i = 0; i < length; ++i) arr[i] = nextNum();
  return arr;
}
function nextBigInts(length: number) {
  const arr = [];
  for(let i = 0; i < length; ++i) arr[i] = nextBigInt();
  return arr;
}

inputs = fs.readFileSync("/dev/stdin", "utf8");
inputArray = inputs.split(/\s/);
main();

function f(a :number, b :number) :number {
  return 4*a*b + 3*a + 3*b;
}

// area = 4ab + 3a + 3b
function main() {
  const N = nextNum();
  const S = nextNums(N);

  const sDash = [];
  for (let a = 1; a < 1000; a++) {
    for (let b = a; b < 1000; b++) {
      sDash.push(f(a, b));
    }
  }
  
  let cnt = 0;
  for (const s of S) {
    if (!sDash.includes(s)) {
      cnt += 1;
    }
  }
  console.log(cnt);
}

// $ npm run complete --task=sample