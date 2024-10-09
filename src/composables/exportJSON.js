// import destination from "@/assets/destination.json";

  
// for (const state in destination) {
// for (const activityCategory in destination[state]) {
//     destination[state][activityCategory].forEach(destination => {
//     destination.state = state;
//     destination.activityCategory = activityCategory;
//     });
// }
// }

// const fs = require('fs');

// const jsonData = destination;

// // Modify the JSON data as needed (e.g., add state and activityCategory properties)

// const jsonString = JSON.stringify(jsonData, null, 2); // Indent the JSON for better readability

// fs.writeFile('@/assets/destination_new.json', jsonString, (err) => {
// if (err) {
//     console.error('Error writing to file:', err);
// } else {
//     console.log('JSON data exported to output.json');
// }
// });


const fs = require('fs');

// Read the original JSON file (replace with your file path)
const rawData = fs.readFileSync('destination.json');
const destination = JSON.parse(rawData);
const modifiedDestinations = [];


// Add 'state' and 'activityCategory' to each destination object
for (const state in destination) {
  for (const activityCategory in destination[state]) {
    destination[state][activityCategory].forEach(destinationObj => {
      destinationObj.state = state;
      destinationObj.activityCategory = activityCategory;
      modifiedDestinations.push(destinationObj);
    });
  }
  
}

// Write the updated data back to a new JSON file
fs.writeFileSync('updated_destination.json', JSON.stringify(modifiedDestinations, null, 2));

console.log('Transformation complete. Check updated_destination.json file.');
