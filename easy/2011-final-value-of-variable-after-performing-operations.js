/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function(operations) {
    let value = 0;
    operations.forEach(op => {
        if(op == "X++" || op == "++X")
            ++value;
        else 
            --value;
    });
    return value;
};
