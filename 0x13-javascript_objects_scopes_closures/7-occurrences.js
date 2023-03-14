#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach(ele => {
    if (ele === searchElement) {
      counter++;
    }
  });
  return counter;
};
