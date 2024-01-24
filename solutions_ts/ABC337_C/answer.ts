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
  const N = nextNum();
  const A = nextNums(N);
  const b = new Array(N + 1).fill(0);

  let tmp = 0
  for (let i = 0; i < N; i++) {
    if (A[i] === -1) {
      tmp = i + 1;
    } else {
      b[A[i]] = i + 1;
    }
  }
  
  const ans :number[] = [tmp];
  for (let i = 0; i < N - 1; i++) {
    tmp = b[tmp];
    ans.push(tmp);
  }
  console.log(...ans);
}
// $ npm run complete --task=sample