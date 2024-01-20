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
  type Total = {
    [key: string]: number
  };
  const total :Total = {};
  const N = nextNum();

  for (let i = 0; i < N; i++) {
    const s = next();
    if (total[s]) {
      total[s]++;
    } else {
      total[s] = 1;
    }
  }

  let maxCnt = 0;
  let ans;
  for (const key in total) {
    if (total[key] > maxCnt) {
      maxCnt = total[key];
      ans = key;
    }
  }
  console.log(ans);
}

// $ npm run complete --task=sample