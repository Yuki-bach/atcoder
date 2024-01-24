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
  const [N, D, P] = nextNums(3);
  const F = nextNums(N);
  F.sort((a, b) => b - a);

  let ans = 0;
  let i = 0;
  while(i < N) {
    const sum = F.slice(i, i + D).reduce((sum, item) => sum + item, 0);
    if (sum >= P) {
      ans += P;
      i += D;
    }
    else break;
  }
  ans += F.slice(i, N).reduce((sum, item) => sum + item, 0);
  console.log(ans);
}

// $ npm run complete --task=sample