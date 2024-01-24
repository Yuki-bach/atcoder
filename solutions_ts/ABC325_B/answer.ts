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
  const count :number[] = new Array(24).fill(0);
  for (let i = 0; i < N; i++) {
    const [W, X] = nextNums(2);
    for (let j = 9 - X; j < 18 - X; j++) {
      let jDash = j;
      if (jDash < 0) jDash += 24;
      else if (jDash >= 23) jDash -= 24;
      count[jDash] += W;
    }
  }
  const ans = Math.max(...count);
  console.log(ans);
}

// $ npm run complete --task=sample