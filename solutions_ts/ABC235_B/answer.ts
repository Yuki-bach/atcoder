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
  // let pos = nextNum();
  // for (let i = 0; i < N - 1; i++) {
  //   const right = nextNum();
  //   if (pos < right) pos = right
  //   else {
  //     console.log(pos);
  //     break;
  //   }
  //   if (i === N - 2) console.log(right);
  // }

  const H = nextNums(N);
  for (let i = 0; i < N; i++) {
    if (H[i] >= H[i + 1] || i === N - 1) {
      console.log(H[i]);
      break;
    }
  }
}

// $ npm run complete --task=sample