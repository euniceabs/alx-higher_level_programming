#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  for (let e = 0; e < x; e++) theFunction();
};
