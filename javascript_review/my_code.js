// const name = "Joseph";
let age = 10;
// var email = "asdfasdf"; dont do this

function doSomething(myArg) {
  myArg[2] = 15;
}

const myFunc = function() {
  console.log(arguments);
}

const myFunc2 = () => {
  console.log(arguments);
}

const id = 1
// const name = "Joseph"
const email = "joseph.ditton@usu.edu"
const isTeacher = true

const user = {
  id,
  name,
  email,
  isTeacher
}

console.log(user);

let name = undefined;


function sayHello() {

}

name && sayHello();

console.log(myBoolean);
const nums = [1,2,3,4,5];
const [asdf, qwer, asdfasdf] = nums;


function displayTeacher({ id, name, email, isTeacher }) {
  console.log(id, name, email, isTeacher);
}

displayTeacher(user);



const newNums = nums.map(num => num * 2);
// const newNums = nums.map((num) => {
//   return num * 2;
// });

console.log(newNums);



// doSomething(nums);

// console.log(nums);
// myFunc2(1,2,3,4, "asdf", [1,2,3], {name: "asdf"})