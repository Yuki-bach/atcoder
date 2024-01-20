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
  const points: number[][] = [];
  for (let i = 0; i < N; i++) {
    const [x, y] = nextNums(2);
    points.push([x, y]);
  }

  let ans = 0;
  for (let i = 0; i < N - 1; i++) {
    for (let j = i + 1; j < N; j++) {
      const len_squared = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2;
      ans = Math.max(ans, len_squared);
    }
  }
  console.log(Math.sqrt(ans));
}

// $ npm run complete --task=sample