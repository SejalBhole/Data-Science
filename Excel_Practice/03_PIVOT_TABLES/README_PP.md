# Excel Practice --- PivotTable: House Search Analysis

## Date

20 August 2026

## Topic

**PivotTables in Microsoft Excel**

## Exercise

**Creating a PivotTable to Analyse the Results of a House Search**

This exercise used a property portfolio dataset to practice creating and
modifying PivotTables, changing aggregation functions, applying multiple
filters, and using PivotTable drill-down.

## Part 1 --- Property Count by Type and Location

The first PivotTable was set up to show:

-   **Asking Price** → Values
-   **Type of Property** → Rows
-   **Location** → Columns
-   **Remaining fields** → Filters

The purpose was to summarize the property portfolio by property type and
location.

### Filters

The PivotTable was then filtered to show properties with:

-   **3 bedrooms**
-   **Medium garden**
-   **2 bathrooms**

The value calculation was changed to a **Count of properties**.

### Drill-Down

The exercise also required identifying the one **Detached** property
that matched the selected criteria.

By double-clicking the relevant PivotTable cell, Excel creates a new
worksheet containing the underlying property record.

This is known as **drill-down / Show Details**.

------------------------------------------------------------------------

## Part 2 --- Average Asking Price

The PivotTable was then changed to answer a different business question.

### PivotTable Layout

-   **Postcode** → Rows
-   **Type of Property** → Columns
-   **Remaining fields** → Filters
-   **Asking Price** → Values

The Asking Price aggregation was changed to **Average**.

### Filters

The PivotTable was filtered to show properties with:

-   **2 bathrooms**
-   **2 or 3 bedrooms**
-   **Countryside** location

The resulting PivotTable shows the **average asking price by postcode
and property type**.

### Drill-Down

The exercise also required double-clicking a property price in the
PivotTable to view the full underlying property details.

------------------------------------------------------------------------

## Key Excel Skills Practiced

-   Creating a PivotTable
-   Understanding **Rows**, **Columns**, **Filters**, and **Values**
-   Using a numeric field as a Value
-   Changing **Sum** to **Count**
-   Changing **Sum** to **Average**
-   Applying multiple filters
-   Filtering based on property characteristics
-   Using **OR logic** for 2 or 3 bedrooms
-   Using PivotTable drill-down / Show Details
-   Analyzing summarized data by property type, location, and postcode

## Important Learning

### 1. Rows vs Columns

**Rows** are useful when you want to list categories vertically.

Example:

> Postcode → Rows

**Columns** are useful when you want to compare categories horizontally.

Example:

> Property Type → Columns

### 2. Filters

Filters control which source records are included in the PivotTable
calculation.

For example:

> 2 bathrooms + 2 or 3 bedrooms + countryside

### 3. Count vs Average

**Count** answers:

> How many properties meet the criteria?

**Average** answers:

> What is the average asking price of the properties that meet the
> criteria?

### 4. Drill-Down

Double-clicking a PivotTable value shows the underlying records that
contributed to that result.

This is useful when someone asks:

> "Which properties make up this number?"

## Interview Takeaway

A good interview explanation is:

> I used a PivotTable to analyze a property portfolio. First, I
> summarized the number of properties by property type and location
> using filters for bedrooms, garden size, and bathrooms. Then I changed
> the PivotTable to calculate average asking prices by postcode and
> property type, applying filters for bathrooms, bedroom count, and
> countryside location. I also used PivotTable drill-down to inspect the
> underlying property records.

## Important Interview Concepts

### Q: Why would you use Count instead of Sum?

If the question is **how many properties**, Count is appropriate.

If the question is **total asking price**, Sum is appropriate.

If the question is **typical/average asking price**, Average is
appropriate.

### Q: How do you show properties with 2 OR 3 bedrooms?

The filter should allow both **2** and **3** to be selected.

This represents:

**Bedrooms = 2 OR Bedrooms = 3**

It is different from requiring one property to have both 2 and 3
bedrooms.

### Q: What is PivotTable drill-down?

Double-clicking a PivotTable result opens a new worksheet containing the
underlying source records used to produce that result.


