# Ranking Method

The goal is to introduce a ranking methodology to create metrics that can flexibly
combines various dimensions that might affect positively or negatively.

## Approach

To combine various variables they need to be normalized. To normalize the numbers
we use Z-score and convert the values to a measure of distance.

Z-score measures how many standard deviations away a value is from its mean and is
represented by  :-

    (mean(X) - x) / std(X)

here,
    X is the list of values in the column
    x is the value
    std is Standard Deviation

Calculate Z-score for all the values per column that are required.

For Example, if there we need to combine column A, B and C where A is a negative
factor and B & C are positive factors.

After calculating the Z-score we can combine the columns A, B and C as : -

    B + C - A

Applying this to each row will give us a number representing the Ranks of each row.
The same formula can be used at District and Block level to create rankings for Blocks
and District.
