#!/usr/bin/node
function xtime (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
}

module.exports = xtime;
