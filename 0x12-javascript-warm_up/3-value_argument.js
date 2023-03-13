#!/usr/bin/node

const first = () => {
  process.argv[2] ? console.log(process.argv[2]) : console.log('No argument');
};
first();
