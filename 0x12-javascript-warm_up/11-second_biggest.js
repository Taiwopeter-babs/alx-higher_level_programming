#!/usr/bin/node

(function () {
  if (process.argv.length === 2 || process.argv.length === 3) {
    console.log(0);
  }
  const args = process.argv.slice(2);
  const arr = args.map((num) => parseInt(num, 10));
  arr.sort((a, b) => a - b);
  console.log(arr);

  for (let i = arr.length - 2; i >= 0; i--) {
    if (arr[i] !== arr[arr.length - 1]) {
      console.log(arr[i]);
      break;
    }
  }
})();
