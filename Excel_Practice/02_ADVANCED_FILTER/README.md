# Excel Practice 02 --- Advanced Filter

## Date

20 August 2026

## Topic

Advanced Filter in Microsoft Excel

## What I Practiced

I practiced using Excel's **Advanced Filter** feature with a property
portfolio dataset. The exercise focused on filtering records using
multiple criteria and extracting the matching records to another
location.

## Practical Exercise 1 --- AND Conditions

I created a separate **Criteria Range** and used the following
conditions:

-   Postcode = **SK13**
-   Bedrooms = **3**
-   Garden Size = **Medium**
-   Cost / Asking Price \< **400,000**

Because these conditions were entered on the **same criteria row**,
Excel interprets them as:

**SK13 AND 3 bedrooms AND Medium garden AND price \< 400,000**

The matching records were then copied to the **Extract Range**.

## Practical Exercise 2 --- Different Criteria

I repeated the Advanced Filter exercise using:

-   Postcode = **SK14**
-   Bedrooms = **3**
-   Garden Size = **Medium**
-   Cost / Asking Price \< **400,000**

## AND / OR Logic Learned

A key concept I practiced was how Advanced Filter interprets the layout
of the Criteria Range:

-   **Conditions on the same row = AND**
-   **Conditions on different rows = OR**

For example:

  Postcode     Bedrooms
  ---------- ----------
  SK13                3
  SK14                4

is interpreted as:

**(SK13 AND 3 bedrooms) OR (SK14 AND 4 bedrooms)**

## Excel Features Practiced

-   Advanced Filter
-   List Range
-   Criteria Range
-   Extract / Copy To Range
-   Multiple criteria
-   AND conditions
-   OR conditions
-   Comparison operators such as `<400000`
-   Copying filtered results to another location

## Key Learning

Advanced Filter is useful when I need more controlled filtering than a
normal filter, especially when I want to use a separate criteria area
and extract matching records somewhere else.

## Interview Takeaway

I can explain Advanced Filter as:

> Advanced Filter allows me to filter a dataset using multiple criteria
> and copy the matching records to another location. The Criteria Range
> defines what I want to find, while the Extract Range defines where I
> want the results to appear.

A key rule I learned is:

**Same row → AND**\
**Different rows → OR**

