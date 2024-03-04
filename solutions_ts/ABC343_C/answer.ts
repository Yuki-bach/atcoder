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
  const initX: number = Math.floor(Math.cbrt(N));

  for (let x = initX; x > 0; --x) {
    // Check x is palindrome
    const kStr: string = (x ** 3).toString();
    let isPalindrome: boolean = true;
    for (let i = 0; i < kStr.length; ++i) {
      if (kStr[i] !== kStr[kStr.length - 1 - i]) {
        isPalindrome = false;
        break;
      }
    }
    if (isPalindrome) {
      console.log(x ** 3);
      break;
    }
  }
}

// $ npm run complete --task=sample