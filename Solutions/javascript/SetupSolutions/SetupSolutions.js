const fs = require("fs");
const path = require("path");

module.exports = {
    getPuzzleInput: (year, day) => {
        const filePath = path.join(__dirname,"..", "..", "..", "Inputs", year, day);
        console.log(filePath);
        const allContents = fs.readFileSync(filePath, 'utf-8');
        const arr = allContents.split(/\r?\n/);
    
        return arr;
    }

}