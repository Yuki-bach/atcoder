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
  const S: string[] = next().split("");
  const uniqueList = [...new Set(S)];

  const countList: number[] = [];
  uniqueList.forEach((value) => {
    countList.push(S.filter((v) => v === value).length);
  });

  let ans = "Yes";

  for (let i = 0; i < Math.max(...countList); i++) {
    const count = countList.filter((v) => v === i + 1).length;
    if (count !== 0 && count !== 2) {
      ans = "No";
    }
  }

  console.log(ans);
}

// $ npm run complete --task=sample