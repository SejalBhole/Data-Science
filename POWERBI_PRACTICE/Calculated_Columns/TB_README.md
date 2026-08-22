# Power BI DAX - Calculated Columns Exercise

## Overview
This repository contains my practice work for creating DAX calculated columns in Microsoft Power BI Desktop. The exercise uses a dataset of the world's tallest buildings.

## What I Did
* **Data Exploring:** Opened the Power BI file and looked at the `Building` table in the Table view.
* **Calculated Column 1 (`Total floors`):** Created a new column by adding the `Floors above ground` and `Floors below ground` together.
* **Calculated Column 2 (`Average floor height`):** Created another column by dividing the building's `Height m` by the `Floors above ground` using the `DIVIDE()` function.
* **Formatting:** Cleaned up the `Average floor height` column to show only two decimal places.
* **Visualizing:** Added a table visual in the Report view to display and sort the final results.

## What I Learned
* How to create and name new calculated columns using DAX.
* How to use basic math operations and functions like `DIVIDE()` in Power BI.
* How to format decimal numbers using the Column Tools.
* How to add the newly created data into a report visual.
