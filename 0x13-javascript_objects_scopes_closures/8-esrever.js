#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  list.forEach(ele => {
    newList.unshift(ele);
  });
  return newList;
};
