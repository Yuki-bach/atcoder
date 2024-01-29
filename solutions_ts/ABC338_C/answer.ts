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
  const Q = nextNums(N);
  const A = nextNums(N);
  const B = nextNums(N);

  let ans :number = 0;

  for (let aNum = 0; aNum < Math.max(...Q) + 1; aNum++) {
    const aChecker = A.every((a, i) => Q[i] >= a * aNum);
    if (!aChecker) break;
    const bNum = Math.min(...B.map((b, i) => b === 0 ? Infinity : Math.floor((Q[i] - A[i] * aNum) / b)));
    if (!Number.isNaN(bNum)) ans = Math.max(ans, aNum + bNum);
  }

  console.log(ans);
}

// $ npm run complete --task=sample