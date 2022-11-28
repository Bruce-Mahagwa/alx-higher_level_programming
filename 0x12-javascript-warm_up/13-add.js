#!/usr/bin/node
// adds 2 integers and exports function
exports.add = function(first, second) {
  if (!isNaN(first) && !isNaN(second)) {
    return parseInt(first) + parseInt(second);
  }
}
