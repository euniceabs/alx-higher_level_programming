#!/usr/bin/node

exports.esrever = function (list) {
  const reverseList = [];
  for (let e = list.length - 1; e >= 0; e--) {
    reverseList.push(list[e]);
  }

  return (reverseList);
};
