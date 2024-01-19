import * as fs from "fs";
const inputs = fs.readFileSync("/dev/stdin", "utf8");

const [a, b, c] = inputs.split("").map(Number);
const ans = (a + b + c) * 111;
console.log(ans);

// $ npm run complete --task=sample