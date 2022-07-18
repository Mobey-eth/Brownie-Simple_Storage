// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract simpleStorage {
    // This will get initialized to 0!
    uint256 favNum;

    struct People {
        uint256 favNum;
        string name;
    }

    People[] public person;
    // mapping attaches a value to a key
    mapping(string => uint256) public nameToFavNum;

    // People public person = People({favNum: 2, name: "moby"});

    function store(uint256 _favNum) public returns (uint256) {
        favNum = _favNum;
        return _favNum;
    }

    // view(reading a state of the chain) and pure(do some type of math w/o saving state) are non state changing functions
    function retrieve() public view returns (uint256) {
        return favNum;
    }

    // function to add person(object) to an array and a mapping
    function addPerson(uint256 _favNum, string memory _name) public {
        person.push(People(_favNum, _name));
        nameToFavNum[_name] = _favNum;
    }
}