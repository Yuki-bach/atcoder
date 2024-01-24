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

function checkBlack9(S :string[], row :number, col :number) {
  return S[row].slice(col, col + 3) === '###'
    && S[row + 1].slice(col, col + 3) === '###'
    && S[row + 2].slice(col, col + 3) === '###'
}

function checkWhiteTopLeft(S :string[], row :number, col :number) {
  return S[row][col + 3] === '.'
    && S[row + 1][col + 3] === '.'
    && S[row + 2][col + 3] === '.'
    && S[row + 3][col] === '.'
    && S[row + 3][col + 1] === '.'
    && S[row + 3][col + 2] === '.'
    && S[row + 3][col + 3] === '.';
}

function checkWhiteBotomRight(S :string[], row :number, col :number) {
  return S[row + 5][col + 5] === '.'
    && S[row + 5][col + 6] === '.'
    && S[row + 5][col + 7] === '.'
    && S[row + 5][col + 8] === '.'
    && S[row + 6][col + 5] === '.'
    && S[row + 7][col + 5] === '.'
    && S[row + 8][col + 5] === '.';
}

function main() {
  const [N, M] = nextNums(2);
  const S :string[] = [];
  for (let i = 0; i < N; i++) {
    S.push(next());
  }
  for (let row = 0; row <= N - 9; row++) {
    for (let col = 0; col <= M - 9; col++) {
      const checker = checkBlack9(S, row, col)
        && checkBlack9(S, row + 6, col + 6)
        && checkWhiteTopLeft(S, row, col)
        && checkWhiteBotomRight(S, row, col);
      if (checker) console.log(row + 1, col + 1);
    }
  }
}

// $ npm run complete --task=sample