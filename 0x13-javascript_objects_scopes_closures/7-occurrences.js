#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (let e = 0; e < list.length; e++) {
    counter = (list[e] === searchElement ? counter + 1 : counter);
  }

  return counter;
};
