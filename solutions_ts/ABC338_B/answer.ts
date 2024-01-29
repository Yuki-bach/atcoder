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

  const count :{[name: string]: number}= {};
  for (const c of S) {
    if (c in count) count[c] += 1
    else count[c] = 1
  }

  let ans :string = S[0];
  let maxCount :number = 0;
  for (const c of Object.keys(count)) {
    if (count[c] > maxCount) {
      maxCount = count[c]
      ans = c;
    } else if (count[c] === maxCount) {
      ans = c < ans ? c : ans;
    }
  }
  console.log(ans);
}

// $ npm run complete --task=sample