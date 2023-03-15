#!/usr/bin/node
const arr = require('./100-data');
const newList = arr.list.map((element, index) => element * index);
console.log(arr.list);
console.log(newList);
