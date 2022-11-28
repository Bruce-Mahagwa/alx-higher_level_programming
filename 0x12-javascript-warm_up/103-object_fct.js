#!/usr/bin/node
// increments value using an object method
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function() {
  return myObject.value++;
}
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
