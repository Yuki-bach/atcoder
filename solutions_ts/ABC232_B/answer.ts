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
  const S = next().split("");
  const T = next().split("");
  const zCode = 'z'.charCodeAt(0);

  for (let i = 0; i < 26; i++) {
    const SDash = S.map(s => {
      const code = s.charCodeAt(0);
      const newCharCode = (code + i <= zCode) ? code + i : code + i - 26;
      return String.fromCharCode(newCharCode);
    });
    if (T.join('') === SDash.join('')) {
      console.log("Yes");
      return;
    }
  }
  console.log("No");
}

// $ npm run complete --task=sample