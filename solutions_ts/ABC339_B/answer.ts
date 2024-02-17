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
  const [H, W, N] = nextNums(3);

  let matrix = new Array(H);
  for (let i = 0; i < H; i++) {
    matrix[i] = new Array(W).fill(".");
  }
  
  const moves = [
    [0, -1],
    [1, 0],
    [0, 1],
    [-1, 0],
  ];
  let dir = 0;
  let pos = [0, 0];

  for (let i = 0; i < N; i++) {
    if (matrix[pos[1]][pos[0]] === ".") {
      matrix[pos[1]][pos[0]] = "#";
      dir = dir < 3 ? dir + 1 : 0;
    } else {
      matrix[pos[1]][pos[0]] = ".";
      dir = dir > 0 ? dir - 1 : 3;
    }
    pos[0] += moves[dir][0];
    pos[1] += moves[dir][1];
    if (pos[0] < 0) pos[0] = W - 1;
    if (pos[0] > W - 1) pos[0] = 0;
    if (pos[1] < 0) pos[1] = H - 1;
    if (pos[1] > H - 1) pos[1] = 0;
  }
  matrix.forEach((row) => {
    console.log(row.join(""));
  });
}

// $ npm run complete --task=sample
