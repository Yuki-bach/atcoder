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

function main() {
  const N: number = nextNum();
  const posList: number[][] = [];
  for (let i = 0; i < N; i++) {
    posList.push(nextNums(2));
  }

  const matrix: number[][] = [];
  for (let i = 0; i < N; i++) {
    matrix[i] = [];
    for (let j = 0; j < N; j++) {
      matrix[i].push(
        (posList[i][0] - posList[j][0]) ** 2 +
          (posList[i][1] - posList[j][1]) ** 2
      );
    }
  }
  matrix.forEach((row) => {
    const maxValue = (Math.max(...row.filter((v) => v !== 0)));
    console.log(row.findIndex((v) => v === maxValue) + 1);
  });
}

// $ npm run complete --task=sample
