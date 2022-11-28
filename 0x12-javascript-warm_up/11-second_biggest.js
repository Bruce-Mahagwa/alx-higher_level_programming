#!/usr/bin/node
// prints biggest int in a list
let arr = [...process.argv.slice(2)];
if (arr.length <= 1) {
  console.log(0);
} else {
    arr = arr.map(item => parseInt(item));
    arr.sort((a, b) => {
      if (a < b) {
	return -1;
	}
      else if (a > b) {
	return 1;	
	}
      else {
	return 0;
	}
    });
      console.log(arr[arr.length - 2]);
}
