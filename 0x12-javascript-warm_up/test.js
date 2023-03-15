#!/usr/bin/node
const person = {
    name: ['Bob', 'Smith'],
    age: 32,
    bio: function () {
        console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old`);
    },
    introduceself: function () {
        console.log(`Hi, I am ${this.name[0]}`);
    }
};

person.bio();
person.introduceself();
console.log(Object.getPrototypeOf(person));