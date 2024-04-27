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

function main() {
  const N: number = nextNum();
  const A: number[] = nextNums(N);
  const seq: number[] = [];

  for (let i = 0; i < N; ++i) {
    seq.push(A[i]);
    
    while (seq.length > 1 && seq.at(-2) === seq.at(-1)) {
      const ball = seq.pop()!;
      seq.pop()!;

      seq.push(ball + 1);
    }
  }
  console.log(seq.length);
}

// $ npm run complete --task=sample