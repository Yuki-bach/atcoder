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
  for (let i = 0; i < length; ++i) arr[i] = next();
  return arr;
}
function nextNums(length: number) {
  const arr = [];
  for (let i = 0; i < length; ++i) arr[i] = nextNum();
  return arr;
}
function nextBigInts(length: number) {
  const arr = [];
  for (let i = 0; i < length; ++i) arr[i] = nextBigInt();
  return arr;
}

inputs = fs.readFileSync("/dev/stdin", "utf8");
inputArray = inputs.split(/\s/);
main();

function checker(S: string, T: string) {
  if (S === T) return true;
  for (let i = 0; i < S.length - 1; i++) {
    const SDash =
      S.substring(0, i) + S.at(i + 1) + S.at(i) + S.substring(i + 2);
    if (SDash === T) {
      return true;
    }
  }
  return false;
}

function main() {
  const S: string = next();
  const T: string = next();
  console.log(checker(S, T) ? "Yes" : "No");
}

// $ npm run complete --task=sample
