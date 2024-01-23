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
  const S = next();
  let i = 0;

  for (const s of S) {
    if (s === "ABC"[i]) {
      continue;
    } else if (s === "ABC"[i + 1]) {
      i += 1;
    } else if (i + 2 <= 2 && s === "ABC"[i + 2]) {
      i += 2;
    } else {
      console.log("No");
      return;
    }
  }

  console.log("Yes");
}

// $ npm run complete --task=sample