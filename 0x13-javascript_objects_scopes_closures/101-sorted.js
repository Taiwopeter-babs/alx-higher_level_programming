#!/usr/bin/node
const dict = require('./101-data.js').dict;

// get an array of unique values from the dict object
const newArray = Object.values(dict).filter((value, index) => {
  return Object.values(dict).indexOf(value) === index;
});
// create a new object
const newObject = {};
/*
 * create a new array for each value of Array newArray that holds
 * the keys with values matching the values in newArray
 */
for (let i = 0; i < newArray.length; i++) {
  const objValueArray = Object.keys(dict).filter((k) => dict[k] === newArray[i]);
  newObject[newArray[i]] = objValueArray;
}
console.log(newObject);
