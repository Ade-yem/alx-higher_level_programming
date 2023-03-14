#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  for (const i of list) {
    arr.unshift(i);
  }
  return (arr);
};

