# Excel Practice --- PivotTable: Holiday Analysis

## Date

20 August 2026

## Topic

**PivotTables in Microsoft Excel**

## Exercise

**Holiday Data --- Average Price Analysis**

This practice exercise used a holiday dataset to build a PivotTable and
answer a business-style question using multiple filters and a calculated
value.

## Business Question

Find the **average holiday price for each country** when all of the
following conditions are satisfied:

-   Travel Method = **Plane**
-   Number of Days \>= **7**
-   Resort Name **starts with S**
-   Show only countries where the resulting **Average Price \> £500**

## PivotTable Setup

### Rows

**Country**

Country is placed in the Rows area because the requirement is to compare
the average holiday price **country by country**.

### Values

**Price → Average**

The Price field is placed in Values and changed from the default **Sum**
to **Average**.

### Filters

-   **Travel Method → Plane**
-   **No of Days → \>= 7**
-   **Resort Name → Begins With S**

These filters determine which individual holiday records are included in
the calculation.

## Value Filter

After calculating the average price for each country, a **Value Filter**
is applied:

**Average of Price \> £500**

This is different from the normal filters.

-   **Normal filters** decide which source records participate in the
    calculation.
-   **Value filters** decide which summarized results remain visible
    after the calculation.

## PivotTable Concepts Practiced

-   Creating a PivotTable
-   Adding fields to Rows
-   Adding numeric fields to Values
-   Changing Sum to Average
-   Applying multiple filters
-   Using Number Filters such as `>= 7`
-   Using text filters such as **Begins With**
-   Using Value Filters on calculated results
-   Understanding source-data filters vs. value filters
-   Reading country-wise summary results

## Key Learning

The analysis follows this logic:

``` text
Raw Holiday Data
       ↓
Travel Method = Plane
       ↓
No of Days >= 7
       ↓
Resort Name starts with S
       ↓
Group by Country
       ↓
Calculate Average Price
       ↓
Keep countries where Average Price > £500
```

## Interview Takeaway

> I used a PivotTable to analyze holiday prices by country. I placed
> Country in Rows and Price in Values, changed the aggregation from Sum
> to Average, and applied multiple filters for travel method, number of
> days, and resort name. I then used a Value Filter to display only
> countries whose calculated average price was greater than £500.

## Important Interview Concept

**A normal filter and a Value Filter are not the same.**

For example:

-   `Travel Method = Plane` filters the original records.
-   `No of Days >= 7` filters the original records.
-   `Resort Name begins with S` filters the original records.
-   `Average Price > £500` filters the **calculated PivotTable
    results**.

