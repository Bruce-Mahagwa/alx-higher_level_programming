#!/usr/bin/node
// prints factorial
function factorial() {
  const args = process.argv[2];
  if (isNaN(args)) {
    console.log(1);
} else {
    let num = parseInt(args);
    if (num < 0) {
      console.log(-1);
    } else if (num === 0) {
      console.log(1);
    } else {
        let result  = num;
        while (num > 1) {
	  num--;
          result *= num
         }
        console.log(result);
    }
}
}
factorial();
