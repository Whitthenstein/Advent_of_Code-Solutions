const { getPuzzleInput } = require("../SetupSolutions/SetupSolutions.js");

const year = "2022";
const day = "04";
const puzzleInput = getPuzzleInput(year, `Day_${day}.txt`).filter(el => el);
const puzzle = puzzleInput;

const getNumOfAllFullyContainedPairs = (puzzle) => {
    let total = 0;
    for (const line of puzzle) {
        const [one, two] = line.split(",");
        const [min_one, max_one] = one.split("-").map(el =>parseInt(el));
        const [min_two, max_two] = two.split("-").map(el =>parseInt(el));

        if ((min_one >= min_two && max_one <= max_two) || 
        (min_two >= min_one && max_two <= max_one)) {
            total += 1;
        }
    }

    return total;
};

const getNumOfAllOverlappingPairs = (puzzle) => {
    let total = 0;
    for (const line of puzzle) {
        const [one, two] = line.split(",");
        const [min_one, max_one] = one.split("-").map(el =>parseInt(el));
        const [min_two, max_two] = two.split("-").map(el =>parseInt(el));
        let list1 = []
        let list2 = []
        for (let i = min_one; i <= max_one; i++) {
            list1.push(i);
        }
        for (let i = min_two; i <= max_two; i++) {
            list2.push(i);
        }

        if (list2.some(el => el === min_one || el === max_one) 
        || list1.some(el => el === min_two || el === max_two)) {
            total += 1;
        }
    }

    return total;
};

// Script runs here
console.log(`Advent of Code - ${year}: Day ${day}`);
console.log("Part-One Answer:", getNumOfAllFullyContainedPairs(puzzle));
console.log("Part-Two Answer:", getNumOfAllOverlappingPairs(puzzle));