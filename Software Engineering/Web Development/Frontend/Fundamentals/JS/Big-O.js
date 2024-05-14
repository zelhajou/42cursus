        const nemo = ['nemo'];
        const everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank'];
        const large = new Array(10).fill('nemo');

        function findNemo(array) {
                let t0 = performance.now();
                for (let i = 0; i < array.length; i++) {
                        if (array[i] === 'nemo') {
                                console.log('Found NEMO!');
                        }
                }
                let t1 = performance.now()
                console.log('Call to find Nemo took ' + (t1 - t0) + ' milliseconds');
        }

        findNemo(large); // O(n) --> Linear Time
        // Big O notation: O(n) --> Linear Time

        // Log all pairs of array
        const boxes = [0, 1, 2, 3, 4, 5];
        function logFirstTwoBoxes(boxes) {
                console.log(boxes[0]); // O(1)
                console.log(boxes[1]); // O(1)
        }
        // Big O notation: O(2) --> Constant Time
        logFirstTwoBoxes(boxes); // O(2)


        function compressBoxesTwice(boxes, boxes2) {
                boxes.forEach(function (boxes) {
                        console.log(boxes);
                });

                boxes2.forEach(function (boxes) {
                        console.log(boxes);
                });
        }
        // O(a + b) 
        // O(a*b)


        // log all pairs of array
        const boxes1 = ['a', 'b', 'c', 'd', 'e'];

        function logAllPairsOfArray(array) {
                for (let i = 0; i < array.length; i++) {
                        for (let j = 0; j < array.length; j++) {
                                console.log(array[i], array[j]);
                        }
                }
        }

        logAllPairsOfArray(boxes1); // Big O notation: O(n^2) --> Quadratic Time

        function printAllNumbersThenAllPairSums(numbers) {
                console.log('these are the numbers:');
                numbers.forEach(function (number) {
                        console.log(number);
                });

                console.log('and these are their sums:');
                numbers.forEach(function (firstNumber) {
                        numbers.forEach(function (secondNumber) {
                                console.log(firstNumber + secondNumber);
                        });
                });
        } 

        printAllNumbersThenAllPairSums([1, 2, 3, 4, 5]); // O(n + n^2) --> Quadratic Time

        // Rule 1: Worst Case
        // Rule 2: Remove Constants
        // Rule 3: Different terms for inputs
        // Rule 4: Drop Non Dominants

