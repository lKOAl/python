// bubbleSort, the worst (sane) sorting algortithm!
// not at all efficient, but it's easy to understand
// start from the bottom, compare each item against its neighbor,
// and swap them if they need to be swapped

function bubbleSort(arr) {
    // code to sort here 
    for (var i = 0; i < arr.length; i++)
        for (var j = i + 1; j < arr.length; j++)
            if (arr[i] > arr[j]) {
                var temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            }

    // sort in-place
}

let test_a = [8, 1, 4, 5, 9, 2, 7, 6, 3];
bubbleSort(test_a);
console.log(test_a); // should display [1, 2, 3, 4, 5, 6, 7, 8, 9]

let test_b = [1, 3, 2, 3, 6, 3, 3, 3, 3, 3, 5, 9, 3];
bubbleSort(test_b);
console.log(test_b); // should display [1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 6, 9]

// let x = [2, 1, 3, 4, 5];
// let temp = x[0];
// x[0] = x[1];
// x[1] = temp;